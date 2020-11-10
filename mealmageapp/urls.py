"""Defines URL patterns for mealmageapp"""

from django.urls import path

from . import views

app_name = 'mealmageapp'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	# Options page that comes up after logging in
	path('options/', views.options, name='options'),

	# Meals page that is linked from Options
	path('meals/', views.meals, name='meals'),

	path('mealplanning/', views.mealplanning, name='mealplanning'),

	path('grocerylist/', views.grocerylist, name='grocerylist'),

	path('meals/<int:meal_id>/', views.meal_detail, name='meal_detail'),

	path('addmeal/', views.addmeal, name='addmeal'),
]