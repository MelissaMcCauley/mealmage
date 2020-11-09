from django.forms import ModelForm

from .models import StoredDish

class StoredDishForm(ModelForm):
	class Meta:
		model = StoredDish
		fields = ['dish_title', 'meal_type', 'dish_type', 'cuisine_type', 
					'ingredient01','ingredient02','ingredient03',
					'ingredient04','ingredient05','ingredient06',
					'ingredient07','ingredient08','ingredient09',
					'ingredient10','ingredient11','ingredient12',
					'ingredient13','ingredient14','ingredient15','recipe']
		labels = {'dish_title':'Dish Name',
				  'dish_type':'Type of Dish',
				  'meal_type':'Type of Meal',
				  'cuisine_type':'Cuisine Type',
				  'ingredient01':'Ingredient 1',
				  'ingredient02':'Ingredient 2',
				  'ingredient03':'Ingredient 3',
				  'ingredient04':'Ingredient 4',
				  'ingredient05':'Ingredient 5',
				  'ingredient06':'Ingredient 6',
				  'ingredient07':'Ingredient 7',
				  'ingredient08':'Ingredient 8',
				  'ingredient09':'Ingredient 9',
				  'ingredient10':'Ingredient 10',
				  'ingredient11':'Ingredient 11',
				  'ingredient12':'Ingredient 12',
				  'ingredient13':'Ingredient 13',
				  'ingredient14':'Ingredient 14',
				  'ingredient15':'Ingredient 15',
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