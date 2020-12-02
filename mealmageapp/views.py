from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from datetime import datetime, date

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
def updatedish(request, dish_id):
	dish = StoredDish.objects.get(id=dish_id)

	if request.method != 'POST':
		# No data submitted, create a blank form
		form = StoredDishForm(instance=dish)
	else:
		# POST data submitted; process the data
		form = StoredDishForm(instance=dish, data=request.POST)
		if form.is_valid():
			updated_dish = form.save(commit=False)
			updated_dish.owner = request.user
			updated_dish.save()
			return HttpResponseRedirect(reverse('mealmageapp:dish_detail',
			 args=[dish.id]))

	context = {'dish': dish, 'form': form}
	return render(request, 'mealmageapp/updatedish.html', context)	


@login_required
def dish_delete(request, dish_id):
	dish = StoredDish.objects.get(id=dish_id)
	if request.method == 'POST':
		dish.delete()
		return redirect('mealmageapp:dishes')
	context = {'dish': dish}
	return render(request, 'mealmageapp/dish_delete.html', context)	

@login_required
def daily_menu(request):
	"""Displays menus a user has created from their stored dishes, 
		one week at a time"""
	# need to display current week based on current date
	
	day_of_week = datetime.now().weekday()
	today = datetime.now().toordinal()
	if day_of_week == 6:
		sun_date = datetime.now().strftime("%m/%d/%Y")
	if day_of_week == 0:
		sun_date_ord = today - 1
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")
	if day_of_week == 1:
		sun_date_ord = today - 2
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")
	if day_of_week == 2:
		sun_date_ord = today - 3
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")
	if day_of_week == 3:
		sun_date_ord = today - 4
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")
	if day_of_week == 4:
		sun_date_ord = today - 5
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")
	if day_of_week == 5:
		sun_date_ord = today - 6
		sun_date = date.fromordinal(sun_date_ord).strftime("%m/%d/%Y")

	mon_date_ord = sun_date_ord + 1
	mon_date = date.fromordinal(mon_date_ord).strftime("%m/%d/%Y")
	tue_date_ord = sun_date_ord + 2
	tue_date = date.fromordinal(tue_date_ord).strftime("%m/%d/%Y")
	wed_date_ord = sun_date_ord + 3
	wed_date = date.fromordinal(wed_date_ord).strftime("%m/%d/%Y")
	thu_date_ord = sun_date_ord + 4
	thu_date = date.fromordinal(thu_date_ord).strftime("%m/%d/%Y")
	fri_date_ord = sun_date_ord + 5
	fri_date = date.fromordinal(fri_date_ord).strftime("%m/%d/%Y")
	sat_date_ord = sun_date_ord + 6
	sat_date = date.fromordinal(sat_date_ord).strftime("%m/%d/%Y")
	context = {"sun_date": sun_date, "mon_date": mon_date, 
	"tue_date": tue_date, "wed_date": wed_date, "thu_date": thu_date,
	"fri_date": fri_date, "sat_date": sat_date}
	return render(request, 'mealmageapp/daily_menu.html', context)

@login_required
def grocerylist(request):
	"""Lets users pull meal ingredients from their meal plan to a grocery list
	and also add any other items so they can use it as a master grocery list"""
	return render(request, 'mealmageapp/grocerylist.html')




