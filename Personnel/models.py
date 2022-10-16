from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
ROLES = (
    ('secretariat', 'secretariat'),
    ('Surveillant', 'Surveillant'),
    ('Directeur', 'Directeur'),
)

GENDERS = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme'),
)
class Travailleur(AbstractUser):
    idWorker = models.AutoField(primary_key=True)
    numCNI = models.TextField(unique=True)
    telephone = models.CharField(unique=True, null=True, blank=True, max_length=13, default="+2376")
    adresse = models.TextField(blank=True, null=True)
    photo_profil = models.ImageField(upload_to="Images", default='blank.png')
    sex = models.CharField(choices=GENDERS, max_length=10)
    role = models.CharField(choices=ROLES, max_length=20)
    dateNaissance = models.DateField(blank=True, null=True)
    #Affichage du personnel_travailleur
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    def __phone__(self):
        return f'{self.telephone}'

class Enseignant(models.Model):
    owner = models.OneToOneField(
        Travailleur, on_delete=models.CASCADE)
    idEnseignant = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.owner.__str__()

    def start_date(self):
        return self.owner.date_joined

    def username(self):
        return self.owner.username

    def gender(self):
        return self.owner.sex

    def phone_number(self):
        return self.owner.__phone__()
        
