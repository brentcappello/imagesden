from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from registration.signals import user_activated
from registration.models import RegistrationProfile

class MemberProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=100, blank=True)

    #    class Meta:
    #        permissions = (('view_content', 'Can see available content'),)

    def __unicode__(self):
        return self.name


@receiver(user_activated)
def create_member_profile(user, request, *args, **kwargs):
    MemberProfile.objects.create(user=user)

#User.profile = property(lambda u: MemberProfile.objects.get_or_create(user=u)[0])

