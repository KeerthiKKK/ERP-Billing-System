from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
    return render(request,'billing/index.html')

def view_profile(request,id):
    profile=Profile.objects.get(pk=id)
    return HttpResponseRedirect(reverse('profile'))

def profile(request):
    return render(request,'billing/profile.html',{
        'profile':Profile.objects.all()
    })

def edit(request,id):
    if request.method=='POST':
        profile=Profile.objects.get(pk=id)
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return render(request,'billing/edit.html',{
                'form':form,
                'success':True
            })
    else:
        profile = Profile.objects.get(pk=id)
        form=ProfileForm(instance=profile)
    return render(request,"billing/edit.html",{
        'form':form
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                print(f"Authenticated user: {user.username}")
                login(request, user)
                return redirect('index')  # Redirect to index page
            else:
                print("Invlaid cred")

    else:
        form = LoginForm()

    # Render login page
    return render(request, 'billing/login.html', {'form': form})


def register_view(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'billing/registration.html',{
            'form':form
        })
    