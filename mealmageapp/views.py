from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import StoredDish
from .forms import StoredDishForm

def index(request):
	"""The home page for Meal Mage"""
	return render(request, 'mealmageapp/index.html')

@login_required
def options(request):
	"""Contains links to the Stored Dishes, Meal Planning, and Grocery List pages"""
	return render(request, 'mealmageapp/options.html')

@login_required
def dishes(request):
	"""This page lists the titles of all meals currently stored by the user with
	links to be able to create, read, update, or delete a meal"""
	dishes = StoredDish.objects.filter(owner=request.user)
	context = {'dishes': dishes}
	return render(request, 'mealmageapp/dishes.html', context)

@login_required
def newdish(request):
	"""Allows user to add a new dish to their account"""
	if request.method != 'POST':
		# No data submitted, create a blank form
		form = StoredDishForm()
	else:
		# POST data submitted; process the data
		form = StoredDishForm(data=request.POST)
		if form.is_valid():
			new_dish = form.save(commit=False)
			new_dish.owner = request.user
			new_dish.save()
			return redirect('mealmageapp:dishes')

	context = {'form': form}
	return render(request, 'mealmageapp/newdish.html', context)

@login_required
def dish_detail(request, dish_id):
	dish = StoredDish.objects.get(id=dish_id)
	context = {'dish': dish}
	return render(request, 'mealmageapp/dish_detail.html', context)

@login_required
def dish_delete(request, dish_id):
	dish = StoredDish.objects.get(id=dish_id)
	if request.method == 'POST':
		dish.delete()
		return redirect('mealmageapp:dishes')
	context = {'dish': dish}
	return render(request, 'mealmageapp/dish_delete.html', context)	

@login_required
def mealplanning(request):
	"""Lets users create a meal plan from their stored dishes"""
	return render(request, 'mealmageapp/mealplanning.html')

@login_required
def grocerylist(request):
	"""Lets users pull meal ingredients from their meal plan to a grocery list
	and also add any other items so they can use it as a master grocery list"""
	return render(request, 'mealmageapp/grocerylist.html')




