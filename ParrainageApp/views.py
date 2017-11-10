#-*-coding: utf-8-*-

from django.shortcuts import render_to_response, render, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import *
from django.views import generic
from random import randint
from django.db.models import Count


def home(request):
    #Création des parrains et Filleul
    """i = 0
    filiaire = Filiaire.objects.get(nom = 'License')
    while(i<4):
        parrain = Parrain.objects.create(noms ='Aymard' + str(i), age=20, Filiaire=filiaire, description = 'Description de la personne')     
        i = i + 1
    
    i = 0
    filiaire = Filiaire.objects.get(nom = 'Mbf & Msi')
    while(i<2):
        parrain = Parrain.objects.create(noms ='Veronne' + str(i), age=20, Filiaire=filiaire, description = 'Description de la personne')     
        i = i + 1
        
    i = 0
    filiaire = Filiaire.objects.get(nom = 'Mag')
    while(i<2):
        parrain = Parrain.objects.create(noms ='Freddy' + str(i), age=20, Filiaire=filiaire, description = 'Description de la personne')     
        i = i + 1
    
    i = 0
    filiaire = Filiaire.objects.get(nom = 'Mcf')
    while(i<2):
        parrain = Parrain.objects.create(noms ='Sam' + str(i), age=20, Filiaire=filiaire, description = 'Description de la personne')         
        i = i + 1"""
    
    
    if request.method == 'POST':
        #Création du Filleul
        sexe = request.POST['sexe_choisie']
        id_filiere = int(request.POST['filiere_choisie'])
        filiere = Filiaire.objects.get(id = id_filiere)
        noms = request.POST['nom_filleul']
        description = "Juste une brêve description de la personne"
        filleul = Filleuil.objects.create(noms = noms, Filiaire = filiere, description = description, sexe = sexe)        
        
        #Je recupere tout les parrains de ma filiere qui n'ont pas de filleul
        les_parrain = Parrain.objects.filter(filleul__isnull = True).filter(Filiaire = filiere).annotate(num_filleul= Count('filleul')).filter(num_filleul__lt= 1)
        
        #Choix du Parrain
        #Cas de MCF(ok)
        if filiere.nom == 'Mcf':            
            mon_parrain= choisir_parrain_sample(filleul,les_parrain)
        #Cas de Mag(ok)
        if filiere.nom == 'Mag':            
            if les_parrain:
                mon_parrain= choisir_parrain_sample(filleul, les_parrain)
            else:
                les_parrain = Parrain.objects.filter(Filiaire = filiere).annotate(num_filleul= Count('filleul')).filter(num_filleul__lt= 2)
                mon_parrain= choisir_parrain_sample(filleul, les_parrain)
        #Cas de Mbf & Msi(ok)
        if filiere.nom == 'Mbf & Msi':
            if les_parrain:
                mon_parrain= choisir_parrain_sample(filleul, les_parrain)
            else:
                les_parrain = Parrain.objects.filter(Filiaire = filiere).annotate(num_filleul= Count('filleul')).filter(num_filleul__lt= 2)
                mon_parrain= choisir_parrain_sample(filleul, les_parrain)
        #Cas des license
        if filiere.nom == 'License':            
            #Je verifie si tout les parrains n'ont pas déjà 2 filleul
            if(verifier(filiere)):
                if les_parrain:
                    mon_parrain= choisir_parrain_sample(filleul, les_parrain)
                else:
                    les_parrain = Parrain.objects.filter(Filiaire = filiere).annotate(num_filleul= Count('filleul')).filter(num_filleul__lt= 2)
                    mon_parrain= choisir_parrain_sample(filleul, les_parrain)
            else:
                if(verifier2(filiere)):
                    les_parrain = Parrain.objects.exclude(Filiaire = filiere).annotate(num_filleul = Count('filleul')).filter(num_filleul__lt=2)
                    mon_parrain = choisir_parrain_sample(filleul, les_parrain)
                else:
                    les_parrain = Parrain.objects.filter(Filiaire = filiere)
                    mon_parrain = choisir_parrain_sample(filleul, les_parrain)
            
            
        return HttpResponseRedirect('/parrain/' + str(mon_parrain))
    
    filieres = Filiaire.objects.order_by("id")
    
    return render(request, 'ParrainageApp/home.html', {
        'filieres': filieres, 
    })

def choisir_parrain_sample(filleul,les_parrain):
    nbr_parrain = les_parrain.count()
    mon_parrain = les_parrain[randint(0, nbr_parrain-1)]
    mon_parrain.filleul.add(filleul)
    mon_parrain.save() 
    print mon_parrain.id
    return mon_parrain.id

def verifier(filiere):
    les_parrain = Parrain.objects.annotate(num_filleul = Count('filleul')).filter(Filiaire = filiere)
    flag = False
    for elt in les_parrain:
        if elt.num_filleul != 2:            
            flag =  True
            break
            
    print les_parrain[0].num_filleul
    return flag

def verifier2(filiere):
    les_parrain = Parrain.objects.exclude(Filiaire = filiere).annotate(num_filleul = Count('filleul'))
    flag = False
    for elt in les_parrain:
        if elt.num_filleul != 2:
            flag = True
            break
    return flag

def parrain(request, parrain_id):
    
    parrain = Parrain.objects.get(id= parrain_id)
    
    return render(request, 'ParrainageApp/parrain.html', {
        'parrain' : parrain,
    })

def recap(request):
    Parrains = Parrain.objects.order_by("noms")
    
    return render(request, 'ParrainageApp/recap.html', {
        'Parrains': Parrains,
    })