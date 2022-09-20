from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Bug(models.Model):
	CHOICES = (
			("resolved", "resolved"),
			("unresolved", "unresolved")
		)
	title = models.CharField(max_length=100)
	body = models.TextField()
	assigned = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	status = models.CharField(max_length=100, choices=CHOICES, default="unresolved")


class Comment(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	bug = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
