from django.contrib import admin
from django.urls import path,reverse_lazy,include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from core.views import crop_image

from core.views import (
    crop_image
)

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    # path('', views.DashboardView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    path('cropImage', crop_image, name='crop_image'),
    path('add-manager/', views.AddManager,name='add-manager'),
    path('cropimage/', crop_image,name='cropimage'),
    
]
