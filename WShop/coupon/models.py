from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
	code = models.CharField(max_length=50, verbose_name="Mã", unique=True)
	valid_from = models.DateTimeField(verbose_name="Giá trị từ")
	valid_to = models.DateTimeField(verbose_name="Hết giá trị")
	discount = models.IntegerField(verbose_name="Giảm giá(%)",
			validators=[MinValueValidator(0), MaxValueValidator(100)]) 
	active = models.BooleanField(verbose_name="Có hiệu lực?")

	class Meta:
		verbose_name = 'Mã giảm giá'
		verbose_name_plural = 'Mã giảm giá'

	def __str__(self):
		return self.code