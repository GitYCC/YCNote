#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'YC Chen'
SITENAME = u'YC Note'
SITEURL = 'https://www.ycc.idv.tw'

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

PLUGIN_PATHS = ['plugins']

PLUGINS = ['sitemap', 'render_math', 'pelican_alias', 'related_posts']

## 配置sitemap 插件
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.3,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
ATH_JAX = {'align': 'center'}

DISQUS_SITENAME = 'ycnote-1'


DEFAULT_DATE_FORMAT = '%Y / %B %d'

RELATED_POSTS_MAX = 10

THEME = 'theme/typerite'
SITESUBTITLE = u'YC Note, 機器學習(Machine Learning)、深度學習(Deep Learning)、類神經網路(Neural Network)、資料科學(Date Science)、Python、演算法(Algorithm)'

# Static files
STATIC_PATHS = ['images','media','static', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'},
    'extra/CNAME': {'path': 'CNAME'},}


def prev_article(current, articles):
    articles = sorted(articles, key=lambda x: x.date)
    i = articles.index(current) - 1
    if i >= 0:
        return articles[i]
    else:
        return None


def next_article(current, articles):
    articles = sorted(articles, key=lambda x: x.date)
    i = articles.index(current) + 1
    if i < len(articles):
        return articles[i]
    else:
        return None


JINJA_FILTERS = {'prev_article': prev_article, 'next_article': next_article}
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
