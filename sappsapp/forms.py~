from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileteacherForm(forms.ModelForm):
    class Meta:
        model = Profileteacher
        fields = ('phone','email','gender','department','qualification','about','address','picture')


CHOICES=[('student','student'),('parent','parent')]


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields =('user','day','status')


class McqsForm(forms.ModelForm):
    class Meta:
        model = Mcqs
        fields = ('test_id','name')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('mcq','question', 'c1', 'c2', 'c3', 'c4', 'answer')

class UnivresultsForm(forms.ModelForm):
      class Meta:
        model = Univresults
        fields = ('user','semname',)

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('sem','sub','mark','internal','maxi','internmaxi','total','res',)


class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('topic','disc','fil',)


class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = ('topic','disc','video',)



class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('item',)

class AttendexamForm(forms.ModelForm):
    class Meta:
        model = Attendexam
        fields = ('answerkey',)
