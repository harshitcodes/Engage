from account.models import MyUser
from django.db import models
from django.db.models import Q
# from django.db.models import signals
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save


class Post(models.Model):
    user = models.ForeignKey('account.MyUser')
    slug =  models.SlugField(unique = True)
    text = models.CharField(max_length=160)
    image = models.ImageField(upload_to = 'media/feed_pics', blank = True, null = True)
    link = models.TextField(blank = True, null = True)
    upload_file = models.FileField(upload_to = 'files/', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)


    class Meta:
    	ordering = ['-created_at', '-updated_at']
    def __str__(self):
    	return self.text
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments")
    text = models.TextField(max_length = 10000)


def create_slug(instance, new_slug = None):
    slug = slugify(instance.text)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug = new_slug)
    return slug    


def pre_save_post_receiver(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender = Post)        

