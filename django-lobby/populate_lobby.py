import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lobby.settings")
import datetime


import django
django.setup()

from app_lobby.models import Task, User, Ejercicio, Serie, Asignatura, TaskDeporte, TaskEstudio

def populate():

    series = [
        {"repeticiones": 10, "peso": 10, "creador": 1},
        {"repeticiones": 10, "peso": 10, "creador": 2},
        {"repeticiones": 10, "peso": 10, "creador": 3},
    ]

    ejercicios = [
        {"nombre": "Flexiones", "series": [1, 1, 1], "creador": 1},
        {"nombre": "Dominadas", "series": [1, 1, 1], "creador": 1},
        {"nombre": "Extensiones Cuadriceps", "series": [1, 1, 1], "creador": 1},
        {"nombre": "Abdominales", "series": [2, 2, 2], "creador": 2},
        {"nombre": "Curl de Biceps", "series": [2, 2, 2], "creador": 2},
        {"nombre": "Press Militar", "series": [2, 2, 2], "creador": 2},
        {"nombre": "Press Banca", "series": [3, 3, 3, 3], "creador": 3},
        {"nombre": "Sentadilla", "series": [3, 3, 3, 3], "creador": 3},
        {"nombre": "Peso Muerto", "series": [3, 3, 3, 3], "creador": 3},
    ]

    asignaturas = [
        {"nombre": "Matematicas", "creditos": 6, "creador": 1},
        {"nombre": "Fisica", "creditos": 6, "creador": 1},
        {"nombre": "Quimica", "creditos": 6, "creador": 1},
        {"nombre": "Biologia", "creditos": 6, "creador": 1},
        {"nombre": "Historia", "creditos": 6, "creador": 1},
        {"nombre": "Geografia", "creditos": 6, "creador": 1},
        {"nombre": "Ingles", "creditos": 6, "creador": 1},
        {"nombre": "Frances", "creditos": 6, "creador": 1},
        {"nombre": "Aleman", "creditos": 6, "creador": 1},
        {"nombre": "Matematicas", "creditos": 6, "creador": 2},
        {"nombre": "Fisica", "creditos": 6, "creador": 2},
        {"nombre": "Quimica", "creditos": 6, "creador": 2},
        {"nombre": "Biologia", "creditos": 6, "creador": 2},
        {"nombre": "Historia", "creditos": 6, "creador": 2},
        {"nombre": "Geografia", "creditos": 6, "creador": 2},
        {"nombre": "Ingles", "creditos": 6, "creador": 2},
        {"nombre": "Frances", "creditos": 6, "creador": 2},
        {"nombre": "Aleman", "creditos": 6, "creador": 2},
        {"nombre": "Matematicas", "creditos": 6, "creador": 3},
        {"nombre": "Fisica", "creditos": 6, "creador": 3},
        {"nombre": "Quimica", "creditos": 6, "creador": 3},
        {"nombre": "Biologia", "creditos": 6, "creador": 3},
        {"nombre": "Historia", "creditos": 6, "creador": 3},
        {"nombre": "Geografia", "creditos": 6, "creador": 3},
        {"nombre": "Ingles", "creditos": 6, "creador": 3},
        {"nombre": "Frances", "creditos": 6, "creador": 3},
        {"nombre": "Aleman", "creditos": 6, "creador": 3},
        {"nombre": "Matematicas", "creditos": 6, "creador": 4},
        {"nombre": "Fisica", "creditos": 6, "creador": 4},
        {"nombre": "Quimica", "creditos": 6, "creador": 4},
        {"nombre": "Biologia", "creditos": 6, "creador": 4},
        {"nombre": "Historia", "creditos": 6, "creador": 4},
        {"nombre": "Geografia", "creditos": 6, "creador": 4},
        {"nombre": "Ingles", "creditos": 6, "creador": 4},
        {"nombre": "Frances", "creditos": 6, "creador": 4},
        {"nombre": "Aleman", "creditos": 6, "creador": 4},
    ]

    users = [
        {"username": "user1", "email": "user1@gmail.com", "password": "1234", "TotalTareasPendientes": 0, "TotalTareasEnProceso": 0, "TotalTareasCompletadas": 0 ,"TareasPendiantes": [], "TareasCompletadas": [], "TareasEnProceso": [], "puntos": 0, "nivel": 1},
        {"username": "user2", "email": "user2@gmail.com", "password": "4567", "TotalTareasPendientes": 0, "TotalTareasEnProceso": 0, "TotalTareasCompletadas": 0 ,"TareasPendiantes": [], "TareasCompletadas": [], "TareasEnProceso": [], "puntos": 0, "nivel": 1},
        {"username": "user3", "email": "user3@gmail.com", "password": "7890", "TotalTareasPendientes": 0, "TotalTareasEnProceso": 0, "TotalTareasCompletadas": 0 ,"TareasPendiantes": [], "TareasCompletadas": [], "TareasEnProceso": [], "puntos": 0, "nivel": 1},
        {"username": "user4", "email": "user4@gmail.com", "password": "0987", "TotalTareasPendientes": 0, "TotalTareasEnProceso": 0, "TotalTareasCompletadas": 0 ,"TareasPendiantes": [], "TareasCompletadas": [], "TareasEnProceso": [], "puntos": 0, "nivel": 1},
    ]

    tasksDeporte = [
        {"title": "Correr 5km", "description": "Correr 5km en menos de 30 minutos", "fecha": "1920-01-02", "hora": "12:00", "puntosDeExperiencia": 100, "location": "Parque", "acompanantes": [2, 3], "creador": 1, "status": "TODO", "deporte": "Correr", "ejercicios": [1, 2, 3], "tiempo": 30.00},
        {"title": "Correr 10km", "description": "Correr 10km en menos de 1 hora", "fecha": "1920-01-02", "hora": "12:00", "puntosDeExperiencia": 200, "location": "Parque", "acompanantes": [3], "creador": 2, "status": "TODO", "deporte": "Correr", "ejercicios": [4, 5, 6], "tiempo": 60.00},
        {"title": "Correr 15km", "description": "Correr 15km en menos de 1 hora y 30 minutos", "fecha": "1920-01-02", "hora": "12:00", "puntosDeExperiencia": 300, "location": "Parque", "acompanantes": [1, 2], "creador": 3, "status": "TODO", "deporte": "Correr", "ejercicios": [7, 8, 9, 10], "tiempo": 90.00},
        {"title": "Nadar 1km", "description": "Nadar 1km en menos de 30 minutos", "fecha": "1920-01-02", "hora": "12:00", "puntosDeExperiencia": 100, "location": "Piscina", "acompanantes": [2, 3], "creador": 1, "status": "TODO", "deporte": "Natacion", "ejercicios": [1, 2, 3], "tiempo": 30.00},
    ]

    tasksEstudio = [
        {"title": "Estudiar Matematicas", "description": "Estudiar Matematicas para el examen", "fecha": "1920-01-02", "hora":"12:00", "puntosDeExperiencia": 100, "location": "Biblioteca", "acompanantes": [2, 3], "creador": 1, "status": "TODO", "asignatura": 1, "tipo": "Estudio"},
        {"title": "Estudiar Fisica", "description": "Estudiar Fisica para el examen", "fecha": "1920-01-02", "hora":"12:00", "puntosDeExperiencia": 200, "location": "Biblioteca", "acompanantes": [3], "creador": 2, "status": "TODO", "asignatura": 2, "tipo": "Estudio"},
        {"title": "Estudiar Quimica", "description": "Estudiar Quimica para el examen", "fecha": "1920-01-02", "hora":"12:00", "puntosDeExperiencia": 300, "location": "Biblioteca", "acompanantes": [1, 2], "creador": 3, "status": "TODO", "asignatura": 3, "tipo": "Estudio"},
        {"title": "Estudiar Biologia", "description": "Estudiar Biologia para el examen", "fecha": "1920-01-02", "hora":"12:00", "puntosDeExperiencia": 100, "location": "Biblioteca", "acompanantes": [2, 3], "creador": 1, "status": "TODO", "asignatura": 4, "tipo": "Estudio"},
    ]

    for user in users:
        u = User.objects.get_or_create(username=user["username"], email=user["email"], password=user["password"], TotalTareasPendientes=user["TotalTareasPendientes"], TotalTareasEnProceso=user["TotalTareasEnProceso"], TotalTareasCompletadas=user["TotalTareasCompletadas"], puntos=user["puntos"], nivel=user["nivel"])[0]
        u.save()

    for serie in series:
        creador = User.objects.get(id=serie["creador"])
        s = Serie.objects.get_or_create(repeticiones=serie["repeticiones"], peso=serie["peso"], creador=creador)[0]
        s.save()

    for ejercicio_data in ejercicios:
        nombre = ejercicio_data["nombre"]
        series_ids = ejercicio_data["series"]
        creador_id = ejercicio_data["creador"]
        series = Serie.objects.filter(id__in=series_ids)
        creador = User.objects.get(id=creador_id)
        e = Ejercicio.objects.get_or_create(nombre=nombre,creador=creador)[0]
        e.save()
        for s in series:
            e.series.add(s)

    for asignatura in asignaturas:
        creador = User.objects.get(id=asignatura["creador"])
        a = Asignatura.objects.get_or_create(nombre=asignatura["nombre"], creditos=asignatura["creditos"], creador=creador)[0]
        a.save()

    for task in tasksDeporte:
        creador = User.objects.get(id=task["creador"])
        acompanantes_ids = task["acompanantes"]
        t = TaskDeporte.objects.get_or_create(title=task["title"], description=task["description"], fecha=task["fecha"], hora=task["hora"], puntosDeExperiencia=task["puntosDeExperiencia"], location=task["location"], creador=creador, status=task["status"], deporte=task["deporte"], tiempo=task["tiempo"])[0]
        t.save()
        for id in acompanantes_ids:
            acompanante = User.objects.get(id=id)
            t.acompanantes.add(acompanante)

    for task in tasksEstudio:
        creador = User.objects.get(id=task["creador"])
        acompanantes_ids = task["acompanantes"]
        asignaturas = task["asignatura"]
        asignatura = Asignatura.objects.get(id=asignaturas)
        t = TaskEstudio.objects.get_or_create(title=task["title"], description=task["description"], fecha=task["fecha"], hora=task["hora"], puntosDeExperiencia=task["puntosDeExperiencia"], location=task["location"], creador=creador,asignatura=asignatura, status=task["status"],tipo=task["tipo"])[0]
        t.save()
        for id in acompanantes_ids:
            acompanante = User.objects.get(id=id)
            t.acompanantes.add(acompanante)

if __name__ == "__main__":
    print("Starting lobby population script...")
    populate()
    print("lobby population script finished!")
