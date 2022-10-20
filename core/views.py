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

from core.forms import CreateUserCustomForm, AddManagerForm
from .forms import AddManagerForm
from django.views.generic import View
from django.contrib import messages
from templates import *
from accounts.models import CustomUser



class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo": "value"}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        ...


# def AddManager(request):
#     context={}
#     context['form'] = AddManagerForm
#     return render(request,'core/add-manager.html',context)


class AddManagerView(View):
    def get(self,request):
        form = AddManagerForm(request.POST or None)
        return render(request, "core/add-manager.html", {"form": form })

    def post(self, request):
        msg     = None
        success = False

        if request.method == "POST":
            form = AddManagerForm(request.POST)

            if form.is_valid():
                form.save()
                # group = Group.objects.get(name='client')
                fname = form.cleaned_data.get("first_name")
                lname = form.cleaned_data.get("last_name")
                uname = form.cleaned_data.get("username")
                em = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password")
                # user = authenticate(username=username, password=raw_password)
                # user.groups.add(group)

                msg     = messages.add_message(request, messages.SUCCESS,'User created Successfully, Please Login!')
                success = True
                
                return redirect("/core/add-manager/")

            else:
                msg = ('Form is not valid',)
                form.add_error(None,'Form is not valid')
        else:
            form = AddManagerForm()

        return render(request, "core/add-manager.html", {"form": form, "msg" : msg, "success" : success })


# def AddManager(request):
#     userForm=forms.AddManagerForm()

#     if request.method=='POST':
#         userForm=forms.AddManagerForm(request.POST)
        
#         if userForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
           
#             my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
#             my_customer_group[0].user_set.add(user)
#         return HttpResponseRedirect('add-manager')
#     return render(request,'core/add-manager.html',)

