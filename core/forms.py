from django.forms import ModelForm
from open_image.models import Den

class SearchForm(ModelForm):
    class Meta:
        model = Den
        fields = ('title',)

    def process(self):
         search = self.cleaned_data['title']
         return search

from django import forms

#class SearchForm(forms.Form):
#    search = forms.CharField()
#
#    def process(self):
#        search = self.cleaned_data['search']
#        return search