from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from multiselectfield import MultiSelectField
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


GENDER_CHOICES = (('NS', '--'),('M', 'Male'),('F', 'Female'))
BRANCH_CHOICES = (('NS', '--'),('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), 
    ('EEE', 'Electronics and Electrical Engineering'), ('ICE', 'Instrumentation and Control Engineering'))

class MyUser(AbstractUser):
    profile_pic = models.ImageField(upload_to = 'media/profile_pics', blank = True)
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES, default = GENDER_CHOICES[0][0])
    # dob = models.DateField(blank=True, null=True, auto_now_add = False)
    roll_no = models.BigIntegerField(verbose_name = 'Roll Number', blank = True, default = 0)
    branch = models.CharField(max_length = 3, choices = BRANCH_CHOICES, verbose_name = 'Branch',default = BRANCH_CHOICES[0][0],
        blank = True, null = True)

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



    





    # SKILL_SET = (('NS',''), ('C','C'), ('C++', 'C++'), ('Python', 'Python'), ('JAVA', 'JAVA'), ('Javascript', 'Javascript'), 
    # ('Web Development', 'Web Development'), ('Django','Django'), ('Ruby On Rails', 'Ruby On Rails'), 
    # ('Android App Development','Android App Development'),('iOS App Development', 'iOS App Development'), ('Microprocessors', 
    # 'Microprocessors'), ('C#', 'C#'), ('Electronics','Electronics'), ('HTML', 'HTML'), ('HTML 5', 'HTML 5'), ('CSS', 'CSS'), 
    # ('CSS3', 'CSS3'), ('jQuery', 'jQuery'), ('Data Structures', 'Data Structures'), ('Algorithms', 'Algorithms'), ('Robotics','Robotics'),
    # ('Bootstrap', 'Bootstrap'), ('Perl', 'Perl'), ('.NET', '.NET'), ('Data Mining', 'Data Mining'), ('Big Data', 'Big Data'),
    # ('Cloud Computing', 'Cloud Computing'), ('UX Design', 'UX Design'), ('Photoshop','Photoshop'),('SQL','SQL'),
    # ('GNU/Linux','GNU/Linux'), ('Embedded System','Embedded System'), ('VLSI', 'VLSI'))
