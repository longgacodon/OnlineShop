from django.db import models
from product.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupon.models import Coupon
from django.contrib.auth.models import User

class Order(models.Model):
	name = models.CharField(max_length=100, verbose_name="Họ và tên")
	email = models.EmailField()
	address = models.CharField(max_length=250, verbose_name="Địa chỉ")
	postal_code = models.CharField(max_length=20, verbose_name="Mã bưu điện")
	city = models.CharField(max_length=100, verbose_name="Thành phố")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False, verbose_name="Đã trả")
	coupon = models.ForeignKey(Coupon, verbose_name="Mã giảm giá", related_name='orders', null=True,
								blank=True, on_delete=models.SET_NULL)
	discount = models.IntegerField(default=0, verbose_name="Giảm giá(%)",
			validators=[MinValueValidator(0), MaxValueValidator(100)])

	class Meta:
		ordering = ('-created',)
		verbose_name = 'Đơn hàng'
		verbose_name_plural = 'Đơn hàng'

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		total_cost = sum(item.get_cost() for item in self.items.all())
		return total_cost - total_cost * (self.discount / Decimal('100'))

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', verbose_name="Đơn hàng", 
									on_delete=models.CASCADE)
	product = models.ForeignKey(Product, verbose_name="Sản phẩm", related_name='order_items',
									on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá")
	quantity = models.PositiveIntegerField(default=1, verbose_name="Số lượng")

	class Meta:
		verbose_name = 'Chi tiết đơn hàng'
		verbose_name_plural = 'Chi tiết đơn hàng'

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity