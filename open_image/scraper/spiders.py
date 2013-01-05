from dynamic_scraper.spiders.django_spider import DjangoSpider
from open_image.models import NewsWebsite, Article, ArticleItem

from django.contrib.sessions.backends.db import Session
from django.contrib.sessions.backends.db import SessionStore


class ArticleSpider(DjangoSpider):
    
    name = 'article_spider'

    def __init__(self, term, *args, **kwargs):

        self.search_terms = term
        self._set_ref_object(NewsWebsite, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url + self.search_terms
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = Article
        self.scraped_obj_item_class = ArticleItem
        super(ArticleSpider, self).__init__(self, *args, **kwargs)
