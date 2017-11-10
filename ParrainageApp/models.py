# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models.fields.related import OneToOneField, ManyToManyField

# Create your models here.

class Filiaire(models.Model):
    nom = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nom

class Personne(models.Model):
    noms = models.CharField(max_length = 30, null = True)
    age = models.IntegerField(default=20)
    photo = models.ImageField(upload_to = 'ParrainageApp/static/ParrainageApp/img/', null = True, blank = True, default = 'ParrainageApp/static/ParrainageApp/img/PEGGY.jpg')
    Filiaire = models.ForeignKey(Filiaire)
    sexe = models.CharField(max_length = 20, null = True)
    
    def __str__(self):
        return self.noms + self.Filiaire.nom
    def logo(self):
        chaine= str(self.photo)
        return chaine[13:len(chaine)]
    
    class Meta:
        abstract = True


class Filleuil(Personne):
    description = models.TextField()


def quatite(sexe):
    if sexe == "Femme":
        return ("Elle est Jolie", "Elle est charmante", "Elle est élégante", "Oui c'est ta marraine et c'est ...")
    else:
        return ("Il est Mignon", "Un gars sérieux", "Un gars Charismatique", "C'est bien Lui C'est ...")

class Parrain(Personne):
    description = models.TextField()
    filleul = models.ManyToManyField(Filleuil, blank= True)
    
    def get_filleul(self):
        return self.filleul.all()
        

    
        



    
