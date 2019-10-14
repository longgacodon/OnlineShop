from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, null=True, 
                default='M', choices=GENDER_CHOICES)  #avoid setting an invalid default|default=GENDER_CHOICES[0]
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=120)
    birthday = models.DateField()
    day_joined = models.DateTimeField(verbose_name='Day Joined', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'day_joined')

    def __str__(self):
        return self.name	