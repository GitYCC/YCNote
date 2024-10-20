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

GOOGLE_KEY_FILE = './ycnote_raw_source/secret/ga-viewer-347801777.json'
PROPERTY_ID = '347801777'
GA_START_DATE = '2024-04-17'
GA_END_DATE = 'today'
HISTORY_PAGEVIEWS = {
   '/egypt-travel_7.html': 1092,
   '/deep-dl_4.html': 24988,
   '/about-me.html': 2908,
   '/sweet-child-oh-mine.html': 457,
   '/ml-course-techniques_5.html': 4892,
   '/uwarn-performance_2.html': 171,
   '/index2.html': 171,
   '/index.html': 2908,
   '/ml-course-techniques_4.html': 7931,
   '/python-play-with-data_1.html': 5469,
   '/tesla-aiday2021.html': 833,
   '/tensorflow-tutorial_1.html': 5571,
   '/egypt-travel_6.html': 834,
   '/ml-course-foundations_4.html': 17017,
   '/introduction-object-oriented-programming_2.html': 13549,
   '/ml-course-techniques_3.html': 6007,
   '/ml-course-foundations_3.html': 7667,
   '/confusion-matrix.html': 117683,
   '/egypt-travel_1.html': 577,
   '/tensorflow-tutorial_6.html': 12602,
   '/deep-dl_2.html': 37523,
   '/algorithm-complexity-theory.html': 69844,
   '/deep-dl_3.html': 19008,
   '/ml-course-foundations_2.html': 12246,
   '/ml-course-techniques_2.html': 11537,
   '/stock-sell-point.html': 6401,
   '/introduction-object-oriented-programming_3.html': 8877,
   '/ml-course-techniques_1.html': 10667,
   '/multithread-multiprocess-gil.html': 3821,
   '/tensorflow-tutorial_4.html': 13550,
   '/egypt-travel_3.html': 529,
   '/ml-course-foundations_1.html': 13262,
   '/egypt-travel_2.html': 415,
   '/diffusion-model.html': 7535,
   '/big-data-a-revolution.html': 665,
   '/tensorflow-tutorial_5.html': 6090,
   '/deep-dl_1.html': 13009,
   '/introduction-object-oriented-programming_1.html': 5698,
   '/crnn-ctc.html': 9303,
   '/tesla-aiday2022.html': 549,
   '/tensorflow-tutorial_2.html': 5559,
   '/egypt-travel_5.html': 474,
   '/how-to-read-books.html': 845,
   '/uwarn-performance_1.html': 175,
   '/ml-course-techniques_7.html': 14508,
   '/the-brain-the-story-of-you.html': 772,
   '/python-play-with-data_2.html': 13576,
   '/python-play-with-data_3.html': 4804,
   '/latest_ai_info.html': 3688,
   '/egypt-travel_8.html': 480,
   '/ml-course-techniques_6.html': 33722,
   '/egypt-travel_4.html': 482,
   '/the-selfish-gene.html': 1605,
   '/wide-and-deep-learning.html': 1753,
   '/tensorflow-tutorial_3.html': 8018,
}

# GOOGLE_ADSENSE = {
#     'ca_id': 'ca-pub-5639899546876072',
#     'page_level_ads': True,
#     'ads': {
#         'aside': '',
#         'main_menu': '',
#         'index_top': '',
#         'index_bottom': '',
#         'article_top': '5718861428',
#         'article_bottom': '',
#     },
# }

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
