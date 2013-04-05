#THIS IS NOT CURRENTLY IN USE - PULLED FROM NEWSDUB

from django.forms import ModelForm
from django.contrib.auth.models import User
from member.models import MemberProfile
from django import forms
from registration.forms import RegistrationForm

#MEMBERSHIP_CHOICES = (('Free', 'Free'),('Paid', 'Paid'))

class UserRegistrationForm(RegistrationForm):
    website = forms.CharField(label='Website')
    phone = forms.CharField(label='Phone Number')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
#    membership = forms.ChoiceField(widget=forms.RadioSelect, choices=MEMBERSHIP_CHOICES)

#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/ I think inline formsets may resolve this.

class ProfileForm(ModelForm):
    class Meta:
        model = MemberProfile
        exclude = ('user', 'name',)

class UserForm(ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

