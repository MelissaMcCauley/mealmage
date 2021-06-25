from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/',
							  blank=True)

	def __str__(self):
		return f'Profile for user {self.user.username}'

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

class MenuCalendarEntry(models.Model):
	menu_date = models.DateField(unique=True, null=True)
	breakfast_entree = models.CharField(max_length=200, blank=True)
	lunch_entree = models.CharField(max_length=200, blank=True)
	dinner_entree = models.CharField(max_length=200, blank=True)
	dessert = models.CharField(max_length=200, blank=True)


class DailyMenu(models.Model):
	"""A collection of dishes pulled from StoredDish for a certain date"""
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
	menu_date = models.DateField(auto_now_add=False, auto_now=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Daily Menus'

	def __str__(self):
		"""Return a string representation of the model"""
		return self.menu_date


class GroceryList(models.Model):
	"""A grocery list created by the user"""
	grocery_list_item = models.CharField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model"""
		return self.grocery_list_item






