from django.contrib import admin
from .models import Category,Product,Currency

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Currency)