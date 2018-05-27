#!/usr/bin/env python
import markdown

AUTHOR = 'charlesreid1'
SITENAME = 'Git Subway Maps'
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

PATH = 'content'
OUTPUT_PATH = 'output'

# --------------8<---------------------
# Theme

THEME = 'simple-bootstrap'

# --------------8<---------------------
# Files and content

# Don't try to turn HTML files into pages
READERS = {'html': None}

# This will look for a directory img/ 
# inside the directory content/
# The contents of img/ will be available at 
# {{ SITEURL }}/img
STATIC_PATHS = ['img','css','vendor']


# --------------8<---------------------
# apps

EXTRA_TEMPLATES_PATHS = []
TEMPLATE_PAGES = {}
TEMPLATE_PAGES['index.html'] = 'index.html'

EXTRA_TEMPLATES_PATHS.append('subway')
TEMPLATE_PAGES['one_branch.html']     = 'one_branch.html'
TEMPLATE_PAGES['two_branches.html']   = 'two_branches.html'

TEMPLATE_PAGES['subway.css']          = 'subway.css'
TEMPLATE_PAGES['one_branch.css']      = 'one_branch.css'
TEMPLATE_PAGES['two_branches.css']    = 'two_branches.css'

TEMPLATE_PAGES['jquery-1.9.0.min.js'] = 'jquery-1.9.0.min.js'
TEMPLATE_PAGES['jquery.subwayMap-0.5.0.js'] = 'jquery.subwayMap-0.5.0.js'


# --------------8<---------------------
# idk just some dumb stuff

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

