from django.db import models

# Create your models here.
class Work(models.Model):
    work_name = models.TextField(max_length=20)
    description_work = models.TextField()