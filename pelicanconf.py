#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Monica Mow'
SITENAME = 'The Least Square'
SITEURL = 'https://monicamow.github.io'
SITESUBTITLE = 'Trying to automate my job away.'

PATH = 'content'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Friend\'s Blog', 'http://sampurkiss.github.io/'),
         ('Graphic Detail', 'https://www.economist.com/graphic-detail/'),
         ('FlowingData', 'https://flowingdata.com/'),
         ('Atlas', 'https://www.theatlas.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/mcm_xci'),
          ('GitHub', 'https://github.com/monicamow'),
          ('LinkedIn', 'https://www.linkedin.com/in/monicamow'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# add a theme
THEME = 'themes/aboutwilson'

PROFILE_IMAGE = "scatter-red-icon.png"
TWITTER_USERNAME = '@mcm_xci'

# add jupyter notebook to md
MARKUP = ('md', 'ipynb')
#IPYNB_SKIP_CSS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

RMD_READER_RENAME_PLOT='chunklabel'

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]
