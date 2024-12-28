from django.shortcuts import redirect, render
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
import csv

import smtplib
from email.mime.text import MIMEText
from django.conf import settings

def index(request):
    return render(request,"index.html")

def connect(request):
    return render(request,"connect.html")

def my_redirect(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc43kwkIP_TuK6PMbtQZi2PAw9YdzjjroM_0gM0C6F6WMOtrw/viewform?usp=dialog")

def signin(request):
    return render(request,"signin.html")

def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")

def project(request):
    return render(request,"project.html")

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'username already exists! Try with another username')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email already exists! Try with another email')
                return redirect('register')
            else:
                myuser = User.objects.create_user(username=username, password=pass1, email=email)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                # Email sending code
                try:
                    # Email configuration
                    sender_email = settings.EMAIL_HOST_USER
                    sender_password = settings.EMAIL_HOST_PASSWORD
                    
                    # Create email message
                    subject = "Registration Successful!"
                    body = f"""Hello {fname}!
                    
                    Welcome to our platform. Your registration was successful.
                    
                    Username: {username}
                    Email: {email}
                    
                    Thanks for joining us!
                    """
                    
                    msg = MIMEText(body)
                    msg['From'] = sender_email
                    msg['To'] = email
                    msg['Subject'] = subject

                    # Send email
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(msg)
                    server.quit()

                except Exception as e:
                    print(f"Email sending failed: {str(e)}")

                messages.success(request, "Your account has been registered successfully! Please login to continue.")
                return redirect('login')

        else:
            messages.success(request,'Password not matching :(')
            return redirect('register')
    else:
        return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['pass1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


#Donate pages
def donate1(request):
    return render(request,"donate1.html")

def donate2(request):
    return render(request,"donate2.html")

def donate3(request):
    return render(request,"donate3.html")

def show_user_count(request):
    # Get the total number of registered users
    user_count = User.objects.count()
    return render(request, 'show_user_count.html', {'user_count': user_count})

def show_registered_users(request):
    # Fetch all users
    users = User.objects.all()
    return render(request, 'show_registered_users.html', {'users': users})

