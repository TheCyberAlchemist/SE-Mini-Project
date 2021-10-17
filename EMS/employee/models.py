from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class department(models.Model):
	name = models.CharField(max_length=500)
	desciption = models.TextField()
	
	def __str__(self):
		return str(self.name)


class employee(models.Model):
	User_id = models.OneToOneField(get_user_model(),on_delete = models.CASCADE)
	# name = models.CharField(max_length=500)
	# email = models.EmailField()
	designation = models.CharField(max_length=500)
	emp_id = models.CharField(max_length=50)
	phone_no = models.CharField(max_length=10)
	Department = models.ForeignKey(department,on_delete = models.CASCADE)

	def __str__(self):
		return str(self.User_id)

class attendance(models.Model):
	Employee_id = models.ForeignKey(employee,on_delete = models.CASCADE)
	entry_time = models.DateTimeField(auto_now_add=False)
	exit_time = models.DateTimeField(auto_now_add=False)
	def __str__(self):
		return f"{self.Employee_id}"