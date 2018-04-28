# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from sappsapp.models import *
from sappsapp.forms import *
from datetime import date
# Create your views here.

today=date.today()
def index(request):
	return render(request, 'index.html', context=None)


def login(request):
	return render(request, 'login.html', context=None)


studtotal = User.objects.filter(groups__name='Students').count()
spresent = Attendance.objects.filter(day = today).count()
spercent = (float(spresent)/float(studtotal))*100



@login_required
def dashboard(request):
        if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			assigns = Assignments.objects.filter(user = request.user).count()
			res = Resources.objects.filter(user = request.user).count()
		except:
			profile = {}
			assigns = {}
			res={}
        if request.user.is_staff:
           return HttpResponseRedirect(reverse('dashboard'))
        else:
           return HttpResponseRedirect(reverse('parentprofile'))
	
	return render(request, 'dashboard.html', {'profile':profile, 'spercent':spercent, 'spresent':spresent, 'assigns':assigns,'res':res})


@login_required
def profile(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
		except:
			profile = None
	return render(request, 'dashboard/profile.html', {'profile':profile})

@login_required
def profileedit(request):
	try:
		profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
	except:
		profile = None
	if request.method == "POST":
		form = ProfileteacherForm(request.POST, instance=profile)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.save()
			return redirect('profile')
	else:
		form = ProfileteacherForm(instance=profile)
	return render(request, 'dashboard/profileedit.html', {'form':form, 'profile':profile })


@login_required
def students(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			childprofile = Profilechild.objects.all()
		except:
			profile = None
			childprofile =None
	return render(request, 'dashboard/students.html', {'profile':profile, 'childprofile':childprofile})


@login_required
def attendance(request):

	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			attend = Attendance.objects.filter(day=today)
		except:
			profile = {}
			attend = {}
	if request.method == "POST":
		form = AttendanceForm(request.POST)
		if form.is_valid():
			att = form.save(commit=False)
			att.save()
			return redirect('attendance')
	else:
		form = AttendanceForm()
	return render(request, 'dashboard/attendance.html', {'profile':profile, 'form':form, 'attend':attend })


@login_required
def mcqs(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			mcqs = Mcqs.objects.filter(user=request.user)
		except:
			profile = {}
			mcqs = {}
	if request.method == "POST":
		form = McqsForm(request.POST)
		if form.is_valid():
			att = form.save(commit=False)
			att.user = request.user
			att.marks = 0
			att.save()
		return redirect('mcqs')
	else:
		form = McqsForm()
	return render(request, 'dashboard/setmcq.html', {'profile':profile, 'mcqs':mcqs, 'form':form })


@login_required
def assignments(request):
	user = request.user
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
			assigns = Assignments.objects.filter(user=user)
		except:
			profile = {}
			assigns = {}
	if request.method == "POST":
		form = AssignmentsForm(request.POST, request.FILES)
		if form.is_valid():
			forms = form.save(commit=False)
			forms.user = user
			forms.save()
			return redirect('assignments')
	else:
		form = AssignmentsForm()
	return render(request, 'dashboard/assignments.html', { 'profile':profile, 'assigns':assigns, 'form':form, })


@login_required
def resources(request):
	user = request.user
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
			res = Resources.objects.filter(user=user)
		except:
			profile = {}
			res ={}
	if request.method == "POST":
		form = ResourcesForm(request.POST, request.FILES)
		if form.is_valid():
			formres = form.save(commit=False)
			formres.user = user
			formres.save()
			return redirect('resources')
	else:
		form = ResourcesForm()
	return render(request, 'dashboard/resources.html', { 'profile':profile, 'res':res, 'form':form, })

def ques(request, pk):
	pk = pk
	mcq = Mcqs.objects.get(pk=pk)
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			formq = form.save(commit=False)
			formq.mcq = mcq
			formq.save()
			return redirect('ques', pk=pk)
	else:
		form = QuestionForm()
	return render(request, 'dashboard/mcq.html', { 'profile':profile, 'form':form, 'mcq':mcq })


#Assignment DELETE
def removeassigns(request, pk):
    post = get_object_or_404(Assignments, pk=pk)
    post.delete()
    return redirect('assignments')

#Attendance DELETE
def removeattend(request, pk):
    post = get_object_or_404(Attendance, pk=pk)
    post.delete()
    return redirect('attendance')

#Resources DELETE
def removeres(request, pk):
    post = get_object_or_404(Resources, pk=pk)
    post.delete()
    return redirect('resources')

#Search Attendance
def searchattend(request):
	attend={}
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			aitem = form.save(commit= False)
			aitem.save()
			try:
				user = User.objects.get(username = aitem.item)
				attend = Attendance.objects.filter(user = user)
			except:
				try:
					attend = Attendance.objects.filter(day = aitem.item)
				except:
					pass
	return render(request, 'dashboard/attendance.html', {'profile':profile, 'attend':attend })

#Search Students
def searchstud(request):
	childprofile={}
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			sitem = form.save(commit= False)
			sitem.save()
			try:
				user = User.objects.get(username = sitem.item)
				childprofile = Profilechild.objects.filter(user = user)
			except:
				try:
					childprofile = Profilechild.objects.all()
				except:
					pass
	return render(request, 'dashboard/students.html', {'profile':profile, 'childprofile':childprofile})

#student profile
def studentpro(request, pk):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
		prof = Profilechild.objects.get(pk=pk)
	return render(request, 'dashboard/student/stdntproforteacher.html', {'profile':profile, 'prof':prof })

#student detail
def attendanceres(request,pk):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
		user = User.objects.get(pk=pk)
		attend = Attendance.objects.filter(user=user)
	return render(request, 'dashboard/student/attendanceres.html', {'attend':attend, 'profile':profile})

#assignment detail
def assignmentdet(request,pk):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
		user = User.objects.get(pk=pk)
		attend = Assignments.objects.filter(user=user)
	return render(request, 'dashboard/student/assignmentdet.html', {'attend':attend, 'profile':profile})


def parentpro(request,pk):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
		except:
			profile = None
		pprof = Profileparent.objects.get(pk=pk)
	return render(request, 'dashboard/parent/parentprofile.html', {'profile':profile, 'pprof':pprof })


@login_required
def parents(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			parentprofile = Profileparent.objects.all()
		except:
			profile = None
			parentprofile =None
	return render(request, 'dashboard/parents.html', {'profile':profile, 'parentprofile':parentprofile})


#questions list mcq
def questionlist(request,pk):
    lis = Question.objects.all()
    return render(request, 'dashboard/questionlist.html', {'lis':lis})

#Question DELETE
def questiondelete(request, pk):
    post = get_object_or_404(Mcqs, pk=pk)
    post.delete()
    return redirect('mcqs')

#University result main page add
def subject(request):
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=request.user, user__is_active = True)
			mcqs = Univresults.objects.filter(user=request.user)
			users = User.objects.all()
		except:
			profile = {}
			mcqs = {}
			users = {}
	return render(request, 'dashboard/subject.html', {'profile':profile, 'users':users, })

#add semester mark
def markadd(request, pk):
	pk = pk
	mcq = Univresults.objects.get(pk=pk)
	try:
		subjects = Subject.objects.filter()
	except:
		profile = {}
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
	if request.method == "POST":
		form = SubjectForm(request.POST)
		if form.is_valid():
			formq = form.save(commit=False)
			formq.mcq = mcq
			formq.save()
			return redirect('markadd', pk=pk)
	else:
		form = SubjectForm()
	return render(request, 'dashboard/markadd.html', { 'profile':profile, 'form':form, 'mcq':mcq })





	

#sem name add

def semname(request, pk):
	pk = pk
	mcq = Univresults.objects.get(pk=pk)
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
                        
		except:
			profile = {}
        if request.method == "POST":
		form = UnivresultsForm(request.POST)
		if form.is_valid():
			formq = form.save(commit=False)
			formq.mcq = mcq
			formq.save()
			return redirect('semname', pk=pk)
	else:
		form = UnivresultsForm()
	return render(request, 'student/semname.html', { 'profile':profile, 'mcq':mcq,'form':form })

#Search Students
def searchparent(request):
	parentprofile={}
	if request.user.is_authenticated():
		try:
			profile = Profileteacher.objects.get(user=user, user__is_active = True)
		except:
			profile = {}
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			sitem = form.save(commit= False)
			sitem.save()
			try:
				user = User.objects.get(username = sitem.item)
				parentprofile = Profileparent.objects.filter(user = user)
			except:
				try:
					parentprofile = Profileparent.objects.all()
				except:
					pass
	return render(request, 'dashboard/parents.html', {'profile':profile, 'parentprofile':parentprofile})





