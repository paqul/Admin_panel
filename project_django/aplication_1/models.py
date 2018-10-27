from django.db import models

# Create your models here.


class Model1(models.Model):
    var1 = models.CharField(max_length=10)
    var2 = models.CharField(max_length=50)
    var3 = models.CharField(max_length=30)

    def __str__(self):
        return "{var1} : {var2} : {var3}".format(var1=self.var1, var2=self.var2, var3=self.var3)


class Model2(models.Model):
    whole_var = models.ForeignKey(Model1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "All variables in other object: {whole_var}".format(whole_var=self.whole_var)


class Model3(models.Model):
    other_var = models.CharField(max_length=1)
    second_var = models.ForeignKey(Model2, on_delete=models.DO_NOTHING)

