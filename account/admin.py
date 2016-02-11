from django.contrib import admin
from .models import MyUser, SkillSet, Project
# Register your models here.
admin.site.register(MyUser)
admin.site.register(SkillSet)
admin.site.register(Project)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
# class ProfileAdmin(admin.ModelAdmin):
# 	form = ProfileForm
# 	fieldsets = (
# 		(None, {
# 			'fields': ('first_name', 'last_name', 'profile_pic', 'roll_no', 'gender', 'branch','dob')
# 			})
# 		)

