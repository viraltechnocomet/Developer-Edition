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

from .forms import *
from django.views.generic import View
from django.contrib import messages
from templates import *
from accounts.models import CustomUser
from accounts.forms import SignUpForm, UpdateForm
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
            return redirect('core:all-user-list')
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
            return redirect('core:all-user-list')
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
            return redirect('core:all-user-list')
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
        return render(request, "core/all-user-list.html", context)



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

            usernameid = request.POST.get('email')
            username = CustomUser.objects.get(id=usernameid)
            print(usernameid)
            policy = policyForm.save(commit=False)
            policy.category=category
            policy.username=username
            policy.save()
            return redirect('core:add-policy-view')
    return render(request,'core/add-policy.html',{'policyForm':policyForm})


def AddPolicyView(request):
    policies = Policy.objects.all()
    return render(request,'core/add-policy-view.html',{'policies':policies})



def UserUpdateView(request, id):
    context = {}

    if request.method == "POST":
        print("hello...")
        emp = CustomUser.objects.get(id = id)
        form = UpdateForm(request.POST, instance=emp)
        if form.is_valid():
            print("done...")
            form.save()
            return redirect('core:all-user-list')
        context['emp'] = emp
        context['form'] = form
    else:
        emp = CustomUser.objects.get(id=id)
        form = UpdateForm(instance=emp)
        context['emp']=emp
        context['form']=form
    return render(request, 'core/user-update.html', context)

def UserDeleteView(request,id):
    emp = CustomUser.objects.get(id = id)
    emp.delete()
    return redirect('core:all-user-list')