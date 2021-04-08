from django.db import models

class Dictionary(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Слово(анаграмма)')

	def __str__(self):
		return self.name


