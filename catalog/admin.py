from django.contrib import admin
from .models import Order, Product, Ailment

class ProductAdmin(admin.ModelAdmin):
	# sets values for how the admin site lists your products
	list_display = ('name', 'price', 'isBlend')
	list_display_links = ('name',)
	list_per_page = 10
	ordering = ['isBlend']
	search_fields = ['name', 'description', 'isBlend']
	exclude = ['ailments']

# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Ailment)