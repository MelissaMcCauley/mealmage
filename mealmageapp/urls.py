"""Defines URL patterns for mealmageapp"""

from django.urls import path
from . import views

app_name = 'mealmageapp'

urlpatterns = [
	# Home page
	path('', views.index, name='index'),

	# Options page that comes up after logging in
	path('options/', views.options, name='options'),

	# Dishes page that is linked from Options
	path('dishes/', views.dishes, name='dishes'),

	# Your Menus page that is linked from Options
	path('menus/', views.menus, name='menus'),

	path('grocerylist/', views.grocerylist, name='grocerylist'),

	path('<int:dish_id>/', views.dish_detail, name='dish_detail'),

	path('newdish/', views.newdish, name='newdish'),

	path('<int:dish_id>/updatedish/', views.updatedish, name='updatedish'),

	path('<int:dish_id>/dish_delete/', views.dish_delete, name='dish_delete'),


	]