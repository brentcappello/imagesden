from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from scrapy.contrib.djangoitem import DjangoItem
from dynamic_scraper.models import Scraper, SchedulerRuntime
from django.template.defaultfilters import slugify
from datetime import datetime
from django.contrib.auth.models import User


class NewsWebsite(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Den(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(default=datetime.now())

    def save(self):
        self.slug = slugify(self.title)
        super(Den, self).save()

    def __unicode__(self):
        return self.title

class UserDen(models.Model):
    created_by = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(default=datetime.now())

#    def save(self):
#        self.slug = slugify(self.title)
#        super(UserDen, self).save()

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    news_website = models.ForeignKey(NewsWebsite)
    description = models.TextField(blank=True)
    url = models.URLField()
    thumbnail = models.CharField(max_length=200)
    search_term = models.CharField(max_length=200)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)
    dens = models.ManyToManyField(Den, blank=True, null=True)
    userdens = models.ManyToManyField(UserDen, blank=True, null=True)
    created = models.DateTimeField(default=datetime.now())
#    slug = models.SlugField(unique=True)
#
#    def save(self):
#        self.slug = slugify(self.thumbnail)
#        super(Article, self).save()

    def __unicode__(self):
        return self.title

class ArticleItem(DjangoItem):
    django_model = Article


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, NewsWebsite):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()

    if isinstance(instance, Article):
        if instance.checker_runtime:
            instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)