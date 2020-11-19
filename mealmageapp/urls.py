"""Defines URL patterns for mealmageapp"""

from django.urls import path

from . import views

from .views import DishDelete

app_name = 'mealmageapp'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	# Options page that comes up after logging in
	path('options/', views.options, name='options'),

	# Meals page that is linked from Options
	path('dishes/', views.dishes, name='dishes'),

	path('mealplanning/', views.mealplanning, name='mealplanning'),

	path('grocerylist/', views.grocerylist, name='grocerylist'),

	path('<int:dish_id>/', views.dish_detail, name='dish_detail'),

	path('newdish/', views.newdish, name='newdish'),

	# path('<int:dish_id>/update_dish/', views.update_dish, name='dish_delete') ---??

	path('<pk>/delete/', DishDelete.as_view(), name='dish_delete'),


]