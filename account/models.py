from django.db import models
from django.contrib.auth.models import User, AbstractUser   
from django.core.validators import URLValidator
# from multiselectfield import MultiSelectField
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


GENDER_CHOICES = (('NS', '--'),('M', 'Male'),('F', 'Female'))
BRANCH_CHOICES = (('NS', '--'),('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), 
    ('EEE', 'Electronics and Electrical Engineering'), ('ICE', 'Instrumentation and Control Engineering'))
YEAR_CHOICES = (('1st','First Year'), ('2nd', 'Second Year'),('3rd', 'Third Year'),('4th', 'Fourth'))

class MyUser(AbstractUser):
    profile_pic = models.ImageField(upload_to = 'media/profile_pics', blank = True)
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES, default = GENDER_CHOICES[0][0])
    dob = models.DateField(blank=True, null=True, auto_now_add = False)
    roll_no = models.BigIntegerField(verbose_name = 'Roll Number', blank = True, default = 0)
    year = models.CharField(max_length = 3, choices = YEAR_CHOICES, default = "--")
    branch = models.CharField(max_length = 3, choices = BRANCH_CHOICES, verbose_name = 'Branch',default = BRANCH_CHOICES[0][0],
        blank = True, null = True)
    profile_links = models.TextField(validators=[URLValidator()], default = "--", help_text = "Prefer Linked In Profile")
    following = models.ManyToManyField('self', symmetrical = False, related_name = 'follower')



    unique_together = ('email',)
    verbose_name = 'User'

    def __str__(self):
        return self.username    
    	
class SkillSet(models.Model):
    tags = models.CharField(max_length = 30)
    is_saved = models.BooleanField(default = False)
    of_user = models.ManyToManyField(MyUser, related_name ='user_skills')

    def __str__(self):
        return self.tags

DEFAULT_MENTOR_USER = 1
class Project(models.Model):
    title = models.CharField(max_length = 30, blank = True)
    description = models.TextField(max_length = 200, blank = False)
    is_team = models.BooleanField(default = False)
    team_member = models.ManyToManyField(MyUser, related_name = "member_of_team")
    mentor = models.ForeignKey(MyUser, related_name = "user_projects", null = True ,default = DEFAULT_MENTOR_USER)
    related_link = models.CharField(validators=[URLValidator()], max_length = 254, unique = True, blank = True)
    of_user = models.ForeignKey(MyUser, related_name = "user_project")
