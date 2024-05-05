from django.contrib import admin
from .models import User, Task, Ejercicio, Serie, Asignatura, TaskDeporte, TaskEstudio

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Ejercicio)
admin.site.register(Serie)
admin.site.register(Asignatura)
admin.site.register(TaskEstudio)
admin.site.register(TaskDeporte)