from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard_view, name='admin_dashboard'),
    path('blood-requests/', views.admin_blood_request_list, name='admin_blood_request_list'),
    path('blood-requests/<int:id>/', views.admin_blood_request_detail, name='admin_blood_request_detail'),
    path('blood-requests/<int:id>/delete/', views.admin_delete_blood_request, name='admin_delete_blood_request'),
    path('users/', views.admin_user_list, name='admin_user_list'),
    path('users/<int:id>/edit/', views.admin_edit_user, name='admin_edit_user'),
    path('users/<int:id>/delete/', views.admin_delete_user, name='admin_delete_user'),
]
