from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User
# Create your tests here.

class ProjectTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.user=User.objects.create(id=1,username='stacy')
        self.project1=Project(id=1,title='instagram',project_image='IMG-20181015-WA0007-1.jpg',description='insta application',link='https://newsapplication1.herokuapp.com/',design=2,usability=3,content=4,vote_submissions=1,user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))
        self.assertTrue(isinstance(self.user,User)) 

    def test_save_method(self):
        self.project1.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete(self):
        self.project1.save_project()
        project=Project.objects.filter(title="instagram").first()
        delete=Project.objects.filter(id=project.id).delete()
        projects=Project.objects.all()
        print(projects)
        self.assertTrue(len(projects)==0)  

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user=User.objects.create(id=1,username='stacy')
        self.project1=Project(id=1,title='instagram',project_image='IMG-20181015-WA0007-1.jpg',description='insta application',link='https://newsapplication1.herokuapp.com/',design=2,usability=3,content=4,vote_submissions=1,user=self.user)
        self.profile1=Profile(id=1,bio='my name is stacy',profile_photo='IMG-20181015-WA0007-1.jpg',contact=789709595,user=self.user)

    def test_instance(self):
        
        self.assertTrue(isinstance(self.profile1,Profile))
        self.assertTrue(isinstance(self.project1,Project))
        self.assertTrue(isinstance(self.user,User))

    def test_save_method(self):
        self.profile1.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0) 

    def test_delete(self):
        self.profile1.save_profile()
        profile=Profile.objects.filter(bio="my name is stacy").first()
        delete=Profile.objects.filter(id=profile.id).delete()
        profiles=Profile.objects.all()
        print(profiles)
        self.assertTrue(len(profiles)==0)