from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        print(postData['nombre'])
        if len(postData['nombre'])<5:
            errors['nombre'] = "El nombre del curso debe ser al menos de 5 caracteres"
        if len(postData['descripcion'])<14:
            errors['descripcion'] = "La descripción debe tener al menos 15 caracteres"
        if postData['nuevo'] == "True":
            for s in Course.objects.all():
                # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
                if postData['nombre'].lower() == s.name.lower(): 
                    errors['nombre'] = "Este curso ya existe"
        return errors





class Course(models.Model):
    name = models.CharField(max_length=255)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()



# class DescriptionManager(models.Manager):
#     def validator(self, postData):
#         errors = {}

#         return errors
        


class Description(models.Model):
    description = models.TextField()
    courses = models.OneToOneField(Course, on_delete = models.CASCADE)
    objects = CourseManager()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    

