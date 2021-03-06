"""sapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from sappsapp.views import *
from child.views import *
from parent.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^dashboard/profile/$', profile, name='profile'),
    url(r'^dashboard/profileedit/$', profileedit, name='profileedit'),
    url(r'^dashboard/students/$', students, name='students'),
    url(r'^dashboard/attendance/$', attendance, name='attendance'),
    url(r'^dashboard/mcqs/(?P<pk>\d+)/$', ques, name='ques'),
    url(r'^dashboard/mcqs/$', mcqs, name='mcqs'),
    url(r'^dashboard/assignments/$', assignments, name='assignments'),
    url(r'^dashboard/resources/$', resources, name='resources'),
    #remove
    url(r'^parents/', parents, name='parents'),
    url(r'^assigns/(?P<pk>\d+)/remove/$', removeassigns, name='removeassigns'),
    url(r'^res/(?P<pk>\d+)/remove/$', removeres, name='removeres'),
    url(r'^attend/(?P<pk>\d+)/remove/$', removeattend, name='removeattend'),
    #student_profile
    url(r'^studentpro/(?P<pk>\d+)/', studentpro, name='studentpro'),
    #parent_profile
    url(r'^parentpro/(?P<pk>\d+)/', parentpro, name='parentpro'),
    #attendance full result
    url(r'^attendanceres/(?P<pk>\d+)/', attendanceres, name='attendanceres'),
    #assignment det
    url(r'^assignmentdet/(?P<pk>\d+)/', assignmentdet, name='assignmentdet'),
    #university result add for TEACHER
    #search
    url(r'^searchattend/$', searchattend, name='searchattend'),
    url(r'^searchstud/$', searchstud, name='searchstud'),
    url(r'^searchparent/$', searchparent, name='searchparent'),
    #url(r'^attend/(?P<item>[\w\+%_& ]+)/$', removeattend, name='removeattend'),
    #question list
    url(r'^questionlist/(?P<pk>\d+)/$', questionlist, name='questionlist'), 
    #questiondelete
    url(r'^questiondet/(?P<pk>\d+)/remove/$', questiondelete, name='questiondelete'),
    #university result
    url(r'^dashboard/subject/$', subject, name='subject'),
    #mark add
    url(r'^dashboard/markadd/(?P<pk>\d+)/$', markadd, name='markadd'),

    #STUDENT SIDE
    url(r'^student/profile/$', studentprofile, name='studentprofile'),
    #student assignment
    url(r'^student/stuassignmentdet/', stuassignmentdet, name='stuassignmentdet'),
    #student attendance
    url(r'^student/stuattendanceres/', stuattendanceres, name='stuattendanceres'),
    #student quuestions
    url(r'^student/questions/', questions, name='questions'),
    #student resources
    url(r'^student/resources/', studentresources, name='studentresources'),
    #attend exam
    url(r'^student/attendexam/(?P<pk>\d+)/$', attendexam, name='attendexam'),
    #semname
    url(r'^student/semname/$', studentUnires, name='studentUnires'),
    #view result
    url(r'^student/viewres/(?P<pk>\d+)/$', viewres, name='viewres'),

    #PARENT SIDE
    url(r'^parent/profile/$', parentprofile, name='parentprofile'),
    #student attendance
    url(r'^parent/stuattendanceres/', parattendanceres, name='parattendanceres'),
    #semname
    url(r'^parent/semname/$', parentUnires, name='parentUnires'),
    #view result
    url(r'^parent/viewres/(?P<pk>\d+)/$', parentviewres, name='parentviewres'),


    url(r'^accounts/', include('registration.backends.simple.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
