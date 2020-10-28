from django import forms

from .models import StoredDish

class StoredDishForm(forms.ModelForm):
	class Meta:
		model = StoredDish
		fields = ['dish_title', 'meal_type', 'dish_type', 'cuisine_type', 
					'ingredient', 'recipe']
		labels = {'dish_title':'Dish Name',
				  'dish_type':'Type of Dish',
				  'meal_type':'Type of Meal',
				  'cuisine_type':'Cuisine Type',
				  'ingredient':'Ingredient',
				  'recipe':'Recipe',	
					}


# class GroceryListForm(forms.ModelForm):
# 	class Meta:
# 		model = GroceryList
# 		fields = ['grocery_list_item']
# 		labels = {'grocery_list_item':'Grocery Item'}


# class MealPlanForm(forms.ModelForm):
# 	class Meta:
# 		model = MealPlan
# 		fields = ['meal_plan_dish_title']
# 		labels = {'meal_plan_dish_title':'Dish Name'}			