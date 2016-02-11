from django.shortcuts import render_to_response, render, get_object_or_404,\
    redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from account.models import *
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.db.models import Q
from feed.forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from proto import settings
from account.views import *


@login_required
def post_create(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST or None, request.FILES)	
		if form.is_valid():
			instance = form.save(commit = False)
			instance.user = request.user
			user = request.user
			instance.save()
			context = {'form' : form, 'user' : user}
			return redirect(timeline)

	context = {'form' : form, }
	return render(request, 'activity/post.html', context)


@login_required
def timeline(request):
	query = request.GET.get('q')
	print(query)
	page = request.GET.get('page')
	followers = request.user.following.all()
	post_list = Post.objects.all()
	query = request.GET.get('q')
	data = {'posts' : []}
	print(query)
	if query:
		post_list = post_list.filter(Q(text__icontains=query))
		print(post_list)

	print(post_list)
	paginator = Paginator(post_list, 10) # Show 10 contacts per page
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)


	context = {'posts' : posts, 'followers' : followers}
	return render(request, 'activity/timeline.html', context)

def post_detail(request, id = None):
	instance = get_object_or_404(Post, id=id)
	print(instance.link)
	context = {'title' : instance.text, 'instance' : instance}
	return render(request, 'activity/post_detail.html', context)

@login_required
def post_update(request, id = None):
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()

		return HttpResponseRedirect(instance.get_absolute_url()) 

	context = {'form' : form}
	return render(request, 'activity/post.html', context)

def post_delete(request, id = None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	return redirect('timeline')


def add_comment(request, id = None):
	post = get_object_or_404(id = id)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save(commit = False)
			form.post = post
			form.save()
			data = {'text' : form.text}
			return JsonResponse(data, safe = False)			