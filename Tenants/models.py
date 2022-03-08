from django.db import models

# Create your models here.
class Tenants(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile = models.IntegerField(null=True , blank=True)
    Contact = models.TextField()
    No_members = models.IntegerField(null=True , blank=True)
    Apartment_no = models.IntegerField(null=True , blank=True)
    Con_start_date = models.DateField(null=True , blank=True)
    Con_end_date = models.DateField(null=True , blank=True)
    Rental_amount = models.IntegerField(null=True , blank=True)


class User(models.Model):
    Email = models.EmailField()
    Password = models.TextField(max_length=20)


class Visitor(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    Date_Visit = models.DateField()
    Date_Submitted = models.DateTimeField(auto_now_add=True)


class Complaints(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Mobile = models.IntegerField()
    Text = models.TextField()
    Date_Reg = models.DateTimeField(auto_now_add=True)
