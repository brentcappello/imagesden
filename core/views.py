from django.views.generic import TemplateView, UpdateView, ListView, DetailView
from open_image.models import NewsWebsite

from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import SearchForm
from django.views.generic.edit import FormMixin

from dynamic_scraper.utils.task_utils import TaskUtils
from open_image.models import NewsWebsite, Article

#from scrapy.crawler import CrawlerProcess
#from scrapy.conf import settings

#from open_image.scraper.invoke import CrawlerWorker
#from multiprocessing.queues import Queue

#from scrapy.conf import settings
#from scrapy.crawler import CrawlerProcess
#from open_image.scraper.spiders import ArticleSpider

#class HomeView(ListView):
#    template_name = 'core/home.html'
#    form_class = SearchForm
#
#    def get_queryset(self):
##        self.newssite = NewsWebsite.objects.values_list()
#        self.newssite = NewsWebsite.objects.all()
#        for i in self.newssite:
#            self.url = i.url
#            self.name = i.name
#
#        if self.name == 'Pinterest' or 'Flickr':
#            self.url = self.url + '_cool_cats'
#            self.pig = self.url
#        else:
#            self.pig = 'broken'
#
#
#    def get_context_data(self, *args, **kwargs):
#        context = super(HomeView, self).get_context_data(*args, **kwargs)
#        context['site'] = self.pig
#        return context


def search_it(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            t = TaskUtils()
            t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider')
                # Process the data in form.cleaned_data
                # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = SearchForm() # An unbound form

    return render(request, 'core/home.html', {
        'form': form,
        })