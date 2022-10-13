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
    render
)

from core.forms import CreateUserCustomForm,Addmanagerform

class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        ...


def AddmanagerView(request):
    context={}
    context['form']=Addmanagerform()
    return render(request,'core/add-manager.html',context)