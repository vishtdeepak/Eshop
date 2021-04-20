from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
	list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
	list_display = ['name']

# class AdminOrder(admin.ModelAdmin):
# 	list_display = ['product','customer']


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Customer)
admin.site.register(Order)
