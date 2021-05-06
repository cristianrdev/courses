from django.shortcuts import render, HttpResponse, redirect
from .models import Course, Description
# from datetime import date
from django.contrib import messages

# Create your views here.

def courses(request):
    if request.method == 'GET':
        print('ES UN GET')
        context = {
            "courses" : Course.objects.all(),
            
        }
        return render(request, 'courses.html', context)

    else:
        print('ES UN POST')
        errors = Course.objects.validator(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
        
            new_course = Course.objects.create(
            name= request.POST['nombre'],
                    )
            
            new_description = Description.objects.create(
            description= request.POST['descripcion'],
            courses = new_course,
                    )
            print("--Guardado con exito---"*5)
            # asocia el comentario al curso
            # new_course.Course.add(new_description)
            return redirect('/')


def destroy(request, id):
    if request.method == 'GET':
        context ={
            "course" : Course.objects.get(id=id)
        }
        return render(request, 'delete.html', context)
    else:
        print('ES UN POST')
        print('BORRANDO CURSO')
        course_to_delete = Course.objects.get(id=id)
        course_to_delete.delete()
        return redirect('/')

