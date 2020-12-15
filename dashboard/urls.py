from django.urls import path
from . import views
"""
urlpatterns = [
    path('', views.projects,name='homepage'),
    path('tutorials/',views.tutorials,name='tutorials'),
    path('<int:pk>/',views.project_page,name='project_page'),
    path('<int:pk>/<int:klj>',views.lesson_dashboard,name='lesson_dashboard'),
]
"""

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('<int:project_id>/',views.project_dashboard,name='project_dashboard'),
    path('<int:project_id>/<int:subproject_id>/',views.subproject_dashboard,name='subproject_dashboard'),
    path('tasks/',views.tasks,name='tasks'),
    path('tasks/<int:pk>/delete/',views.task_delete,name='task_delete'),
    path('tutorials/',views.tutorials,name='tutorials'),
    path('tutorials/<int:tutorial_id>/',views.tutorial_page,name='tutorial_page')
]