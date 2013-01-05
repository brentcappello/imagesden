#from django.forms import ModelForm
#from open_image.models import Article
#
#class SearchForm(ModelForm):
#    class Meta:
#        model = Article
#        fields = ('search_term',)




from django import forms

class SearchForm(forms.Form):
    search = forms.CharField()

#    def clean(self):
#        self.saved_data=self.cleaned_data
#        return self.cleaned_data

    def process(self):
        search = self.cleaned_data['search']
        return search