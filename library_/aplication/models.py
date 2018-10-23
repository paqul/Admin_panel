from django.db import models

# Create your models here.

class Model1(models.Model):
    var1 = models.CharField(max_length=10)
    var2 = models.CharField(max_length=50)
    var3 = models.CharField(max_length=3)


class Model2(models.Model):
    whole_var = models.ForeignKey(Model1, on_delete=models.DO_NOTHING)


class Model3(models.Model):
    other_var = models.CharField(max_length=1)
    second_var = models.ForeignKey(Model2, on_delete=models.DO_NOTHING)

