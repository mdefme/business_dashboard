from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    working_on = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.working_on)

class Project(models.Model):
    project_name = models.CharField(max_length=30,null=True)
    project_description = models.CharField(max_length=200,null=True)
    #provjeri ako ce raditi
    project_date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.project_name)

class Subproject(models.Model):
    subproject_name = models.CharField(max_length=15,null=True)
    number_of_scenes = models.IntegerField(null=True)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.subproject_name)
        #return '['+self.project_id.project_name +'] '+ self.subproject_name

class Scene(models.Model):

    scene_name = models.CharField(max_length=30,null=True,)
    leader_approved_text = models.BooleanField(default=False)
    leader_approved_image = models.BooleanField(default=False)
    client_approved_text = models.BooleanField(default=False)
    client_approved_image = models.BooleanField(default=False)
    subproject_id = models.ForeignKey(Subproject,on_delete=models.CASCADE,null=True)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE,null=True)

    def __str__(self):
        #return '['+self.project_id.project_name +'] '+ self.scene_name
        return str(self.scene_name)

class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=30,null=True,)
    tutorial_paragraph = models.TextField(max_length=1400,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        #return '['+self.project_id.project_name +'] '+ self.scene_name
        return str(self.tutorial_name)

"""
TO DO:
-tutorials/blog
-audio?
"""