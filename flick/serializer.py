from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_photo', 'user_project','contact','user')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'project_image', 'description','link','user')