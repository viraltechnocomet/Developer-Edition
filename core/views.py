from http.client import HTTPResponse
from django.views.generic import (
    TemplateView,
    DetailView,
    View,
    ListView,
    DetailView,
)

from django.http import (
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import (
    render,redirect
)

from core.forms import CreateUserCustomForm, AddManagerForm
from accounts.models import CustomUser
from django.conf import settings
from core.forms import AddManagerForm


class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        ...
        
def AddManager(request):
    context={}
    context['form'] = AddManagerForm
    return render(request,'core/add-manager.html',context)

# def AddManager(request, args, *kwargs):
# 	if not request.user.is_authenticated:
# 		return redirect("login")
# 	user_id = kwargs.get("user_id")
# 	account = CustomUser.objects.get(pk=user_id)
# 	if account.pk != request.user.pk:
# 		return HTTPResponse("You cannot edit someone elses profile.")
# 	context = {}
# 	if request.POST:
# 		form = AddManagerForm(request.POST, request.FILES, instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			return redirect("core:view", user_id=account.pk)
# 		else:
# 			form = AddManagerForm(request.POST, instance=request.user,
# 				initial={
# 					"id": account.pk,
# 					"email": account.email, 
# 					"username": account.username,
# 					"profile_image": account.profile_image,
# 				}
# 			)
# 			context['form'] = form
# 	else:
# 		form = AddManagerForm(
# 			initial={
# 					"id": account.pk,
# 					"email": account.email, 
# 					"username": account.username,
# 					"profile_image": account.profile_image,
# 				}
# 			)
# 		context['form'] = form
# 	context['DATA_UPLOAD_MAX_MEMORY_SIZE'] = settings.DATA_UPLOAD_MAX_MEMORY_SIZE
# 	return render(request, "core/add-manager.html", context)