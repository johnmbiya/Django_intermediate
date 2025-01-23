"""
URL configuration for leblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True
        ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='login',
    ), name='logout'),

    path('password_change', PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
    ), name='password_change'),

    path('password_change/done', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html',
    ), name='password_change_done'),

    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload/', authentication.views.upload_profile_photo, name='upload_profile_photo'),

    path('home/', blog.views.home, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
    path('photo/upload-multiple/', blog.views.create_multiple_photos, name='photo_upload_multiple'),
    path('blog/create/', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>/', blog.views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit/', blog.views.edit_blog, name='edit_blog'),

    path('follow-users/', blog.views.follow_users, name='follow_users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)