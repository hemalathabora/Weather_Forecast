from django.urls import path
from .views import weather_view
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('weather/', weather_view, name='weather'),
    path('blog/', views.blog, name='blog'),
    path('feedback/', views.feedback, name='feedback'),
    path('otherservices/', views.otherservices, name='otherservices'),
    path('careerGuidence/', views.careerGuidence, name='careerGuidence'),
    path('advancedCareer/', views.advancedCareer, name='advancedCareer'),
    path ('disaster/', views.disaster_form_view, name='disaster-form'),
    path ('disaster/results/', views.disaster_results_view, name='disaster-results'),
    path('visionmission/',views.visionmission, name='visionmission'),
    path('blog2/',views.blog2,name='blog2'),
    path('weather/coordinates/', views.weather_by_coordinates, name='weather-by-coordinates'),
    path('weather-options/', views.weather_options, name='weather_options'),
 

]
