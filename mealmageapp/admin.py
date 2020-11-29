from django.contrib import admin

from mealmageapp.models import StoredDish, DailyMenu, GroceryList

admin.site.register(StoredDish)
admin.site.register(DailyMenu)
admin.site.register(GroceryList)
