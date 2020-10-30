from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import StoredDish

def index(request):
	"""The home page for Meal Mage"""
	return render(request, 'mealmageapp/index.html')

@login_required
def options(request):
	"""Contains links to the Stored Dishes, Meal Planning, and Grocery List pages"""
	return render(request, 'mealmageapp/options.html')

@login_required
def meals(request):
	"""This page lists the titles of all meals currently stored by the user with
	links to be able to create, read, update, or delete a meal"""
	meals = StoredDish.objects.filter(owner=request.user)
	context = {'meals': meals}
	return render(request, 'mealmageapp/meals.html', context)

@login_required
def meal(request, meal_id):
	meal = StoredDish.objects.get(id=meal_id)
	context = {'meal': meal}
	return render(request, 'mealmageapp/meal.html', context)	

@login_required
def mealplanning(request):
	"""Lets users create a meal plan from their stored dishes"""
	return render(request, 'mealmageapp/mealplanning.html')

@login_required
def grocerylist(request):
	"""Lets users pull meal ingredients from their meal plan to a grocery list
	and also add any other items so they can use it as a master grocery list"""
	return render(request, 'mealmageapp/grocerylist.html')




