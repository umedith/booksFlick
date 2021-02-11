from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/project$',views.new_project, name='newproject'),
    url(r'^new/profile$',views.new_profile, name='new-profile'),
    url(r'^profile$',views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^vote/(?P<id>\d+)',views.rating,name='rating'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profile-api'),
    url(r'^api/project/$', views.ProjectList.as_view(),name='project-api'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)