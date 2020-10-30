from django.contrib import admin

from mealmageapp.models import StoredDish, MealPlan, GroceryList

admin.site.register(StoredDish)
admin.site.register(MealPlan)
admin.site.register(GroceryList)
