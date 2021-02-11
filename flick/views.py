from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,NewProfileForm,VoteForm
from .models import Project,Profile 
from django.db.models import Max,F

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer




class ProfileList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializers = ProfileSerializer(profile, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)        

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):

    projects=Project.objects.all()
    average=0
    # average = (project.design + project.usability + project.content)/3
    for p in projects:
        average = (p.design + p.usability + p.content)/3
        best_rating = round(average,2)

    return render(request, 'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('welcome')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewProjectForm()
    return render(request, 'new_book.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
   if 'title' in request.GET and request.GET["title"]:
       search_term = request.GET.get("title")
       searched_projects = Project.search_project(search_term).all()
       current_user = request.user
    #    profile=Profile.objects.filter(user=current_user).first()
       print(searched_projects)
       message = f"{search_term}"
       return render(request, "all-apps/search.html",{"message":message,"titles": searched_projects})
   else:
       message = "You haven't searched for any term"
       return render(request, 'all-apps/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def profile(request):
     current_user= request.user
     project=Project.objects.filter(user=current_user).all()
     profile= Profile.objects.filter(user=current_user).first()   
     return render(request,'profile.html',{"project":project,"profile":profile})       


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('welcome')
        # return render(request, 'all-apps/post.html')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

#Found this on github user="MaryannGitonga"
@login_required(login_url='/accounts/login/')
def rating(request,id):
    project=Project.objects.get(id=id)
    rating = round(((project.design + project.usability + project.content)/3),1)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            project.vote_submissions += 1
            if project.design == 0:
                project.design = int(request.POST['design'])
            else:
                project.design = (project.design + int(request.POST['design']))/2
            if project.usability == 0:
                project.usability = int(request.POST['usability'])
            else:
                project.usability = (project.design + int(request.POST['usability']))/2
            if project.content == 0:
                project.content = int(request.POST['content'])
            else:
                project.content = (project.design + int(request.POST['content']))/2
            project.save()
            return redirect('welcome')
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'project':project,'rating':rating})