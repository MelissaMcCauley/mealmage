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
def addmeal(request):
	"""Allows user to add a new dish to their account"""
	if request.method != 'POST':
		# No data submitted, create a blank form
		form = StoredDishForm()
	else:
		# POST data submitted; process the data
		form = StoredDishForm(data=request.POST)
		if form.is_valid():
			new_meal = form.save()
			new_meal.save()
			return HttpResponseRedirect(reverse('mealmageapp:meals'))

	context = {'form': form}
	return render(request, 'mealmageapp/addmeal.html', context)

@login_required
def meal_detail(request, meal_id): # how do I display all the values for each attribute in StoredDish?
	meal = StoredDish.objects.get(id=meal_id)
	context = {'meal': meal}
	return render(request, 'mealmageapp/meal_detail.html', context)	

@login_required
def mealplanning(request):
	"""Lets users create a meal plan from their stored dishes"""
	return render(request, 'mealmageapp/mealplanning.html')

@login_required
def grocerylist(request):
	"""Lets users pull meal ingredients from their meal plan to a grocery list
	and also add any other items so they can use it as a master grocery list"""
	return render(request, 'mealmageapp/grocerylist.html')




