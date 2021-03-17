from django.db import models

# Create your models here.

comp_choices= (('NO','no'),('YES','yes'))

class Task(models.Model):
	title= models.CharField(max_length=200)
	description= models.CharField(max_length=1000,default='No desc. provided')
	is_completed= models.CharField(max_length=3, choices=comp_choices,default= 'NO')

	def __str__(self):
		return self.title	