
from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('add-task', add_task)
]
