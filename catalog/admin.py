from django.contrib import admin
from .models import Order, Product, Ailment

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'isBlend')
	list_display_links = ('name',)
	list_per_page = 10
	ordering = ['isBlend']
	search_fields = ['name']
	exclude = ['ailments']

class OrderAdmin(admin.ModelAdmin):
	list_display = ('buyer', 'total', 'id')
	list_per_page = 10

class AilmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'id')
	list_per_page = 10
	ordering = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ailment, AilmentAdmin)