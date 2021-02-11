from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length =30)
    project_image = models.ImageField(upload_to='images/', blank=True)
    description= models.CharField(max_length =150)
    link = models.TextField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    
    def __str__(self):
        return self.title

    def save_project(self):
        self.save() 

    def delete_project(self):
        self.delete()          
    
    @classmethod
    def search_project(cls,title):
        title = cls.objects.filter(title__icontains=title)
        return  title

class Profile(models.Model):
    # bio= HTMLField()
    profile_photo=models.ImageField(upload_to ='photos/',null=True)
    user_project= models.ForeignKey(Project,null=True, on_delete=models.CASCADE)
    contact=models.IntegerField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save() 