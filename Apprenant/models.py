import datetime
from django.db import models
from Classe.models import Classe
# Create your models here.

SEXE = (
    ('Garçon','Garçon'),
    ('Fille','Fille'),
)

class Eleve(models.Model):
    
    idApprenant =models.AutoField(primary_key=True)
    idClasse = models.ForeignKey(Classe, on_delete=models.CASCADE)
    nomApprenant = models.CharField(blank=True,max_length=50)
    dateNaissance = models.DateField(blank=True, null=True)
    dateInscription = models.DateField()
    photo_profil = models.ImageField(upload_to="Images", default='blank.png')
    sexe = models.CharField(choices=SEXE, max_length=10)
    totalPaye = models.FloatField()
    
    def __str__(self):
        return f'{self.nomApprenant}'