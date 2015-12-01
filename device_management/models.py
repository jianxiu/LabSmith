from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    link = models.URLField()
    owner = models.ForeignKey(User,related_name="owner_user",blank=True,null=True)
    wanted = models.ForeignKey(User,related_name="wanted_user",blank=True,null=True)
    user = models.CharField(max_length=20,blank=True,null=True)
    info = models.CharField(max_length=1000,blank=True,null=True)
    spa_ip = models.CharField(max_length=20,blank=True,null=True)
    spb_ip = models.CharField(max_length=20,blank=True,null=True)
    spa_mac = models.CharField(max_length=17,blank=True,null=True)
    spb_mac = models.CharField(max_length=17,blank=True,null=True)
    mgmt_ip = models.CharField(max_length=20,blank=True,null=True)
    spa_term = models.CharField(max_length=30,blank=True,null=True)
    spb_term = models.CharField(max_length=30,blank=True,null=True)
    bmc_spa_ip =models.CharField(max_length=20,blank=True,null=True)
    bmc_spb_ip=models.CharField(max_length=20,blank=True,null=True)
    platform_type = models.CharField(max_length=30,blank=True,null=True)
    pxeFilePath = models.CharField(max_length=300,blank=True,null=True)
    def __unicode__(self):
        return self.name

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=100)
    device = models.ForeignKey(Device)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    def __unicode__(self):
        return self.user.get_full_name() +" "+  self.msg + " " +  self.device.name + " at " + self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")

class MaintainLog(models.Model):
    id = models.AutoField(primary_key=True)
    MachineName = models.CharField(max_length=30)
    user = models.CharField(max_length=20,blank=True,null=True)
    timestamp=models.DateTimeField()
    content = models.CharField(max_length=1000,blank=True,null=True)
    # countNumber = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.MachineName + " " + self.user+" " + "at"+ " "+self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")


class UsageLog(models.Model):
    id = models.AutoField(primary_key=True)
    machineName = models.CharField(max_length=30)
    user = models.CharField(max_length=20,blank=True,null=True)
    reserveTimestamp=models.DateTimeField()
    releaseTimestamp=models.DateTimeField()
    isUse = models.CharField(max_length=1000,blank=True,null=True)
    # countNumber = models.CharField(max_length=30,blank=True,null=True)
    def __unicode__(self):
        return self.user + " used " + self.MachineName + " form "+ \
               self.reserveTimestamp.strftime("%A, %d. %B %Y %I:%M%p") + " to " + \
               self.releaseTimestamp.strftime("%A, %d. %B %Y %I:%M%p")