from django import forms
from feed.models import Post, Comment
from account.models import MyUser

class PostForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Post
		fields = ['text', 'image', 'link', 'upload_file']


class CommentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Comment
		fields = ['text']