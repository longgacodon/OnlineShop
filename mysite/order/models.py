from django.db import models
from product.models import Product

class Order(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items',
									on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items',
									on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity

"""
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    customter_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=16)
    total_price = models.FloatField()
    payment = models.CharField(max_length=32)
    payment_info = models.TextField()
    status = models.BooleanField(default=False)
    day_created = models.DateTimeField(auto_now_add=True)	
"""