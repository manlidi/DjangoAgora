from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    adresse = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to='media/photo', null=True)
    biographie = models.TextField(null=True)
    centre = models.TextField(null=True)
    groupes = models.ManyToManyField('Groupes', through='Appartenir', related_name='membre')
 
        
class Amis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    primuser=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='prim')
    seconuser=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='secon')
    status=models.BooleanField(default=False,null=True)
    created_at=models.DateTimeField(auto_now=True)
        

class Groupes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='creator')
    nom = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    membres = models.ManyToManyField('Users', through='Appartenir', related_name='groupes_appartenus')
    photo = models.ImageField(upload_to='media/photo_groupe', null=True)
    code_groupe= models.CharField(max_length=250,unique=True,null=True)
    

class Appartenir(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='appartenances')
    groupe = models.ForeignKey('Groupes', on_delete=models.CASCADE, related_name='appartenances')
    created_at = models.DateTimeField(auto_now=True)

class Messages(models.Model):
    text=models.TextField(null=True)
    file=models.FileField(upload_to='media/document',null=True)
    sender=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='sender')
    destinate=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='destinate',null=True)
    destinategroup=models.ForeignKey('Groupes',on_delete=models.CASCADE,related_name='destinategroup' ,null=True)
    lecture=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    
class Notifications(models.Model):
    amis = models.ForeignKey('Amis', on_delete=models.CASCADE,null=True)
    text=models.TextField()
    sender=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='envoyeur')
    destinate=models.ForeignKey('Users',on_delete=models.CASCADE,related_name='receveur')
    lecture=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
