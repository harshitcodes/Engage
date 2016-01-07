from django.shortcuts import render,redirect
from .forms import SignUp,LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request,'base.html')


def signup(request):
    if request.user.is_authenticated():
        return render(request,'account/home.html',)
    form = SignUp(request.POST)
    if form.is_valid():
        user=form.save();
        message = "The User is registered,Refill The form for registering more users like"
        context = {'Message':message,'form':form,"user":user}
        return render(request,'account/Signup.html',context)
    else:
        context = {'form':form}
        return render(request,'account/SignUp.html',context)

require_GET
def login(request):
    if request.user.is_authenticated():
        user = request.user
        context = {"user":user}
        print("yo")
        return render(request,'account/home.html',context)
    else:
        form = LoginForm()
        context = {'form':form}
        print("wo")
        return render(request,'account/login.html',context)

require_POST
def handlelogin(request):
    if request.user.is_authenticated():
        user = request.user
        context = {"user":user}
        print("Authenticated user")
        return render(request,'account/home.html',context)

    form = LoginForm(request.POST)
    if form.is_valid():
        user = form.get_user()
        print("In form is valid")
        auth_login(request,user)
        context = {"user":user}
        return render(request,'account/home.html',context)
    if not form.is_valid():
        form = LoginForm()
        Message = "Error in form"
        context = {'form':form}
        print("IN FORM ISNOT VALID")
        return render(request,'account/login.html',context)
    # newform = LoginForm()
    # context = {"form":newform}
    # return render(request,'account/login.html',context)

@login_required
@require_GET
def home(request):
    if request.user.is_authenticated():
        user = request.user
        context = {"user":user}
        print("Authenticated user")
        return render(request,'account/home.html',context)
    else:
        form = LoginForm()
        Message = "Error in form"
        context = {'form':form}
        print("IN FORM ISNOT VALID")
        return render(request,'account/login.html',context)