from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Người dùng", on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, verbose_name="Ngày sinh", null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', verbose_name="Ảnh đại diện", blank=True)

	class Meta:
		verbose_name = 'Tài khoản người dùng'
		verbose_name_plural = 'Tài khoản người dùng'

	def __str__(self):
		return 'Profile {}'.format(self.user.username)