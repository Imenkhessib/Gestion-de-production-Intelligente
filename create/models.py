from django.db import models

# Create your models here.
class project(models.Model):
    id_project = models.CharField(max_length=50)
    name_project = models.CharField (max_length=50)
    client = models.CharField(max_length=50)
    num_bon_commande = models.IntegerField
    project_chief = models.CharField (max_length=50)


class MO (models.Model):
    num_MO = models.CharField(max_length=50)
    priority_MO =  models.IntegerField
    creation_date = models.DateField
    state_MO = models.CharField(max_length=50)
    date_dem_prev = models.DateField
    date_dem_real = models.DateField
    date_cloture_prev = models.DateField
    date_cloture_act = models.DateField
    date_cloture_real = models.DateField

class piece (models.Model):
    product_id= models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    quantity=models.IntegerField