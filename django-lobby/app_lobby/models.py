from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    
    TotalTareasPendientes = models.IntegerField(default=0)
    TotalTareasEnProceso = models.IntegerField(default=0)
    TotalTareasCompletadas = models.IntegerField(default=0)

    TareasPendientes = models.ManyToManyField('Task', related_name='TareasPendientes')
    TareasEnProceso = models.ManyToManyField('Task', related_name='TareasEnProceso')
    TareasCompletadas = models.ManyToManyField('Task', related_name='TareasCompletadas')

    puntos = models.IntegerField(default=0)

    nivel = models.IntegerField(default=1)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this player."""
        return reverse('user-detail', args=[str(self.id)])
    
    def finish_Task(self, task):
        self.TotalTareasCompletadas += 1
        self.TotalTareasEnProceso -= 1
        self.TareasEnProceso.remove(task)
        self.TareasCompletadas.add(task)
        self.puntos += task.puntosDeExperiencia
        self.save()
    
    def añadir_puntos(self, puntos):
        self.puntos += puntos
        #definir los diferentes niveles
        if self.puntos >= 100:
            self.nivel = 2
        if self.puntos >= 500:
            self.nivel = 3
        if self.puntos >= 1000:
            self.nivel = 4
        if self.puntos >= 2000:
            self.nivel = 5
        if self.puntos >= 5000:
            self.nivel = 6
        self.save()

    def __str__(self):
        return f"{self.username}-{self.nivel}"

    
    
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    fecha = models.DateField(max_length=8, blank=False, null=True)
    hora = models.TimeField(max_length=8, blank=False, null=True)
    puntosDeExperiencia = models.IntegerField(default=0)
    location = models.CharField(max_length=100, blank=True, null=True)
    acompanantes = models.ManyToManyField(User, blank=True, related_name='acompañantes')
    # como asigno la tarea al usuario que la crea? 

    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador', default=1)

    """ enumeracion de status """
    class Status(models.TextChoices):
        TODO = 'TODO'
        DOING = 'DOING'
        DONE = 'DONE'
        PAUSED = 'PAUSED'
    
    status = models.CharField(max_length=6, choices=Status.choices, default=Status.TODO) 
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this task."""
        return reverse('task-detail', args=[str(self.id)])


class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    series = models.ManyToManyField('Serie', blank=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creadorEjercicio', default=1)

    def __str__(self):
        return f"{self.nombre}"
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this task."""
        return reverse('ejercicio-detail', args=[str(self.id)])


class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    repeticiones = models.IntegerField(default=0)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creadorSerie', default=1)
    
    def __str__(self):
        return f"{self.repeticiones} reps X {self.peso} kgs."
    
class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    creditos = models.IntegerField(default=0)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creadorAsignatura', default=1)

    def __str__(self):
        return f"{self.nombre}"

# clase que hereda de task
class TaskDeporte(Task):
    deporte = models.CharField(max_length=100, blank=False, null=False)
    ejercicios = models.ManyToManyField(Ejercicio, blank=True)
    tiempo = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.deporte} - {self.title}"
    
class TaskEstudio(Task):
    asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, null=True, blank=True)

    class tipoTarea(models.TextChoices):
        EXAMEN = 'EXAMEN'
        EJERCICIO = 'EJERCICIO'
        PRACTICA = 'PRACTICA'
        PRESENTACION = 'PRESENTACION'
        OTRA = 'OTRA'

    tipo = models.CharField(max_length=20, choices=tipoTarea.choices, default=tipoTarea.OTRA)

    def __str__(self):
        return f"{self.asignatura} - {self.tipo}"