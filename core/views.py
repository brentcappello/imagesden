from open_image.models import NewsWebsite, Article, Den
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from core.forms import SearchForm
from dynamic_scraper.utils.task_utils import TaskUtils
from django.views.generic import CreateView, ListView
from django.template.defaultfilters import slugify


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




#def search_it(request):
#    search = '' #add in the slug maker
#    if request.method == 'POST': # If the form has been submitted...
#        form = SearchForm(request.POST) # A form bound to the POST data
#        if form.is_valid(): # All validation rules pass
#            form.process()
#            search = form.cleaned_data['search']
##            request.session['my_search'] = search
##            searched = request.session['my_search']
#
#
#
#            #Spider Tasks
#            t = TaskUtils()
#            t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider', search)
#
#            return HttpResponseRedirect('den/' + search) # Redirect after POST
#    else:
#        form = SearchForm() # An unbound form
#
#    return render(request, 'core/home.html', {
#        'form': form,
#        'search': search,
#        })


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


#class ImageListView(ListView):
#    template_name = 'core/post_list.html'
#
#    def get_queryset(self):
#        self.authorpost = Post.objects.filter(author=self.request.user)
#        return self.authorpost
#
#    def get_context_data(self, *args, **kwargs):
#        context = super(PostListView, self).get_context_data(*args, **kwargs)
#        context['post_list'] = self.authorpost
#        return context