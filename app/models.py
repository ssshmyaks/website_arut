from django.db import models

# Create your models here.


class contact(models.Model):
	name = models.CharField(
		max_length=255, verbose_name="Имя"
	)
	email = models.EmailField(
		max_length=255, verbose_name="Электронная почта"
	)
	message = models.CharField(
		max_length=2000, verbose_name="Сообщение"
	)

	def __str__(self):
		return self.name
