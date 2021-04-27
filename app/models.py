from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  title 
#  status
#  date - current 
#  user 
#  priority


class TODO(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('P', 'PENDING'),
    ]
    members_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),
    ('6', '6️⃣'),
    ('7', '7️⃣'),
    ('8', '8️⃣'),
    ('9', '9️⃣'),
    ('10', '🔟'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    user  = models.ForeignKey(User  , on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    members = models.CharField(max_length=2 , choices=members_choices)
    ldate = models.DateField(null=True,blank=True)


class Contact(models.Model):
    cname = models.CharField(max_length=30,blank=True,null=True)
    text = models.CharField(max_length=250,blank=True,null=True)