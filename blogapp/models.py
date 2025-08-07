from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_photos/',null=True,blank=True)

    def __str__(self):
        return self.title