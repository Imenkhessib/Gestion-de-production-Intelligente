from django.db import models
import datetime
# Create your models here.
class project(models.Model):
    id_auto = models.AutoField(primary_key=True)
    id_project = models.CharField(max_length=50)
    name_project = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    num_bon_commande = models.IntegerField()
    project_chief = models.CharField(max_length=50)


class MO (models.Model):
    id_auto = models.AutoField(primary_key=True)
    num_MO = models.CharField(max_length=50)
    priority_MO = models.IntegerField()
    creation_date = models.DateField(default=2020-1-1)
    state_MO = models.CharField(max_length=50)
    date_dem_prev = models.DateField(default=2020-1-1)
    date_dem_real = models.DateField(default=2020-1-1)
    date_cloture_prev = models.DateField(default=2020-1-1)
    date_cloture_act = models.DateField(default=2020-1-1)
    date_cloture_real = models.DateField(default=2020-1-1)

class piece (models.Model):
    product_id = models.CharField(max_length=50)
    designation =models.CharField(max_length=50)
    quantity = models.IntegerField()

