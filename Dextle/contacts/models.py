from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Contact(models.Model):
    contact_first_name = models.CharField(max_length=30, name="First Name", blank=False)
    contact_last_name = models.CharField(max_length=30, name="Last Name", blank=False)
    where_met = models.CharField(max_length=50, name="Where You Met Contact")
    when_met = models.DateField('date met',name="When You Met")
    contact_desc = models.TextField(name="Describe Contact")
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female')
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_email = models.EmailField(max_length=50, name="Contact Email")
    contact_phone = PhoneNumberField(name="Contact Phone", blank=True)

    #def __str__(self):
        #return self.contact_name
