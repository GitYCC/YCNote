import sys

from pelican import signals
from pelican.generators import ArticlesGenerator, PagesGenerator
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']


def initialize_analyticsreporting(key_file_location):
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        key_file_location, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_report(analytics, view_id, start_date, end_date):
    """Queries the Analytics Reporting API V4.

    Args:
    analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
    The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body={
        'reportRequests': [
        {
            'pageSize': 999999,
            'viewId': view_id,
            'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
            'metrics': [{'expression': 'ga:pageviews'}],
            'dimensions': [{'name': 'ga:pagePath'}]
        }]
        }
    ).execute()

def commafy(value):
    return '{:,d}'.format(value)

def get_pageviews(generators):
    generator = generators[0]
    key_file_location = generator.settings.get('GOOGLE_KEY_FILE', None)
    view_id = generator.settings.get('VIEW_ID', None)

    page_view = dict()
    try:
        start_date = generator.settings.get('GA_START_DATE', '2005-01-01')
        end_date = generator.settings.get('GA_END_DATE', 'today')

        analytics = initialize_analyticsreporting(key_file_location)
        response = get_report(analytics, view_id, start_date, end_date)
        for report in response.get('reports', []):
            for row in report.get('data', {}).get('rows', []):
                dimensions = row.get('dimensions')
                if not dimensions:
                    continue
                path = dimensions[0].split('?')[0]

                dateRangeValues = row.get('metrics', [])
                for values in dateRangeValues:
                    for value in values.get('values', []):
                        page_view[path] =  page_view.get(path, 0) + int(value)

    except Exception as e:
        sys.stderr.write("[ga_page_view] Failed to fetch page view information:\n{}\n".format(e))

    article_generator = [g for g in generators if type(g) is ArticlesGenerator][0]
    page_generator = [g for g in generators if type(g) is PagesGenerator][0]

    ARTICLE_SAVE_AS = generator.settings['ARTICLE_SAVE_AS']
    PAGE_SAVE_AS = generator.settings['PAGE_SAVE_AS']

    total_page_view = 0
    for pages, url_pattern in [(article_generator.articles, ARTICLE_SAVE_AS),
                               (page_generator.pages, PAGE_SAVE_AS)]:
        for page in pages:
            url = '/%s' % (url_pattern.format(**page.__dict__))
            pv = page_view.get(url, 0)
            setattr(page, 'pageview', commafy(pv))
            total_page_view += pv

    generator.context['total_page_view'] = commafy(total_page_view)


def register():
    signals.all_generators_finalized.connect(get_pageviews)
