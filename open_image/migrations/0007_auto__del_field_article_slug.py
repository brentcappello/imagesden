# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.slug'
        db.delete_column('open_image_article', 'slug')


    def backwards(self, orm):
        # Adding field 'Article.slug'
        db.add_column('open_image_article', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=1, max_length=50, unique=True),
                      keep_default=False)


    models = {
        'dynamic_scraper.schedulerruntime': {
            'Meta': {'ordering': "['next_action_time']", 'object_name': 'SchedulerRuntime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_action_factor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'next_action_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'num_zero_actions': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runtime_type': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'dynamic_scraper.scrapedobjclass': {
            'Meta': {'ordering': "['name']", 'object_name': 'ScrapedObjClass'},
            'checker_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 1440,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 1,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 5,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scraper_scheduler_conf': ('django.db.models.fields.TextField', [], {'default': '\'"MIN_TIME": 15,\\n"MAX_TIME": 10080,\\n"INITIAL_NEXT_ACTION_FACTOR": 10,\\n"ZERO_ACTIONS_FACTOR_CHANGE": 20,\\n"FACTOR_CHANGE_FACTOR": 1.3,\\n\''})
        },
        'dynamic_scraper.scraper': {
            'Meta': {'ordering': "['name', 'scraped_obj_class']", 'object_name': 'Scraper'},
            'checker_ref_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'checker_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'checker_x_path': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'checker_x_path_result': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_items_read': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_items_save': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pagination_append_str': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'pagination_on_start': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pagination_page_replace': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pagination_type': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'scraped_obj_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dynamic_scraper.ScrapedObjClass']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        },
        'open_image.article': {
            'Meta': {'object_name': 'Article'},
            'checker_runtime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 12, 0, 0)'}),
            'dens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['open_image.Den']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['open_image.NewsWebsite']"}),
            'search_term': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'open_image.den': {
            'Meta': {'object_name': 'Den'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 12, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'open_image.newswebsite': {
            'Meta': {'object_name': 'NewsWebsite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'scraper': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dynamic_scraper.Scraper']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'scraper_runtime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dynamic_scraper.SchedulerRuntime']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['open_image']