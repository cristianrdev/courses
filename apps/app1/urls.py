from django.urls import path     
from . import views
urlpatterns = [
    path('', views.courses),
    path('courses/destroy/<int:id>', views.destroy),


]