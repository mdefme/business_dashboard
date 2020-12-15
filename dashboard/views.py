from django.shortcuts import render,redirect
from .forms import ProjectForm,SubprojectForm,TaskForm,TutorialForm
from .models import Project,Subproject,Scene,User,Task,Tutorial
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def homepage(request):
    
    projects = Project.objects.all()

    project_form = ProjectForm()
    
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            print(request.POST['project_name'])
            #request.POST['project_name']
            #tu je spremljen podatak iz forme
            return redirect('homepage')

    context = {'projects':projects,'project_form':project_form}
    print(request.user.username)
    return render(request,'dashboard/homepage.html',context)

@login_required
def project_dashboard(request,project_id):
    subprojects = Subproject.objects.filter(project_id=project_id)
    project_number_of_scenes = Scene.objects.filter(project_id=project_id).count()
    project_leader_approved_text = Scene.objects.filter(project_id=project_id,leader_approved_text=True).count()
    project_leader_approved_image = Scene.objects.filter(project_id=project_id,leader_approved_image=True).count()
    project_client_approved_text = Scene.objects.filter(project_id=project_id,client_approved_text=True).count()
    project_client_approved_image = Scene.objects.filter(project_id=project_id,client_approved_image=True).count()

    project_name = Project.objects.get(id=project_id).project_name
    print(project_name)
    
    

    subproject_form = SubprojectForm(initial={'project_id':project_id})
    if request.method == 'POST':
        subproject_form = SubprojectForm(request.POST)
        if subproject_form.is_valid():
            subproject_form.save()
            return redirect('project_dashboard',project_id)
            
    context = {
        'subprojects':subprojects,
        'subproject_form':subproject_form,
        'project_leader_approved_text' : project_leader_approved_text,
        'project_leader_approved_image': project_leader_approved_image,
        'project_client_approved_text':project_client_approved_text,
        'project_client_approved_image':project_client_approved_image,
        'project_number_of_scenes':project_number_of_scenes,
        'project_name':project_name
        }
        
    return render(request,'dashboard/project_dashboard.html',context)

@login_required
def subproject_dashboard(request,project_id,subproject_id):

    project = Project.objects.get(id=project_id)
    subproject = Subproject.objects.get(id=subproject_id)
    number_of_scenes = subproject.number_of_scenes
    subproject_name = subproject.subproject_name
    project_name = Project.objects.get(id=project_id).project_name

    scenes = []
    for i in range(number_of_scenes):
        i=i+1
        scene_name = subproject.subproject_name+'-scena-'+str(i)
        obj,created = Scene.objects.update_or_create(
            project_id = project,
            subproject_id = subproject,
            scene_name = scene_name
        )
        scenes.append(obj)

    SceneFormSet = modelformset_factory(
        Scene,
        extra=0,
        exclude=('scene_name','project_id','subproject_id'))

    if request.method == 'POST':
        formset = SceneFormSet(request.POST,request.FILES,queryset = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id))
        if formset.is_valid():
            print(formset)
            formset.save()
    else:
        formset=SceneFormSet(queryset = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id))

    scenes_and_formset = zip(scenes,formset)

    leader_approved_text = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id,leader_approved_text=True).count()
    leader_approved_image = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id,leader_approved_image=True).count()
    client_approved_text = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id,client_approved_text=True).count()
    client_approved_image = Scene.objects.filter(project_id=project_id,subproject_id=subproject_id,client_approved_image=True).count()

    context = {
        'project_id':project_id,
        'subproject_id':subproject_id,
        'formset':formset,
        'scenes_and_formset':scenes_and_formset,
        'leader_approved_text':leader_approved_text,
        'leader_approved_image':leader_approved_image,
        'client_approved_text':client_approved_text,
        'client_approved_image':client_approved_image,
        'number_of_scenes':number_of_scenes,
        'subproject_name':subproject_name,
        'project_name':project_name
    }

    return render(request,'dashboard/subproject_dashboard.html',context)


def tasks(request):
    print(type(request.user))
    task_form = TaskForm()
    task_form.instance.user_id_id = request.user.id
   
    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        task_form.instance.user_id_id = request.user.id
        if task_form.is_valid():
            task_form.save()
            #print(request.POST['project_name'])
            #request.POST['project_name']
            #tu je spremljen podatak iz forme
            return redirect('tasks')
    
    tasks = Task.objects.all()
    users = User.objects.exclude(pk = request.user.id)

    loged_user = User.objects.get(pk=request.user.id)
    loged_tasks = Task.objects.filter(user_id = request.user.id)
    
    context = {
        'task_form':task_form,
        'users':users,
        'tasks':tasks,
        'users':users,
        'loged_user':loged_user,
        'loged_tasks':loged_tasks
    }
    return render(request,'dashboard/tasks.html',context)

def task_delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('tasks')

def tutorials(request):
    tutorial_form = TutorialForm()
    tutorial_form.instance.user_id_id = request.user.id

    if request.method == 'POST':
        tutorial_form = TutorialForm(data=request.POST)
        tutorial_form.instance.user_id_id = request.user.id
        if tutorial_form.is_valid():
            tutorial_form.save()
            return redirect('tutorials')


    tutorials = Tutorial.objects.all()
    context = {
        'tutorials':tutorials,
        'tutorial_form':tutorial_form,
    }
    return render(request,'dashboard/tutorials.html',context)

def tutorial_page(request,tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    context = {
        'tutorial':tutorial
    }


    return render(request,'dashboard/tutorial_page.html',context)

