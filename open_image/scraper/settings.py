# Scrapy settings for open_news project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

import sys
import os.path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path = sys.path + [os.path.join(PROJECT_ROOT, '../../..'), os.path.join(PROJECT_ROOT, '../..')]

from django.core.management import setup_environ
import imagesden.settings
setup_environ(imagesden.settings)


BOT_NAME = 'newsfinder'
BOT_VERSION = '1.0'

CONCURRENT_REQUESTS = 200
SPIDER_MODULES = ['dynamic_scraper.spiders', 'open_image.scraper',]
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.DjangoImagesPipeline',
    'dynamic_scraper.pipelines.ValidationPipeline',
    'open_image.scraper.pipelines.DjangoWriterPipeline',
]

#before this was just ../thumbnails
IMAGES_STORE = os.path.join(PROJECT_ROOT, '../../imagesden/media')

#IMAGES_THUMBS = {
#    'small': (170, 170),
#}

DSCRAPER_LOG_ENABLED = True
DSCRAPER_LOG_LEVEL = 'INFO'
DSCRAPER_LOG_LIMIT = 5