"""
URL configuration for post_machine_admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import user.views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', user.views.root_page),
    path('admin/', admin.site.urls),
    path('user/', user.views.user_page),
    path('login/', user.views.LoginPage.as_view()),
    path('register/', user.views.RegisterPage.as_view()),
    path('logout/', user.views.logout_page),
    path('parcel/', include('parcel.urls')),
    path('post_machine/', include('post_machine.urls'))
]
