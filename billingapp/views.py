from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate,login
# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'billing/index.html')

@login_required
def view_profile(request):
    return redirect('profile')

@login_required
def profile(request):
    try:
       
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
       
        return render(request, 'billing/profile.html', {
            'error': 'No profile exists for the current user. Please create one.'
        })

    return render(request, 'billing/profile.html', {
        'profile': profile
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
                        # Create and populate the Profile instance
            Profile.objects.create(
                user=user,
                business_title=form.cleaned_data.get('business_title'),
                business_address=form.cleaned_data.get('business_address'),
                business_email=form.cleaned_data.get('business_email'),
                business_phone=form.cleaned_data.get('business_phone'),
                business_gst=form.cleaned_data.get('business_gst'),
            )

            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'billing/registration.html',{
            'form':form
        })
    
def create_bill(request):
    if request.method=='POST':
        form1=BillingForm(request.POST)
        form2=CustomerForm(request.POST)
        
        if form1.is_valid() and form2.is_valid():
            new_id=form1.cleaned_data['bill_id']
            new_date=form1.cleaned_data['bill_date']

            new_customername=form2.cleaned_data['customer_name']
            new_custaddress=form2.cleaned_data['customer_address']
            new_custmobno=form2.cleaned_data['customer_mobileno']
            new_custgst =form2.cleaned_data['customer_gst']

            new_bill=Billing(
                bill_id=new_id,
                bill_date=new_date,
                user=request.user
            )

            new_customer=Customer(
                customer_name=new_customername,
                customer_address=new_custaddress,
                customer_mobileno=new_custmobno,
                customer_gst=new_custgst,
                user=request.user
            )

            new_bill.save()
            new_customer.save()

            return render(request,'billing/create_bill.html',{
            'form1':BillingForm(),
            'form2':CustomerForm(),
            'success':True
        })
    
    else:
        form1=BillingForm()
        billing = Billing.objects.filter(user=request.user)
        form2=CustomerForm()
        customer = Customer.objects.filter(user=request.user)
        
    return render(request,'billing/create_bill.html',{
            'form1':form1,
            'billing':billing,
            'form2':form2,
            'customer':customer,
        })
    
@login_required
def allbill(request):
    allbill=Billing.objects.filter(user=request.user)
    return render(request,'billing/allbills.html',{
        'allbill':allbill
    })