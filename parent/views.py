# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,  get_object_or_404
# Create your views here.

from sappsapp.models import *
from sappsapp.forms import *
from django.contrib.auth.decorators import login_required


#student profile

@login_required
def parentprofile(request):
        
	if request.user.is_authenticated():
           try:
           
      	     profile = Profilechild.objects.get(user=request.user)
           except:
			profile = {}

        context = { 'profile':profile }
	return render(request, 'parent/profile.html', context)



#student attendance
@login_required
def parattendanceres(request):
	if request.user.is_authenticated():
		attend = Attendance.objects.filter(user=request.user)
	return render(request, 'parent/parattendanceres.html', {'attend':attend,})


#MCQ for student
@login_required
def parentUnires(request):
	
	if request.user.is_authenticated():
		try:
			mark = Univresults.objects.filter(user=request.user)
		except:
			mark = {}
	return render(request, 'parent/parentUnires.html', { 'mark':mark })
    
#view result
@login_required
def parentviewres(request,pk):
    if request.user.is_authenticated():
		try:
			que = Subject.objects.get(pk=pk)
		except:
			que = {}
    print type(que)
    print Subject
    return render(request, 'parent/viewres.html', {'quest':que})




