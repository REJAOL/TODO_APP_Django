from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

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
              




    