from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tasks.forms import TasksForm
from tasks.models import Tasks
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
        if request.user.is_authenticated:
            user = request.user
            form=TasksForm()
            tasks = Tasks.objects.filter(user = user)
            context={
                "form":form,
                "tasks":tasks
            }
            return render(request, 'index.html', context)

def login(request):
     if request.method == 'GET':
        form = AuthenticationForm()
        context={
            "form":form
        }
        return render(request, 'login.html', context)
     else:
          form = AuthenticationForm(data=request.POST)

          if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)
                if user is not None:
                    loginUser(request, user)
                    return redirect('home')
               
          else:
               context={
                    "form":form,
               }

               return render(request, 'login.html', context)

                       

               

           

          



def signup(request):

    if request.method =='GET':
            form = UserCreationForm()
            context={
                "form":form
            }
            return render(request, 'signup.html', context)
    else:
         form = UserCreationForm(request.POST)
         context ={
              "form":form
         }

         if form.is_valid():
              user = form.save()
              if user is not None:
                   return redirect('login')

         else:
              
              return render(request, 'signup.html', context)
              
@login_required(login_url='login')
def add_task(request):
    if request.user.is_authenticated:
        user = request.user
        form=TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user=user
            task.save()
            return redirect('home')
        else:
            return render(request, 'index.html', context={'form':form} )


def delete_task(request, id):
     Tasks.objects.get(pk = id).delete()
     return redirect('home')


def change_task(request, id, status):
        task= Tasks.objects.get(pk=id)
        task.status=status
        task.save()
        return redirect('home')


def signout(request):
     logout(request)
     return redirect('login')

