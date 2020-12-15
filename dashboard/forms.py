from django.forms import ModelForm
from .models import Project,Subproject,Task,Tutorial
from django import forms

class ProjectForm(ModelForm):

    project_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Project name'
    }))
    project_description = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Project description'
    }))

    class Meta:
        model = Project
        fields = ('project_name','project_description')

 
class SubprojectForm(ModelForm):
    subproject_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Subproject name'
    }))
    number_of_scenes = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Number of scenes'
    }))
    
    class Meta:
        model = Subproject
        fields = ('subproject_name','number_of_scenes','project_id')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('working_on',)
        #fields = '__all__'
  
  
class TutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = ('tutorial_name','tutorial_paragraph',)
        #fields = '__all__'