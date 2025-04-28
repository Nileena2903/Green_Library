from django.db import models

# Create your models here.


class student_tbl(models.Model):
 snm = models.CharField(max_length=25)
 email = models.EmailField()
 mob = models.CharField(max_length=50)