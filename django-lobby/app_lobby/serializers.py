from rest_framework import serializers
from .models import Task, TaskDeporte, TaskEstudio, Serie, Ejercicio, Asignatura, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDeporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDeporte
        fields = '__all__'

class TaskEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEstudio
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'