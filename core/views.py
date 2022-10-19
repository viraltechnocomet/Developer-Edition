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
    HttpResponse,
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


