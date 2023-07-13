from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views

admin.site.site_header = "Developer Martin Pereira"
admin.site.site_title = "Welcome to Dasboard"
admin.site.index_title = "Welcome to Portfolio"
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('web', views.web, name='web'),
]