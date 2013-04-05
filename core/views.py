#stdlib imports

#core django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, View, DetailView
from django.template.defaultfilters import slugify
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.core.exceptions import ObjectDoesNotExist
#from django.utils import simplejson

#third party app imports
from dynamic_scraper.utils.task_utils import TaskUtils
from braces.views import JSONResponseMixin
from easy_thumbnails.files import get_thumbnailer

#imports from local apps
from open_image.models import NewsWebsite, Article, Den, UserDen
from core.forms import SearchForm, UserDenForm


def search_it(request, template_name='core/home.html'):
    search = '' #add in the slug maker
    form = SearchForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
        form.process()
        search = form.cleaned_data['title']
        slug = slugify(search)
        try:
            e = Den.objects.get(slug=slug)
        except ObjectDoesNotExist:
            den = form.save(commit=False)
            den.save()

            #Spider Tasks
            t = TaskUtils()
            t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider', search)

        return redirect('den/' + slug)
    return render(request, template_name, {'form': form,})


#def get_latest_image(request, search_term):
#    # Query comments since the past X seconds
##    image_since = datetime.datetime.now() - datetime.timedelta(seconds=seconds_old)
#    image = Article.objects.filter(search_term=search_term)
#    images = list(image)
#
#    # Return serialized data or whatever you're doing with it
#    return HttpResponse(simplejson.dumps(images),mimetype='application/json')


def image_grid(request, slug):
    images = get_object_or_404(Den, slug=slug)
#    object_list = images.article_set.all()
    search_term = slug.replace('-', ' ');
    image_list = Article.objects.filter(search_term=search_term)
#    for item in image_list:
#        thumb_url = get_thumbnailer(item.thumbnail)['avatar'].url
#        thumb_url.save()

    #this may not be the optimal way. I would prefer to load the images by using a M2M relationship
    #object_list is the m2m relationship which I am currently not using.

    return render(request, 'core/image_grid.html', {
#        'object_list': object_list,
        'den': images,
        'image_list': image_list,
#        'thumb': thumb_url,
        })

class ImageObjectApiView(JSONResponseMixin, SingleObjectMixin, View):
    model = Article

    def get(self, request, *args, **kwargs):
        instance = [self.get_object()]
        return self.render_json_object_response(instance)


class ImageObjectApiListView(JSONResponseMixin, MultipleObjectMixin, View):
    model = Article
    image = {}

    def get(self, request, slug, *args, **kwargs):
        search_term = slug.replace('-', ' ');
        term = Article.objects.filter(search_term=search_term)
        for item in term:
            image = item.thumbnail
            thumbnailer = get_thumbnailer(image)
            thumbnail_options = {'crop': True, 'size': (202,158)}
            thumbnailer.get_thumbnail(thumbnail_options)
        return self.render_json_object_response(term)

class UserDenCreateView(CreateView):
    form_class = UserDenForm
    template_name = 'userden_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        obj.save()

        return HttpResponseRedirect('/')

#this is a list of all the users custom dens
class MyDenListView(ListView):
    template_name = 'core/mydens_list.html'

    def get_queryset(self):
        self.mydens = UserDen.objects.filter(created_by=self.request.user)
        return self.mydens

    def get_context_data(self, *args, **kwargs):
        context = super(MyDenListView, self).get_context_data(*args, **kwargs)
        context['mydens'] = self.mydens
        return context

class UserDenListView(ListView):
    template_name = 'core/userimage_grid.html'

    def get_queryset(self):
        self.created_byarticle = UserDen.objects.filter(created_by=self.request.user)
        return self.created_byarticle

    def get_context_data(self, *args, **kwargs):
        context = super(UserDenListView, self).get_context_data(*args, **kwargs)
        context['image_list'] = self.created_byarticle
        return context



#def userimage_grid(request, slug):
#    images = get_object_or_404(UserDen, slug=slug)
#    #    object_list = images.article_set.all()
#    search_term = slug.replace('-', ' ');
#    image_list = Article.objects.filter(search_term=search_term)
#    #    for item in image_list:
#    #        thumb_url = get_thumbnailer(item.thumbnail)['avatar'].url
#    #        thumb_url.save()
#
#    #this may not be the optimal way. I would prefer to load the images by using a M2M relationship
#    #object_list is the m2m relationship which I am currently not using.
#
#    return render(request, 'core/userimage_grid.html', {
#        #        'object_list': object_list,
#        'den': images,
#        'image_list': image_list,
#        #        'thumb': thumb_url,
#    })


