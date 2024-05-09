from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .api import TaskViewSet, TaskDeporteViewSet, TaskEstudioViewSet, SubjectViewSet, EjercicioViewSet, SerieViewSet

urlpatterns = [
    path('tasks/',TaskViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
    path('tasks/<int:pk>/',TaskViewSet.as_view({'delete': 'destroy'})),
    path('tasksDeporte/',TaskDeporteViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
    path('tasksDeporte/<int:pk>/',TaskDeporteViewSet.as_view({'delete': 'destroy'})),
    path('tasksEstudio/', TaskEstudioViewSet.as_view({'get':'list', 'put':'update', 'post':'create'})),
    path('taskEstudio/<int:pk>/', TaskEstudioViewSet.as_view({'delete':'destroy'})),
    path('asignaturas/', SubjectViewSet.as_view({'get':'list', 'put':'update', 'post':'create'})),
    path('asignatura/<int:pk>/', SubjectViewSet.as_view({'delete':'destroy'})),
    path('ejercicios/', EjercicioViewSet.as_view({'get':'list', 'put':'update', 'post':'create'})),
    path('ejercicio/<int:pk>/', EjercicioViewSet.as_view({'delete':'destroy'})),
    path('series/', SerieViewSet.as_view({'get':'list', 'put':'update', 'post':'create'})),
    path('serie/<int:pk>/', SerieViewSet.as_view({'delete':'destroy'})),

]