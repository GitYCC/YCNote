import sys

from pelican import signals
from pelican.generators import ArticlesGenerator, PagesGenerator
from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


def get_report(client, property_id, start_date, end_date):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="pagePath")],
        metrics=[Metric(name="screenPageViews")],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    response = client.run_report(request)
    return response


def commafy(value):
    return '{:,d}'.format(value)


def get_pageviews(generators):
    generator = generators[0]
    key_file_location = generator.settings.get('GOOGLE_KEY_FILE', None)
    property_id = generator.settings.get('PROPERTY_ID', None)

    credentials = service_account.Credentials.from_service_account_file(
        key_file_location
    )
    client = BetaAnalyticsDataClient(credentials=credentials)
    start_date = generator.settings.get('GA_START_DATE', '2015-08-17')
    end_date = generator.settings.get('GA_END_DATE', 'today')

    page_view = generator.settings.get('HISTORY_PAGEVIEWS', dict())
    try:
        response = get_report(client, property_id, start_date, end_date)
        for row in response.rows:
            path = row.dimension_values[0].value
            value = row.metric_values[0].value
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
