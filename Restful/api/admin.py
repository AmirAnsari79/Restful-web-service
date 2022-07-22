from django.contrib import admin

# Register your models here.
from api.models import Store, Item

admin.site.register(Store)
admin.site.register(Item)