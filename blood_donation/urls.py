from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('admin_dashboard/', include('admin_dashboard.urls')),
    path('blood/', include('blood.urls')),
    path('', views.base, name='home'),
]
