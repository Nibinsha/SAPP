# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,  get_object_or_404
# Create your views here.

from sappsapp.models import *
from sappsapp.forms import *
from django.contrib.auth.decorators import login_required


#student profile

@login_required
def studentprofile(request):
        
	if request.user.is_authenticated():
           try:
           
      	     profile = Profilechild.objects.get(user=request.user)
           except:
			profile = {}

        context = { 'profile':profile }
	return render(request, 'student/profile.html', context)


#student assignment
@login_required
def stuassignmentdet(request):
	if request.user.is_authenticated():
		try:
			profile = Profilechild.objects.get(user=request.user)
		except:
			profile = {}
		
		assign = Assignments.objects.filter(user=request.user)
	return render(request, 'student/stuassignmentdet.html', {'assign':assign, 'profile':profile})

#student attendance
@login_required
def stuattendanceres(request):
	if request.user.is_authenticated():
		attend = Attendance.objects.filter(user=request.user)
	return render(request, 'student/stuattendanceres.html', {'attend':attend,})

#student resources
@login_required
def studentresources(request):
	if request.user.is_authenticated():
		try:
			res = Resources.objects.filter(user=request.user)
		except:			
			res ={}
	return render(request, 'student/studentresource.html', { 'res':res, })


#MCQ for student
@login_required
def questions(request):
	
	if request.user.is_authenticated():
		try:
			que = Mcqs.objects.all()
		except:
			que = {}
	return render(request, 'student/studentmcq.html', { 'que':que })

#attend exam
@login_required
def attendexam(request,pk):
    pk = pk
    mcq = Mcqs.objects.get(pk=pk)
    quest= Question.objects.filter(mcq=mcq)
    print type(quest)

    if request.method == "POST":
		form = AttendexamForm(request.POST)
		if form.is_valid():
			formq = form.save(commit=False)
			formq.save()
			return redirect('attendexam',pk=pk)
    else:
		form = AttendexamForm()
    return render(request, 'student/attendexam.html', {'quest':quest, 'ans':form})

#MCQ for student
@login_required
def studentUnires(request):
	
	if request.user.is_authenticated():
		try:
			mark = Univresults.objects.filter(user=request.user)
		except:
			mark = {}
	return render(request, 'student/studentUnires.html', { 'mark':mark })
    
#view result
@login_required
def viewres(request,pk):
    if request.user.is_authenticated():
		try:
			que = Subject.objects.get(pk=pk)
		except:
			que = {}
    print type(que)
    print Subject
    return render(request, 'student/viewres.html', {'quest':que})




