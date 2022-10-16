from django.db import models
from Classe.models import Niveau
from Personnel.models import Travailleur, Enseignant
from Apprenant.models import Eleve

# Create your models here.
class Subject(models.Model):
    idMatiere = models.AutoField(primary_key=True)
    idNiveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    idProf = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    idpersonne = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    nomMatiere = models.CharField(max_length=45)
    coefficient = models.FloatField()
    description = models.TextField(default="Ici la description...")

    def __str__(self):
        return f'{self.nomMatiere}'
class Note(models.Model):
    idNote = models.AutoField(primary_key=True)
    idApprenant = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    idMatiere = models.ForeignKey(Subject, on_delete=models.CASCADE)
    note = models.FloatField()

    def __str__(self):
        return 