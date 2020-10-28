from django.db import models
from django.contrib.auth.models import User

class StoredDish(models.Model):
	"""A particular dish that has been added by the user to their account"""
	dish_title = models.CharField(max_length=200) # required
	dish_type = models.CharField(max_length=20) # required - options provided in drop down such as "entree", "side", "dessert", "appetizer"
	meal_type = models.CharField(max_length=20, blank=True) # required - will use labels like Breakfast, Lunch, Dinner, Brunch, Snack
	cuisine_type = models.CharField(max_length=50, blank=True) # optional - (e.g. Italian, Korean, Indian...etc.) 
	ingredient = models.CharField(max_length=50, blank=True) # optional - block of text or separate field for each ingredient?
	recipe = models.TextField(blank=True) # optional - block of text or separate field for each step?
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Stored Dishes'

	def __str__(self):
		"""Return a string representation of the model"""
		return self.dish_title


# class MealPlan(models.Model):
# 	"""A collection of meals pulled from StoredDish for a certain period of time"""
# 	meal_plan_dish_title = models.ForeignKey(StoredDish, 
# 		on_delete=models.CASCADE)


# 	def __str__(self):
# 		"""Return a string representation of the model"""
# 		return self.meal_plan_dish_title	


# class GroceryList(models.Model):
# 	"""A grocery list created by the user"""
# 	grocery_list_item = models.CharField(max_length=100)
# 	owner = models.ForeignKey(User, on_delete=models.CASCADE)

# 	def __str__(self):
# 		"""Return a string representation of the model"""
# 		return self.grocery_list_item






