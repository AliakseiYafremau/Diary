"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app.views import sign_up, user_page, log_in, distributor, lesson_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log_in', log_in, name='log_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('user/<str:name>', user_page, name='user_page'),
    path('', distributor, name='distributor'),
    path('user/<str:name>/lessons/<str:lesson>', lesson_page, name='lesson_page'),
]
