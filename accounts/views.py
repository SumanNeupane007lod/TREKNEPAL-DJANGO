from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print("enter inside post")
        if user is None:
            messages.info(request,'wrong username or password')
            print("wrong user name")
            return redirect('login')
        else:
            
            auth.login(request,user)
            print('user entered')
            user=User.objects.get(username=username)
            
            return redirect('/')
            return render(request,'user_profile.html',{'user':user})
            #return render(request,'index.html',{'user':user})
    else:
        return render (request,'login.html')

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print('user created')
                return redirect('/')
    
        else:
            messages.info(request,'password invalid')
            return redirect('register')

    else:
        return render(request, 'register.html')

def logout(request):
    user=None
    return redirect('/')

def user_profile(request):
    pass