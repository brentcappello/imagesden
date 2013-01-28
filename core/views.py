#stdlib imports

#core django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, View
from django.template.defaultfilters import slugify
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
#from django.utils import simplejson

#third party app imports
from dynamic_scraper.utils.task_utils import TaskUtils
from braces.views import JSONResponseMixin

#imports from local apps
from open_image.models import NewsWebsite, Article, Den
from core.forms import SearchForm




def search_it(request, template_name='core/home.html'):
    search = '' #add in the slug maker
    form = SearchForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
        form.process()
        search = form.cleaned_data['title']
        den = form.save(commit=False)
        den.save()
        #Spider Tasks
        t = TaskUtils()
        t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider', search)

        slug = slugify(search)

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

def image_grid_list(request):
    image_dict = {}
    for image in Article.objects.all():
        get_objects = TemperatureData.objects.filter(Device=filter_device)
        current_object = get_objects.latest('Date')
        current_data = current_object.Data
        temperature_dict[image] = current_data
    return render_to_response('core/image_grid_list.html', {'image': image_dict})


def image_grid(request, slug):
    images = get_object_or_404(Den, slug=slug)
#    object_list = images.article_set.all()
    search_term = slug.replace('-', ' ');
    image_list = Article.objects.filter(search_term=search_term)

    #this may not be the optimal way. I would prefer to load the images by using a M2M relationship
    #object_list is the m2m relationship which I am currently not using.

    return render(request, 'core/image_grid.html', {
#        'object_list': object_list,
        'den': images,
        'image_list': image_list,
        })

class ImageObjectApiView(JSONResponseMixin, SingleObjectMixin, View):
    model = Article

    def get(self, request, *args, **kwargs):
        instance = [self.get_object()]
        return self.render_json_object_response(instance)

class ImageObjectApiListView(JSONResponseMixin, MultipleObjectMixin, View):
    model = Article

    def get(self, request, search_term, *args, **kwargs):
        term = Article.objects.filter(search_term=search_term)
        return self.render_json_object_response(term)