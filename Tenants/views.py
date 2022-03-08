import razorpay
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from .forms import tenantform
from .models import User, Tenants, Visitor, Complaints

# Create your views here.
from django.conf import settings

# Sigin-Up function
def signup(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            if User.objects.filter(Email=request.POST.get('email')):
                messages.info(request, 'User already exist for this EmailId')
                return render(request, 'SignUp.html')
            else:
                model = User()
                model1 = Tenants()
                model.Email = request.POST.get('email')
                model.Password = request.POST.get('password')
                model1.Email = request.POST.get('email')
                model.save()
                model1.save()
                return redirect('login')
    else:
        return render(request, 'SignUp.html')

# Sign-In function
def login(request):
    if request.method == 'POST':
        if User.objects.filter(Email=request.POST.get("email"), Password=request.POST.get("password")).exists():
            if request.POST.get("email") == 'Admin@gmail.com':
                return redirect('admin1')
            else:
                print("exist")
                a = request.POST.get("email")
                print(a)
                return redirect(f'tenant/{a}')
        else:
            messages.info(request, 'The Email and Password does not match')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')


# Function for displaying tenant detail page
def tenant(request, mail):
    print(f'This is my Id:{mail}')
    if Tenants.objects.filter(Email=mail):
        print('tenant exist')
        tenant = Tenants.objects.get(Email=mail)
    if request.method == 'POST':
        form = tenantform(request.POST, instance=tenant)
        if form.is_valid():
            tenant.save()
            messages.success(request, 'Details has been updated.')
            return render(request, 'Detail.html', {'form': form})
    else:
        form = tenantform(instance=tenant)
        return render(request, 'Detail.html', {'form': form})


def home(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('mobile') and request.POST.get(
                'date'):
            model = Visitor()
            model.Name = request.POST.get('name')
            model.Email = request.POST.get('email')
            model.Mobile = request.POST.get('mobile')
            model.Date_Visit = request.POST.get('date')
            model.save()
            messages.success(request, 'Request has been sent.')
    return render(request, 'Home1.html')


def admin1(request):
    tenant = Tenants.objects.all()
    return render(request, 'Admin.html', {'tenant': tenant})


def rentpay(request, email):
    tenant = Tenants.objects.get(Email=email)
    print(tenant.Rental_amount)
    rent = tenant.Rental_amount
    if request.method == "POST":
        amount = request.POST.get('price')
        client = razorpay.Client(
            auth=("rzp_test_KadYnmNZAFuKEg", "9mcPg3kEtzfcfALA5OTsiedi"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'Transaction.html', {'rent': rent})


@csrf_exempt
def success(request):
    return render(request, "Success.html")


def complaint(request, mail):
    print('hello')
    print(mail)
    tenant = Tenants.objects.get(Email=mail)
    if request.method == 'POST':
        model = Complaints()
        if request.POST.get('message'):
            model.Name = tenant.Name
            model.Email = tenant.Email
            model.Mobile = tenant.Mobile
            model.Text = request.POST.get('message')
            model.save()
            messages.success(request, 'Complaint has been registered.We will look into it')
    return render(request, 'Complaint.html', {'tenant': tenant})


def adminmsg(request):
    complaint = Complaints.objects.all()
    return render(request, 'AdminMsg.html', {'complaint': complaint})


def delete(request, id):
    complaint = Complaints.objects.get(id=id)
    complaint.delete()
    messages.success(request,   'Complaint is deleted')
    return redirect('admin_complaint')


def sendmail(request, email):
    send_mail('The Roof Top_Complaint Status', 'The complaint had been assigned', settings.EMAIL_HOST_USER, [email])
    messages.success(request, f'Email has been sent to {email}')
    return redirect('admin_complaint')


def visitor(request):
    visitor = Visitor.objects.all()
    return render(request, 'Admin_Visitor.html', {'visitor': visitor})


def sendmail_visitor(request, email):
    visitor = Visitor.objects.get(Email=email)
    send_mail('The Roof Top_Visit', f'Your visit to our place has been planned on {visitor.Date_Visit}', settings.EMAIL_HOST_USER, [email])
    messages.success(request, f'Email has been sent to {email}')
    return redirect('admin_visitor')

def delete_visitor(request,id):
    visitor = Visitor.objects.get(id=id)
    name = visitor.Name
    visitor.delete()
    messages.success(request, f'Visitor details of {name} is deleted')
    return redirect('admin_visitor')