from django.views.generic import TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from member.models import MemberProfile
from member.forms import ProfileForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect



class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'member/index.html'

class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'member/profile.html'

    def member_view(self):
        self.member = self.request.user.get_profile()
        return self.member

#    def get_or_create_user_profile(request):
#        profile = None
#        user = request.user
#        try:
#            profile = user.get_profile()
#        except MemberProfile.DoesNotExist:
#            profile = MemberProfile.objects.create(user)
#        return profile

#    def member_view(self):
#        try:
#            self.member = self.request.user.get_profile()
#        except MemberProfile.DoesNotExist:
#            self.member = MemberProfile.objects.create(user)
#        return self.member

#    def newsletter_count(self):
#        self.newsletter_objects = Newsletter.objects.filter(created_by=self.request.user)
#        self.ncount = self.newsletter_objects.count()
#        return self.ncount

    def get_context_data(self, *args, **kwargs):
        context = super(AccountView, self).get_context_data(*args, **kwargs)
        context['profile'] = self.member_view()
#        context['newsletter_count'] = self.newsletter_count()
        return context

def passchange(request):
    change_password_form = PasswordChangeForm(data=request.POST or None, user=request.user)

    if change_password_form.is_valid():
        change_password_form.save()
        return HttpResponseRedirect('/dashboard/account/')

    return render(request, 'registration/password_change_form.html', {
        'form':change_password_form,
        })

def profileedit(request):
    instance_a = get_object_or_404(MemberProfile, user=request.user)
    instance_b = get_object_or_404(User, pk=request.user.id)

    a = ProfileForm(request.POST or None, instance=instance_a)
    b = UserForm(request.POST or None, instance=instance_b)

    if a.is_valid() and b.is_valid():
        a.save() and b.save()
        return HttpResponseRedirect('/dashboard/account/')


    return render(request, 'member/profile-edit.html', {
        'form': a,
        'forms': b,
        })