from django import forms
from django.contrib.auth import authenticate
from .models import *
from django.forms import extras
from material import *
from django.db.models import Q
from django.utils.text import slugify
from django.core.validators import URLValidator

class SignupForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password', widget = forms.PasswordInput, help_text = 'Should be same as Password')
	def clean_password2(self):
		data_password1 = self.cleaned_data['password1']
		data_password2 = self.cleaned_data['password2']
		if data_password1 and data_password2 and data_password2 != data_password1:
			raise forms.ValidationError("Passwords don't match")
		return data_password2
	
	def save(self,commit = True):
		user = super(SignupForm, self).save(commit = False)
		user.set_password(self.cleaned_data.get('password1'))
		user.is_active = False
		if commit:
			user.save()
		return user
	
	class Meta:
		model = MyUser
		fields = ['username', 'email']

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 20)
	password = forms.CharField(widget = forms.PasswordInput(attrs = {'class' : 'dumb', 'placeholder' : 'Enter Password'}))
	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(LoginForm, self).__init__(*args, **kwargs)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			print("authenticated")
			self.user_cache = authenticate(username = username, password = password)

			if self.user_cache is None:
				raise forms.ValidationError('Invalid username or Password')
			elif not self.user_cache.is_active:
				raise forms.ValidationError('User is not active')
			return 	self.cleaned_data
	
	def get_user(self):
		return self.user_cache

class ForgotPasswordForm(forms.Form):
	email = forms.EmailField(max_length = 254)
	def clean_email(self):
		data_email = self.cleaned_data.get('email')
		if data_email and MyUser.objects.filter(email = data_email).count() == 0:
			raise forms.ValidationError("We cannot find the user with this email address. Please verify email address and try again.")
		return data_email
class SetPasswordForm(forms.Form):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput, help_text = 'Should be same as Password')

	def clean_password2(self):
		data_password1 = self.cleaned_data['password1']
		data_password2 = self.cleaned_data['password2']
		if data_password1 and data_password2 and data_password1 !=data_password2:
			raise forms.ValidationError("Passwords don't match")
		return data_password2	

class ProfileForm(forms.ModelForm):
	old_password = forms.CharField(label = 'Current Password', widget = forms.PasswordInput, required = False)
	new_password = forms.CharField(label = 'New Password', widget = forms.PasswordInput, required = False)
	# dob = forms.DateField(widget = extras.SelectDateWidget(years = [y for y in range(1990, 2000)]), required = False)
	layout = Layout(
		Row(Span6('first_name'), Span6('last_name')),
		Row('gender'),
		Row(Span4('dob'), Span6('roll_no')),
		Row('branch'),
		Row('year'),
		Row('profile_links'),
		# Row('skill_set'),
		Row('old_password', 'new_password'),
		Row('profile_pic'), 
		)

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		# self.fields['username'].widget.attrs['readonly'] = True
		# self.fields['email'].widget.attrs['readonly'] = True
		self.fields['roll_no'].required = True
		instance_roll_no = 	getattr(self, 'instance', None)
		if instance_roll_no and instance_roll_no.pk:
			self.fields['roll_no'].widget.attrs['readonly'] = True
		self.fields['first_name'].required = True


	def clean_gender(self):
		data_gender = self.cleaned_data['gender']
		if data_gender and data_gender == 'NS':
			raise forms.ValidationError("You must specify your gender")
		return data_gender
		
	def clean_old_password(self):
		data_old_password = self.cleaned_data['old_password']
		if data_old_password and not self.instance.check_password(data_old_password):
			raise forms.ValidationError("Incorrect Password")
		return data_old_password
		
	def clean_new_password(self):
		data_old_password = self.cleaned_data['old_password']
		data_new_password = self.cleaned_data['new_password']
		if not data_old_password and data_new_password:
			raise forms.ValidationError("Please Specify old Password")
		if data_new_password and data_new_password == data_old_password:
			raise forms.ValidationError("New Password should not be same as old password")
		return data_new_password

	def clean_profile_links(self):
		data_profile_links = self.cleaned_data['profile_links']
		# validate = URLValidator(verify_exists = True)
		return data_profile_links




	# def clean_username(self):
	# 	data_username = self.cleaned_data['username']
	# 	if data_username != self.instance.username:
	# 		raise forms.ValidationError("Invalid Username")
	# 	return data_username
		
	# def clean_email(self):
	# 	data_email = self.cleaned_data['email']
	# 	if data_email != self.instance.email:
	# 		raise forms.ValidationError("Invalid Email")
	# 	return data_email
		
	def clean_roll_no(self):
		data_roll_no = self.cleaned_data['roll_no']
		# This is a read only field and cannot be updated after it is submitted for the first time..
		#getting an instance of roll_no and then checking if it is already there..
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
			return instance.roll_no
		if len(data_roll_no) > 11 or len(data_roll_no) < 11:
			raise forms.ValidationError("Invalid Roll Number")
		self.instance['roll_no'].widget.attrs['readonly'] = True	
		return data_roll_no	
		

	def save(self, commit = True):
		user = super(ProfileForm, self).save(commit = False)
		if self.cleaned_data['new_password']:
			user.set_password(self.cleaned_data['new_password'])
		if commit:
			user.save()
		return user

	class Meta:
		model = MyUser
		fields = ['first_name', 'last_name', 'profile_pic', 'roll_no', 'gender', 'branch','dob', 'profile_links', 'year']
		widgets = {'dob': extras.SelectDateWidget(years = [y for y in range(1990, 2002)])}



class AddProjectForm(forms.ModelForm):
	# mentor = forms.ModelMultipleChoiceField(queryset = MyUser.objects.all(), )
	layout = Layout(
		Fieldset("Please Enter the details of your Project", 
			Row('title'),
			Row('description'),
			# Row(Span4('is_team'), Span6('team_member')),
			Row('mentor'),
			Row('related_link'),
		))

	def __init__(self, *args, **kwargs):
		print('in')
		current_user = kwargs.pop('current_user', None)
		print(current_user)
		super(AddProjectForm, self).__init__(*args, **kwargs)
		self.fields['mentor'] = forms.ModelChoiceField(queryset = MyUser.objects.exclude(id = current_user.id))


	class Meta:
		model = Project
		fields = ['title', 'description', 'mentor', 'related_link']
		widgets = {'is_team': forms.CheckboxInput}


#, 'is_team', 'team_member'
