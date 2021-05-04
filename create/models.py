from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

#from viewflow.fields import CompositeKey

import datetime
# Create your models here.
class project(models.Model):
    project_Reference = models.CharField(max_length=50, primary_key=True)
    id_auto = models.IntegerField()
    name_project = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    Purchase_Order = models.CharField(max_length=50, null=True)
    project_chief = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.id_auto = project.objects.all().count() + 1
        super(project, self).save()


class MO (models.Model):
    id_auto = models.IntegerField()
    num_MO = models.CharField(max_length=50, primary_key=True)
    priority_MO = models.IntegerField(null=True)
    launch_Date = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    state_MO = models.CharField(max_length=60)
    mechanical_engineer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #date_dem_prev = models.DateField(default=False)
    #date_dem_real = models.DateField(default=False)
    #date_cloture_prev = models.DateField(default=False)
    #date_cloture_act = models.DateField(default=False)
    date_val_dem = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    date_val_respval = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    date_val_chefproj = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    date_val_respprod = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    date_val_chefat = models.DateField(default=datetime.datetime.now().strftime("%Y-%m-%d"))
    cause_invalid = models.TextField()
    project_Reference = models.ForeignKey(project, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.id_auto = MO.objects.all().count() + 1
        super(MO, self).save()



class piece (models.Model):
    id_auto = models.AutoField(primary_key = True)
    id_item = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    quantity = models.IntegerField(null=False)
    material = models.CharField(max_length=50)
    scheduled_hours = models.IntegerField(default=0)
    performed_hours = models.IntegerField(default=0)
    compliance = models.IntegerField(default=0)
    no_compliance = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    thickness = models.IntegerField(default=0)
    CNC = models.BooleanField()
    Router = models.BooleanField()
    laser_Cutters = models.BooleanField()
    milling = models.BooleanField()
    machine_choices = (
        ('cnc', 'CNC'),
        ('router', 'Router'),
        ('milling', 'Milling'),
        ('lathe', 'Lathe'),
        ('laser_cutter', 'Laser Cutter'),
    )
    machines = MultiSelectField(choices=machine_choices, blank=False)
    scheduled_hours_CNC = models.IntegerField(default=0, null=True)
    scheduled_hours_Router = models.IntegerField(default=0, null=True)
    scheduled_hours_Milling = models.IntegerField(default=0, null=True)
    scheduled_hours_laser_cutters = models.IntegerField(default=0, null=True)
    two_d = models.FileField(null=True, blank=True)
    three_d = models.FileField(null=True, blank=True)

    num_MO = models.ForeignKey(MO, on_delete=models.CASCADE, null=True)
    #id = CompositeKey(columns=['id_item', 'num_MO'])

    class Meta(object):
        unique_together = [
            ("id_item", "num_MO"),
        ]



class machine(models.Model):
    type = models.CharField(max_length=50)
    state_machine = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

class task(models.Model):
    id_task = models.CharField(max_length=50)
    state_task = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    priority_task = models.IntegerField(default=0)
    num_item = models.ForeignKey(piece , on_delete=models.CASCADE, default="1555")
    id_machine = models.ForeignKey(machine, on_delete=models.CASCADE)

class user (models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50)
    is_online = models.BooleanField()

class access_control(models.Model):
    password = models.CharField(max_length=50)
    permission_class = models.IntegerField(default=1)
    is_admin = models.BooleanField()
    application_name = models.CharField(max_length=50)
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)


class machine_operator(models.Model):
    id_operator = models.ForeignKey(user, on_delete=models.CASCADE, primary_key=True)
    skills = models.CharField(max_length=50)
    id_auto_machine = models.ForeignKey(machine, on_delete=models.CASCADE)
    id_auto_item = models.ForeignKey(piece, on_delete=models.CASCADE)