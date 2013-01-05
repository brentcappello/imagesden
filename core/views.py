from open_image.models import NewsWebsite
from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import SearchForm
from dynamic_scraper.utils.task_utils import TaskUtils


def search_it(request):
    search = '' #add in the slug maker
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.process()
            search = form.cleaned_data['search']

            request.session['my_search'] = search
            searched = request.session['my_search']
            t = TaskUtils()
            t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider', searched)

            return HttpResponseRedirect(search) # Redirect after POST
    else:
        form = SearchForm() # An unbound form

    return render(request, 'core/home.html', {
        'form': form,
        'search': search,
        })