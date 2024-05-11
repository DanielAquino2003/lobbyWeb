from djoser.views import TokenCreateView
from djoser.conf import settings
from rest_framework import mixins, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, TaskDeporte, TaskEstudio, Serie, Ejercicio, Asignatura
from .serializers import TaskSerializer, TaskDeporteSerializer, TaskEstudioSerializer, SerieSerializer, EjercicioSerializer, AsignaturaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class MyTokenCreateView(TokenCreateView):
    def _action(self, serializer):
        response = super()._action(serializer)
        tokenString = response.data['auth_token']
        tokenObject = settings.TOKEN_MODEL.objects.get(key=tokenString)
        response.data['user_id'] = tokenObject.user_id
        return response
    
class TaskViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(creador=self.request.user)

    def list(self, request):
        """ queryset = self.queryset.filter(creador=request.user) """
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't delete this task")
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't update this task")
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class TaskDeporteViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TaskDeporteSerializer
    def get_queryset(self):
        return TaskDeporte.objects.filter(creador=self.request.user)

    def list(self, request):
        """ queryset = self.queryset.filter(creador=request.user) """
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't delete this task")
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't update this task")
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class TaskEstudioViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = TaskEstudioSerializer
    def get_queryset(self):
        return TaskEstudio.objects.filter(creador=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't delete this task")
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        if task.creador != request.user:
            raise ValidationError("You can't update this task")
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class SubjectViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = AsignaturaSerializer
    def get_queryset(self):
        return Asignatura.objects.filter(creador=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        subject = get_object_or_404(self.get_queryset(), pk=pk)
        if subject.creador != request.user:
            raise ValidationError("You can't delete this subject")
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        subject = get_object_or_404(self.get_queryset(), pk=pk)
        if subject.creador != request.user:
            raise ValidationError("You can't update this subject")
        serializer = self.serializer_class(subject, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class EjercicioViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = EjercicioSerializer
    def get_queryset(self):
        return Ejercicio.objects.filter(creador=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        ejercicio = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        ejercicio = get_object_or_404(self.get_queryset(), pk=pk)
        if ejercicio.creador != request.user:
            raise ValidationError("You can't delete this subject")
        ejercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        ejercicio = get_object_or_404(self.get_queryset(), pk=pk)
        if ejercicio.creador != request.user:
            raise ValidationError("You can't update this subject")
        serializer = self.serializer_class(ejercicio, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class SerieViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):

    serializer_class = SerieSerializer
    def get_queryset(self):
        return Serie.objects.filter(creador=self.request.user)

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serie = serializer.save(creador=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        serie = get_object_or_404(self.get_queryset(), pk=pk)
        if serie.creador != request.user:
            raise ValidationError("You can't delete this subject")
        serie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk=None):
        serie = get_object_or_404(self.get_queryset(), pk=pk)
        if serie.creador != request.user:
            raise ValidationError("You can't update this subject")
        serializer = self.serializer_class(serie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
