from datetime import datetime
import logging

LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]

AUTHOR = 'Yi-Chang Chen'
SITEURL = ' '
SITENAME = 'YC Note'
SITETITLE = 'YC Note'
SITESUBTITLE = 'ML/DL Tech Blog'
SITEDESCRIPTION = '[ YC Note - ML/DL Tech Blog ] Hello, I am YC, an ML engineer/researcher with experience in CV, NLP/NLU, and Recommender. I built this blog for anyone interested in data science and machine learning.'

SITEDESC1 = "Hello, I am YC, an ML engineer/researcher with experience in CV, NLP/NLU, and Recommender. I also have experience in high-QPS ML systems. In my spare time, I'm a blogger and guitar singer."
SITEDESC2 = "This blog is a resource for anyone interested in data science and machine learning, featuring tutorials, research papers, and the latest industry technologies."

# SITELOGO = ''
FAVICON = '/images/favicon.png'
BROWSER_COLOR = '#FFFFFF'
THEME_COLOR = 'light'
PYGMENTS_STYLE = 'default'

ROBOTS = 'index, follow'

THEME = 'theme/Flex'
# PATH = 'content'
OUTPUT_PATH = 'output/'
TIMEZONE = 'Asia/Taipei'

DISABLE_URL_HASH = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': True},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'title': 'Table of Contents'},
    },
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'sitemap', 'related_posts', 'ga_pageviews', 'seo', 'neighbors', 'series', 'search']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'indexes': 0.2,
        'pages': 0.0,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly',
    }
}

MATH_JAX = {
    'color': 'black', #'#0B5345'
    'align': 'left',
    'indent': '1em',
    'linebreak_automatic': True,
    'responsive': True,
    'responsive_break': 768,
}

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer
SEO_ARTICLES_LIMIT = 30
SEO_PAGES_LIMIT = 30

SEARCH_MODE = 'output'
SEARCH_HTML_SELECTOR = 'div.main-contents'
STORK_VERSION = '1.5.0'

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

GITHUB_CORNER_URL = ''

SOCIAL = (
    ('facebook', 'https://www.facebook.com/yc.note'),
    ('github', 'https://github.com/GitYCC'),
    ('linkedin', 'https://www.linkedin.com/in/yi-chang-chen-aba1b6114/'),
)

MENUITEMS = (
    ('About Me', '/about-me.html'),
    ('AI.ML', '/category/aiml.html'),
    ('CS', '/category/cs.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike 4.0 International License',
    'version': '4.0',
    'slug': 'by-sa',
    'icon': True,
    'language': 'en_US',
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 30

ADD_THIS_ID = 'ra-63b4eabb5e84e9fb'

STATIC_PATHS = ['media', 'images', 'extra/ads.txt', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/ads.txt': {'path': 'ads.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False

USE_LESS = True
USE_GOOGLE_FONTS = True

GOOGLE_KEY_FILE = './ycnote_raw_source/secret/ga-viewer-373311-4e6bcfd54126.json'
VIEW_ID = '161391535'
GA_START_DATE = '2005-01-01'
GA_END_DATE = 'today'

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-5639899546876072',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '5718861428',
        'article_bottom': '',
    },
}

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
