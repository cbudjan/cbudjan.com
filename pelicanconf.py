#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christoph Budjan'
SITENAME = u'Christoph Budjan'
SITEURL = 'http://cbudjan.com'
MAIL_USERNAME = 'christoph'
MAIL_HOST = 'budjan.de'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'
THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#Article permalink structure
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 4
DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {'en': '%b %d, %Y'}
DEFAULT_DATE_FORMAT = '%b %d, %Y'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
NEWEST_FIRST_ARCHIVES = True
LOCALE = ""

# Navigation sections and relative URL:
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('Research', 'pages/research.html'),
        ('About', 'pages/contact.html')]

# Static paths will be copied under the same name
STATIC_PATHS = ["images"]
OUTPUT_PATH = '/output'

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),('extra/favicon.ico', 'favicon.ico'),('extra/google0f93d0d7967afd0f.html', 'google0f93d0d7967afd0f.html'))
# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# Social links
TWITTER_USERNAME = 'cbudjan'
LINKEDIN_URL = 'http://www.linkedin.com/pub/christoph-budjan/27/791/815'
GITHUB_URL = 'http://github.com/cbudjan'

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'disqus_static']

## Sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

## Disqus plugin
DISQUS_SITENAME = u'cbudjan'
DISQUS_SHORTNAME = u'cbudjan'
DISQUS_SECRET_KEY = u'tSKzDNXXr8qNFL6cuCYTtgayv7m7mqJET8SpuVVT4YAbMrMMdEkUXbbISNrRuz3W'
DISQUS_PUBLIC_KEY = u'yQwa287yZZ5uhQewBUD3TK0VEDU1YnAYIV9EWwYer0d5DcNZlpWlrkf4lP3QWQn2'
