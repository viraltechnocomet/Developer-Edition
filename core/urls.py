from django.contrib import admin
from django.urls import path,reverse_lazy,include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from core.views import *
urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    # path('', views.DashboardView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    # path('cropImage', crop_image, name='crop_image'),
    path('add-admin/', views.AddAdminView.as_view(),name='add-admin'),
    path('add-manager/', views.AddManagerView.as_view(),name='add-manager'),
    path('add-agent/', views.AddAgentView.as_view(),name='add-agent'),
    path('all-user-list/', views.ShowDataView.as_view(),name='all-user-list'),
    path('add-category/', views.AddCategory,name='add-category'),
    path('add-policy/', views.AddPolicy,name='add-policy'),
    path('add-policy-view/', views.AddPolicyView,name='add-policy-view'),
    path('user-update/<int:id>', views.UserUpdateView,name='user-update'),
    path('user-delete/<int:id>', views.UserDeleteView,name='user-delete'),
    
    # path('cropimage/', crop_image,name='cropimage'),
    
]
