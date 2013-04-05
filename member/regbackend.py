#THIS IS NOT CURRENTLY IN USE - PULLED FROM NEWSDUB

from member.models import MemberProfile
from member.forms import UserRegistrationForm
#from django.contrib.auth.models import Group, Permission

#Adds form data to both the User model via usrdata and to the MemberProfile model via data
def user_created(sender, user, request, **kwargs):
    form = UserRegistrationForm(request.POST)
    data = MemberProfile(user=user)
    usrdata = user
    data.website = form.data["website"]
    data.phone = form.data['phone']
    usrdata.first_name = form.data['first_name']
    usrdata.last_name = form.data['last_name']
    data.save()
    usrdata.save()

    #This decides if the user is paid or free from forms.py
#    mlevel = form.data['membership']
#    if mlevel == 'Paid':
#        g = Group.objects.get(name='paid member')
#    else:
#        g = Group.objects.get(name='free member')
#    usrdata.groups.add(g)


from registration.signals import user_registered
user_registered.connect(user_created)
