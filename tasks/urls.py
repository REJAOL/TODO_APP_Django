
from django.contrib import admin
from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('add-task', add_task),
    path('delete-task/<int:id>', delete_task),
    path('change-status/<int:id>/<str:status>', change_task),
    path('logout', signout),
]
