from django.contrib import admin

from mealmageapp.models import StoredDish, DailyMealPlan, GroceryList

admin.site.register(StoredDish)
admin.site.register(DailyMealPlan)
admin.site.register(GroceryList)
