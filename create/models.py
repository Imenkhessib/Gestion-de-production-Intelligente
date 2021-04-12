from django.db import models
import datetime


# Create your models here.
class project(models.Model):
    id_auto = models.PositiveIntegerField()
    project_ref = models.CharField(max_length=50, primary_key=True)
    project_name = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    purchase_order = models.IntegerField()
    project_manager = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.id_auto = project.objects.all().count() + 1
        super(project, self).save()


class MO(models.Model):
    id_auto = models.PositiveIntegerField()
    mo_reference = models.CharField(max_length=50, primary_key=True)
    mo_priority = models.PositiveIntegerField()
    launch_Date = models.DateField(default=2020 - 1 - 1)
    mo_status = models.CharField(max_length=50)
    schedul_start_date = models.DateField(default=2020 - 1 - 1)
    exec_start_date = models.DateField(default=2020 - 1 - 1)
    schedul_due_date = models.DateField(default=2020 - 1 - 1)
    refresh_due_date = models.DateField(default=2020 - 1 - 1)
    exec_due_date = models.DateField(default=2020 - 1 - 1)
    project_Reference = models.ForeignKey(project, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.id_auto = MO.objects.all().count() + 1
        super(MO, self).save()


class item(models.Model):
    id_auto = models.PositiveIntegerField()
    item_reference = models.CharField(max_length=50, primary_key=True)
    designation = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    material = models.CharField(max_length=50)
    scheduled_hours = models.IntegerField(default=0)
    performed_hours = models.IntegerField(default=0)
    compliance = models.IntegerField(default=0)
    no_compliance = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    thickness = models.IntegerField(default=0)
    cnc = models.BooleanField()
    router = models.BooleanField()
    laser_Cutters = models.BooleanField()
    milling = models.BooleanField()
    mo_reference = models.ForeignKey(MO, on_delete=models.CASCADE, default="1555")
    two_d_plan = models.FileField(null=True, blank=True)
    three_d_plan = models.FileField(null=True, blank=True)

    class Meta(object):
        unique_together = [
            ("item_reference", "mo_reference"),
        ]

    def save(self, *args, **kwargs):
        self.id_auto = item.objects.all().count() + 1
        super(item, self).save()


class machine(models.Model):
    id_auto = models.PositiveIntegerField()
    mach_reference = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    state_machine = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)


class task(models.Model):
    id_auto = models.PositiveIntegerField()
    task_reference = models.CharField(max_length=50)
    task_status = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    task_priority = models.IntegerField(default=0)
    item_reference = models.ForeignKey(item, on_delete=models.CASCADE, default="1555")
    mach_reference = models.ForeignKey(machine, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.id_auto = item.task.all().count() + 1
        super(task, self).save()


class user(models.Model):
    id_user = models.CharField(max_length=50, primary_key=True)
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

    class Meta(object):
        unique_together = [
            ("application_name", "id_user"),
        ]


class machine_operator(models.Model):
    id_operator = models.ForeignKey(user, on_delete=models.CASCADE, primary_key=True)
    skills = models.CharField(max_length=50)
    id_auto = models.ForeignKey(machine, on_delete=models.CASCADE)
    id_auto = models.ForeignKey(item, on_delete=models.CASCADE)
