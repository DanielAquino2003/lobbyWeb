from django.shortcuts import render
from .models import Task, User, Ejercicio, Serie, Asignatura, TaskDeporte, TaskEstudio
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render()

# Views for Study Tasks ---------------------------------------------------------------------------------------

class TaskEstudioListView(ListView):
    model = TaskEstudio
    ordering = ['id']

class TaskEstudioCreateView(CreateView):
    model = TaskEstudio
    fields = ['title', 'description', 'fecha', 'hora', 'puntosDeExperiencia', 'acompanantes', 'status', 'asignatura', 'tipo']

class TaskEstudioDetailView(DetailView):
    model = TaskEstudio

# Views for Sport Tasks ---------------------------------------------------------------------------------------

class TaskDeporteListView(ListView):
    model = TaskDeporte
    ordering = ['id']

class TaskDeporteCreateView(CreateView):
    model = TaskDeporte
    fields = ['title', 'description', 'fecha', 'hora', 'puntosDeExperiencia', 'acompanantes', 'status', 'deporte', 'ejercicios', 'tiempo']

class TaskDeporteDetailView(DetailView):
    model = Task
    
# Views for Generic Tasks ---------------------------------------------------------------------------------------

class TaskListView(ListView):
    model = Task
    ordering = ['id']

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'fecha', 'hora', 'puntosDeExperiencia', 'acompanantes', 'status']

# Views for Users ---------------------------------------------------------------------------------------

class UserListView(ListView):
    model = User
    ordering = ['id']

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']


# Views for Exercises ---------------------------------------------------------------------------------------

class EjercicioListView(ListView):
    model = Ejercicio
    ordering = ['id']

class EjercicioDetailView(DetailView):
    model = Ejercicio

class EjercicioCreateView(CreateView):
    model = Ejercicio
    fields = ['nombre', 'series']


# Views for Series ---------------------------------------------------------------------------------------

class SerieListView(ListView):
    model = Serie
    ordering = ['id']

class SerieDetailView(DetailView):
    model = Serie

class SerieCreateView(CreateView):
    model = Serie
    fields = ['nombre', 'repeticiones']

# Views for Subjects ---------------------------------------------------------------------------------------

class AsignaturaListView(ListView):
    model = Asignatura
    ordering = ['id']

class AsignaturaDetailView(DetailView):
    model = Asignatura

class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = ['nombre', 'creditos']

# Create your views here.
