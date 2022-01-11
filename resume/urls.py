from django.urls import path
from resume import views
from django.template.loader import render_to_string

urlpatterns=[path('',views.index,name='index'),]