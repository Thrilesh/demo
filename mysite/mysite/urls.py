"""
URL configuration for mysite project.
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World! Django is working on Vercel! 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world, name='home'),
]