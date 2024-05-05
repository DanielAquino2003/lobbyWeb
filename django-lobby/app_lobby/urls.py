from django.urls import path
from .views import AsignaturaListView, AsignaturaDetailView, AsignaturaCreateView, SerieCreateView, SerieDetailView, SerieListView, TaskListView, TaskDetailView, TaskCreateView, UserListView, UserDetailView, UserCreateView, EjercicioListView, EjercicioDetailView, EjercicioCreateView
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('ejercicios/', EjercicioListView.as_view(), name='ejercicio-list'),
    path('ejercicio/<int:pk>/', EjercicioDetailView.as_view(), name='ejercicio-detail'),
    path('ejercicio/create/', EjercicioCreateView.as_view(), name='ejercicio-create'),
    path('series/', SerieListView.as_view(), name='serie-list'),
    path('serie/<int:pk>/', SerieDetailView.as_view(), name='serie-detail'),
    path('serie/create/', SerieCreateView.as_view(), name='serie-create'),
    path('asignaturas/', AsignaturaListView.as_view(), name='asignatura-list'),
    path('asignatura/<int:pk>/', AsignaturaDetailView.as_view(), name='asignatura-detail'),
    path('asignatura/create/', AsignaturaCreateView.as_view(), name='asignatura-create'),
]