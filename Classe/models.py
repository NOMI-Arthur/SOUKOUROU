from django.db import models

# Create your models here.
class Niveau(models.Model):
        idNiveau = models.AutoField(primary_key=True)
        niveau = models.IntegerField()
        def __str__(self):
            return f'{self.niveau}'
        
class Classe(models.Model):
    idClasse = models.AutoField(primary_key=True)
    niveau = models.ForeignKey(Niveau, 
     on_delete=models.CASCADE
    )
    libelleSalle = models.CharField(max_length=15)
    montant = models.FloatField()
    
    def __str__(self):
        return f'{self.libelleSalle}'
    def __montant__(self):
        return f'{self.montant}'
    def __level__(self):
        return f'{self.niveau}'
        
    