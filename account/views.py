from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template import loader
from django.db.models.signals import pre_save
from django.template import RequestContext
from django.views.generic import ListView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import *
from django.db.models import Q
from .models import *
from feed.views import *


# Create your views here.
@require_http_methods(['GET', 'POST'])
def base(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = LoginForm();
    else:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = f.get_user()
            auth_login(request, user)
            print("Valid")
            #return JsonResponse(data = {'success': True})
            return redirect('home')
        else:
            data = {'error': True, 'errors' : dict(f.errors.items())}
            return	JsonResponse(status = 400, data = data)

    return render(request, 'authentication/login.html',{'form': f})		


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f =SignupForm();
    else:
        f = SignupForm(request.POST)
        if f.is_valid():
            user = f.save();
            email_body_context = {
                'username' : user.username,
                'token': urlsafe_base64_encode(force_bytes(user.username)),
                'uid' : user.id,
                'protocol': 'http',
                'domain' : get_current_site(request).domain
            }
            body = loader.render_to_string('authentication/signup_email_body_text.html', email_body_context)
            email_message = EmailMultiAlternatives('Welcome To Proto',body, settings.DEFAULT_FROM_EMAIL, [user.email])
            email_message.send()
            return render(request, 'authentication/signup_email_sent.html', { 'email' : user.email })
    return render(request, 'authentication/signup.html', { 'form': f})


@require_GET
def logout(request):
    auth_logout(request)
    return redirect('base');

@require_GET
@login_required
def home(request):
    # print(request.user.profile_pic)

    return redirect('timeline')



@require_GET
def activate(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    '''
    try:
        user = MyUser.objects.get(id = uid)
    except MyUser.DoesNotExist:
        raise Http404('Invalid User')
    '''
    user = get_object_or_404(MyUser, id = uid)
    username_from_token = force_text(urlsafe_base64_decode(token))
    if user.is_active:
        return redirect('base')

    if user.username == username_from_token:
        user.is_active = True
        user.save()
        return render(request, 'authentication/activation_success.html')
    else:
        return render(request, 'authentication/activation_failure.html')


@require_http_methods(['GET', 'POST'])
def forgot_password(request):
    if request.user.is_authenticated():
        return redirect('home')
    if request.method == 'GET':
        f = ForgotPasswordForm()
    if request.method == 'POST':
        f = ForgotPasswordForm(request.POST)
        if f.is_valid():
            user = MyUser.objects.get(email = f.cleaned_data['email'])
            email_body_context = {
                'username' : user.username,
                'token': default_token_generator.make_token(user),
                'uid' : user.id,
                'protocol': 'https' if settings.USE_HTTPS else 'http',
                'domain' : get_current_site(request).domain
            }
            body = loader.render_to_string('authentication/forgot_password_email_body_text.html', email_body_context)
            email_message = EmailMultiAlternatives('Reset your password on MiniQuora',body, settings.DEFAULT_FROM_EMAIL, [user.email])
            email_message.send()
            context = {'email': user.email}
            return render(request, 'authentication/forgot_password_email_sent.html', context)
    context = {'form': f}
    return render(request, 'authentication/forgot_password.html',context)

@require_http_methods(['GET', 'POST'])
def reset_password(request, uid = None, token = None):
    if request.user.is_authenticated():
        return redirect('home')
    try:
        user = MyUser.objects.get(id = uid)
    except(MyUser.DoesNotExist):
        user = None
    if not user or not default_token_generator.check_token(user,token):
        context = {'validlink': False}
        return render(request, 'authentication/set_password.html', context)
    if request.method == 'GET':
        f = SetPasswordForm()
    else:
        f = SetPasswordForm(request.POST)
        if f.is_valid():
            user.set_password(f.cleaned_data['password1'])
            user.save()
            return redirect('base')
    context = {'validlink': True, 'form': f}
    return render(request, 'authentication/set_password.html', context)


# def handle_uploaded_pic(self):
#     dest = open('profile_pics/', wb+)
#     for chunk in self.chunks():
#         dest.write(chunk)
#     dest.close()

@require_http_methods(['GET', 'POST'])
@login_required
def edit_profile(request):
    if request.method == 'GET':
        print("in to get profile")
        form = ProfileForm(instance = request.user)
    if request.method == 'POST':
        print("Before")
        form = ProfileForm(request.POST or None, request.FILES, instance = request.user)
        print(request.user)
        if form.is_valid():
            # print(request.FILES['profile_pic'])

            user_profile = form.save(commit = False)#getting the instance of the form so that it doesn't generate a new instance every time.
            # print(user_profile)
            user_profile.user = request.user
            # if request.FILES:
            #     new_profile_pic = MyUser(profile_pic = request.FILES['profile_pic'])
            #     new_profile_pic.save()
            # handle_uploaded_pic(request.FILES['profile_pic'])
            form.save()
            context = {'save_success': 'True'}
            return redirect('home')
            
        else:
            print(form.errors)
            data = {'error': True, 'errors': dict(form.errors.items())}
            return JsonResponse( status = 400, data = data)

    print("Before rendering")        
    return render(request, 'authentication/profile.html', {'form': form, 'my_skills': request.user.user_skills.all()})  


@login_required
@require_GET
def search(request):
    query_term = request.GET.get('q')
    data = {'skills': []}
    print(query_term)
    if not query_term:
        return JsonResponse(data)
    skills = SkillSet.objects.filter(
        Q(tags__icontains = query_term)
    )
    # print(request.user.user_skills)
    data['skills'] = [{'id' : q.id, 'tags' : q.tags} for q in skills]
    return JsonResponse(data)

@csrf_exempt
@login_required
@require_POST
def save(request):
    print(request.POST) 
    skill = request.POST.get('skill')
    # print(skill)
    obj =  SkillSet.objects.get(pk = skill)
    user = request.user.user_skills.add(obj)
    print(obj.of_user.all())
    print(request.user.user_skills.all())
    print(obj)
    # request.user.user_skills += obj
    # data = {'user_skills' : []}
    print(request.user)
    # print(request.user_set.all())
    context = { 'my_skills' : request.user.user_skills.all() }
    print(context['my_skills'])
    return render(request, 'base/loggedin.html', context)

@require_GET
@login_required
def add_skills(request):
    return render(request, 'base/add_skills.html')

@require_GET
@login_required
def my_profile(request):
    user_projects = request.user.user_project.all()
    context = {'user' : request.user, 'my_skills' : request.user.user_skills.all(), 'projects' : user_projects}
    return render(request, 'base/my_profile.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def add_project(request):
    if request.method == 'GET':
        print('get form')
        form = AddProjectForm(current_user = request.user)

    else:
        form = AddProjectForm(request.POST, current_user = request.user)
        print("post")
        if form.is_valid():
            project_instance = form.save(commit = False)
            print('valid')
            # project_instance = form.save(commit = False)
            selected_user_mentor = form.cleaned_data.get('mentor')
            project_instance.of_user = request.user
            form.save()
            # print(Project.title)
            user_projects = request.user.user_project.all()
            context = { 'Project' : user_projects }
            print('before')
            return redirect(request, 'base/my_profile.html', context)

    return render(request, 'base/add_project.html', {'form' : form})

def open_profile(request, id = None):
    instance = get_object_or_404(MyUser, id=id)
    skills = instance.user_skills.all()
    print(skills)
    user_projects = instance.user_projects.all()
    context = {'instance' : instance, 'projects' : user_projects, 'skills' : skills}
    return render(request, 'base/open_profile.html', context)


@require_GET
@login_required
def otherhome(request):
    users = MyUser.objects.all()
    context = {'users': users, 'friends' : request.user.following.all()}
    return render(request, 'base/follow.html', context)


@require_GET
@login_required
def follow(request, id = None):
    print("in follow")
    to_user = get_object_or_404(MyUser, id=id)
    from_user = request.user
    data = {'result' : 0}
    if to_user.id != from_user.id and to_user not in from_user.following.all():
        from_user.following.add(to_user)
        data['result'] = 1
        return JsonResponse(data, safe = False)
    else:
        if from_user.id == to_user.id:
            data['error'] = "You Cannot follow yourself"

        else:
            data['error'] = "You are already following this user"    
        return JsonResponse(data, safe = False)

@require_GET
@login_required
def unfollow(request, id = None):
    to_user = get_object_or_404(MyUser, id = id)
    from_user = request.user
    data = {'result' : 0}
    if to_user.id != from_user.id and to_user in from_user.following.all():
        from_user.following.remove(to_user)
        data['result'] = 1
        return JsonResponse(data, safe = False)
    else:
        if from_user.id == to_user.id:
            data['error'] = "You cannot unfollow yourself"
        else:
            data['error'] = "You are not following this user"
        return JsonResponse(data, safe = False)