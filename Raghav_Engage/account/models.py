from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)

    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    dob = models.DateField(blank=True, null=True)
    # contact = PhoneNumberField(unique = True, null=True, blank=True, help_text=('Only Indian'))
    # street_address = models.CharField(max_length = 100, null=True, blank=True)
    # city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    # pincode = models.CharField(max_length=8, default="0000000")
    following = models.ManyToManyField("self", symmetrical = False, related_name = "follower")
    class Meta:
    	unique_together = (['email'])
    	verbose_name = 'User'

    def __str__(self):
        return self.username

SKILL_SET = (('','Null'), ('C','C'), ('C++', 'C++'), ('Python', 'Python'), ('JAVA', 'JAVA'), ('Javascript', 'Javascript'),
    ('Web Development', 'Web Development'), ('Django','Django'), ('Ruby On Rails', 'Ruby On Rails'),
    ('Android App Development','Android App Development'),('iOS App Development', 'iOS App Development'), ('Microprocessors',
    'Microprocessors'), ('C#', 'C#'), ('Electronics','Electronics'), ('HTML', 'HTML'), ('HTML 5', 'HTML 5'), ('CSS', 'CSS'),
    ('CSS3', 'CSS3'), ('jQuery', 'jQuery'), ('Data Structures', 'Data Structures'), ('Algorithms', 'Algorithms'), ('Robotics','Robotics'),
     ('Bootstrap', 'Bootstrap'), ('Perl', 'Perl'), ('.NET', '.NET'), ('Data Mining', 'Data Mining'), ('Big Data', 'Big Data'),
     ('Cloud Computing', 'Cloud Computing'), ('UX Design', 'UX Design'), ('Photoshop','Photoshop'),('SQL','SQL'),
     ('GNU/Linux','GNU/Linux'), ('Embedded System','Embedded System'), ('VLSI', 'VLSI'))

class Profile(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30, blank = True)
    Profile_Pic = models.ImageField(upload_to = 'User_ProfilePics/', blank = True)
    followers = models.ManyToManyField(MyUser, related_name = 'following_me')
    skill_set = models.CharField(max_length = 20, choices = SKILL_SET, default = SKILL_SET[0])

    def __str__(self):
        return self.first_name