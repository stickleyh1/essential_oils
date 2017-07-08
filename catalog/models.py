from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime as dt
import uuid

class Ailment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Ailment")
	name = models.CharField("name", max_length=200, help_text="The name of the ailment", default="Ailment Name")

	def __str__(self):
		return self.name
		
class Product(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Product")
	name = models.CharField("name", max_length=200, help_text="The name of the product", default="Oil Name")
	description = models.CharField("description", max_length=1000, help_text="The description of the product", blank=True, default="An oil that treats ailments")
	price = models.DecimalField(default=10.00, max_digits=19, decimal_places=2)
	isBlend = models.BooleanField(default=False)
	ailments = models.ManyToManyField(Ailment, help_text="Select the ailments this product treats", related_name="Ailments")

	def __str__(self):
		if self.isBlend:
			return '%s (Blended Oil) - %s' % (self.name, self.price)
		else:
			return '%s (Single Oil) - %s' % (self.name, self.price)

	def get_absolute_url(self):
		return reverse('product-detail', args=[str(self.id)])

class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Order")
	total = models.DecimalField(default=10.00, max_digits=19, decimal_places=2)
	buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Borrower")
	products = models.ManyToManyField(Product, help_text="Select the products in this order", related_name="Products")

	def __str__(self):
		return '%s : %s (%s)' % (self.buyer.username, self.total, self.id)