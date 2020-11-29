from django.db import models
from django.contrib.auth.models import User



class StoredDish(models.Model):
	"""A particular dish that has been added by the user to their account"""
	DISH_TYPE_CHOICES = [
		('entree', 'Entree'),
		('side', 'Side'),
		('appetizer', 'Appetizer'),
		('dessert', 'Dessert'),
	]
	MEAL_TYPE_CHOICES = [
		('breakfast', 'Breakfast'),
		('brunch', 'Brunch'),
		('lunch', 'Lunch'),
		('dinner', 'Dinner'),
	]
	CUISINE_TYPE_CHOICES = [
		('american', 'American'),
		('italian', 'Italian'),
		('korean', 'Korean'),
		('indian', 'Indian'),
		('ethiopian', 'Ethiopian'),
		('vietnamese', 'Vietnamese'),
		('thai', 'Thai'),
		('sushi', 'Sushi'),
		('panasian', 'Pan Asian'),
		('mexican', 'Mexican'),
		('german', 'German'),
		('japanese', 'Japanese'),
		('cajun', 'Cajun'),
		('texmex', 'Texmex'),
		('greek', 'Greek'),
		('mediterranean', 'Mediterranean'),
		('french', 'French'),
		('southern', 'Southern'),
		('spanish', 'Spanish'),
		('other', 'Other'),
	]
	dish_title = models.CharField(max_length=200) # required
	dish_type = models.CharField(max_length=20, choices=DISH_TYPE_CHOICES) # required 
	meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES) # required
	cuisine_type = models.CharField(max_length=50, blank=True, choices=CUISINE_TYPE_CHOICES) # optional
	ingredient01 = models.CharField(max_length=50, blank=True) # optional
	ingredient02 = models.CharField(max_length=50, blank=True) # optional
	ingredient03 = models.CharField(max_length=50, blank=True) # optional
	ingredient04 = models.CharField(max_length=50, blank=True) # optional
	ingredient05 = models.CharField(max_length=50, blank=True) # optional
	ingredient06 = models.CharField(max_length=50, blank=True) # optional
	ingredient07 = models.CharField(max_length=50, blank=True) # optional
	ingredient08 = models.CharField(max_length=50, blank=True) # optional
	ingredient09 = models.CharField(max_length=50, blank=True) # optional
	ingredient10 = models.CharField(max_length=50, blank=True) # optional
	ingredient11 = models.CharField(max_length=50, blank=True) # optional
	ingredient12 = models.CharField(max_length=50, blank=True) # optional
	ingredient13 = models.CharField(max_length=50, blank=True) # optional
	ingredient14 = models.CharField(max_length=50, blank=True) # optional
	ingredient15 = models.CharField(max_length=50, blank=True) # optional
	recipe = models.TextField(blank=True) # optional - block of text or separate field for each step?
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Stored Dishes'

	def __str__(self):
		"""Return a string representation of the model"""
		return self.dish_title


class DailyMenu(models.Model):
	"""A collection of dishes pulled from StoredDish for a certain period of time"""
	breakfast_dish_entree = models.CharField(max_length=200, blank=True)
	breakfast_dish_side_1 = models.CharField(max_length=200, blank=True)
	breakfast_dish_side_2 = models.CharField(max_length=200, blank=True)
	breakfast_dish_side_3 = models.CharField(max_length=200, blank=True)
	lunch_dish_entree = models.CharField(max_length=200, blank=True)
	lunch_dish_side_1 = models.CharField(max_length=200, blank=True)
	lunch_dish_side_2 = models.CharField(max_length=200, blank=True)
	lunch_dish_side_3 = models.CharField(max_length=200, blank=True)
	dinner_dish_entree = models.CharField(max_length=200, blank=True)
	dinner_dish_side_1 = models.CharField(max_length=200, blank=True)
	dinner_dish_side_2 = models.CharField(max_length=200, blank=True)
	dinner_dish_side_3 = models.CharField(max_length=200, blank=True)
	dessert_dish = models.CharField(max_length=200, blank=True)
	snack_dish_1 = models.CharField(max_length=200, blank=True)
	snack_dish_2 = models.CharField(max_length=200, blank=True)
	snack_dish_3 = models.CharField(max_length=200, blank=True)
	meal_plan_date = models.DateField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)	


class GroceryList(models.Model):
	"""A grocery list created by the user"""
	grocery_list_item = models.CharField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.grocery_list_item






