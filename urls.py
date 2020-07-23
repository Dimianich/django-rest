"""api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views
from rest_auth.views import (LoginView, LogoutView, PasswordResetView, PasswordChangeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/login/', LoginView.as_view(), name='rest_login'),
    path('api/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/registration/',
         include('rest_auth.registration.urls')),

    #path('api/password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('api/password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('api/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #path('api/password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    #path('api/password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('api/password_reset/', PasswordResetView.as_view(), name='rest_password_reset'),

    path('api/password_change/', PasswordChangeView.as_view(), name='rest_password_change'),

]
