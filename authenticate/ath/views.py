from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Student
# Create your views here.
 
def home(request):
    return render(request, 'home.html',{})

def base(request):
    return render(request,'base.html',{})

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user = authenticate(request, username=username, password=password)

        if  user is None:
            messages.info(request, "Invalid credentials.")    
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
        
    return render(request,'login.html',{})


def logout_view(request):
    logout(request)
    return redirect('/login/')


def signup_view(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Check if required fields are not empty
        user=User.objects.filter(username=username)
        if user.exists():
           messages.info(request, "username is not available. Please try another one.")    
           return redirect('/signup/')


        if username and email and password:
            try:
                # Create a new user instance
                user = User.objects.create_user(username=username, email=email, password=password)
                # Redirect to the login page after successful user creation
                return redirect('login')  # Assuming 'login' is the name of the login URL pattern
            except Exception as e:
                return HttpResponse(f"An error occurred: {e}")
        else:
            messages.info(request, "please fill all the fields.")    
            return redirect('/signup/')  
    else:
        return render(request, 'signup.html')  # Render the signup form template




def student(request):
    if request.method=="POST":
         name=request.POST.get('name')
         #regno=request.POST.get('regno')
         email=request.POST.get('email')
         image=request.FILES.get('image')
         
         student=Student.objects.create(
             name=name,
             #regno=regno,
             contact=email,
             image=image,
          )
         student.save()
         
         messages.info(request, "Succefully applied")    
         return render(request,'student.html',{})
    else:
      return render(request, 'student.html')
    


def student_list(request):
    students = Student.objects.all()  # Retrieve all Student objects from the database
    return render(request, 'student_list.html', {'students': students})