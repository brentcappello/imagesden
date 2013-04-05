from django.contrib import admin
from registration.admin import RegistrationAdmin
from registration.models import RegistrationProfile
from django.contrib.auth.models import User
from member.models import MemberProfile
from django.utils.translation import ugettext_lazy as _


admin.site.unregister(User)

class MemberProfileInline(admin.StackedInline):
    model = MemberProfile

class MemberAdmin(admin.ModelAdmin):
    inlines = [MemberProfileInline]


admin.site.register(User, MemberAdmin)



#class MemberAdmin(admin.ModelAdmin):
#    pass
#
#admin.site.register(MemberProfile, MemberAdmin)










