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
    render, redirect
)

from core.forms import *
from .forms import *
from django.views.generic import View
from django.contrib import messages
from templates import *
from accounts.models import CustomUser
from accounts.forms import SignUpForm
from .models import * 
from templates import *
from django.contrib import messages
from accounts.models import USER_TYPES
from . import forms



class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo": "value"}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        ...


class AddAdminView(TemplateView):
    def get(self,request):
        user = request.user
        init_data = {"type" : "ADMIN","created_by":user}
        form = SignUpForm(initial=init_data)
        
        context={
            'form': form
        }
        return render(request, "core/add-admin.html",context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            return redirect('core:add-admin')
        else:
            messages.error(request, form.errors)

        context={
            'form': form
        }
        return render(request, "core/add-admin.html",context)

class AddManagerView(TemplateView):
    def get(self,request):
        user = request.user
        init_data = {"type" : "MANAGER","created_by":user}
        form = SignUpForm(initial=init_data)
        context={
            'form': form
        }
        return render(request, "core/add-manager.html", context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            return redirect('core:add-manager')
        else:
            messages.error(request, form.errors)

        context={
            'form': form
        }
        return render(request, "core/add-manager.html",context)


class AddAgentView(TemplateView):
    def get(self,request):
        user = request.user
        init_data = {"type" : "AGENT","created_by":user}
        form = SignUpForm(initial=init_data)
        context={
            'form': form
        }
        return render(request, "core/add-agent.html", context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            return redirect('core:add-agent')
        else:
            messages.error(request, form.errors)

        context={
            'form': form
        }
        return render(request, "core/add-agent.html",context)

class ShowDataView(TemplateView):

    def get(self, request):
        
        showlist = CustomUser.objects.all()
        context = {
            'userdata': showlist
        }
        return render(request, "core/list-all-agent.html", context)



def AddCategory(request):
    categoryForm=forms.CategoryForm() 
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('core:add-category')
    return render(request,'core/add-category.html',{'categoryForm':categoryForm})


def AddPolicy(request):
    policyForm=forms.PolicyForm() 
    
    if request.method=='POST':
        policyForm=forms.PolicyForm(request.POST)
        if policyForm.is_valid():
            categoryid = request.POST.get('category')
            category = Category.objects.get(id=categoryid)

            policy = policyForm.save(commit=False)
            policy.category=category
            policy.save()
            return redirect('core:add-agent')
    return render(request,'core/add-policy.html',{'policyForm':policyForm})
