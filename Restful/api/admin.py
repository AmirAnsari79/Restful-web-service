from django.contrib import admin

# Register your models here.
from api.models import Store, Item, Book

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Book)