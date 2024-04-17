from django.db import models

import os
from django.contrib.auth.models import User
from accounts.models import AuteurUser
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.
class Departement(models.Model):
    nom=models.CharField(max_length=50, null=False)
  
    def __str__(self):
        return self.nom
    
class Commune(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE,null=True)
    nom=models.CharField(max_length=50, null=False)
  
    def __str__(self):
        return self.nom
    
class Arrondissement(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE,null=True)
    nom=models.CharField(max_length=50, null=False)
  
    def __str__(self):
        return self.nom
    
class Quartier(models.Model):
    arrondissement= models.ForeignKey(Arrondissement, on_delete=models.CASCADE,null=True)
    nom=models.CharField(max_length=50, null=False)
  
    def __str__(self):
        return self.nom
    
class Operation(models.Model):
    type = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.type
    

    

class Types(models.Model):
    name=models.CharField(max_length=50, null=False)
  
    def __str__(self):
        return self.name

class Immeuble(models.Model):
    name=models.CharField(max_length=100, null=True)
    departement= models.ForeignKey(Departement, on_delete=models.CASCADE,null=True)
    commune= models.ForeignKey(Commune, on_delete=models.CASCADE,null=True)
    arrondissement= models.ForeignKey(Arrondissement, on_delete=models.CASCADE,null=True)
    quartier= models.ForeignKey(Quartier, on_delete=models.CASCADE,null=True)
    operation= models.ForeignKey(Operation, on_delete=models.CASCADE,null=True)
    proprietaire= models.ForeignKey(AuteurUser,related_name="proprietaire", on_delete=models.CASCADE,null=True)
    ambassadeur= models.ForeignKey(AuteurUser,related_name="ambassadeur", on_delete=models.CASCADE,null=True)
    type= models.ForeignKey(Types, on_delete=models.CASCADE,null=True)
    prix=models.IntegerField(null=True)
    description=RichTextUploadingField(blank=True, null=True)
    statut=models.BooleanField(default=False, blank=True)
    
   
    
    def __str__(self):
        return self.name

class Chambre(models.Model):
    nombre= models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.nombre)
    
class Salon(models.Model):
    nombre= models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.nombre)
    
class Cuisine(models.Model):
    nombre= models.IntegerField(null=True)
    def __str__(self):
        return str(self.nombre)
    
class Douche(models.Model):
    nombre= models.IntegerField(null=True)
    def __str__(self):
        return str(self.nombre)
    
class Balcon(models.Model):
    nombre= models.IntegerField(null=True)
    def __str__(self):
        return str(self.nombre)
    
    
class Chambres(models.Model):
    proprietaire= models.ForeignKey(AuteurUser, on_delete=models.CASCADE,null=True)
    immeuble= models.ForeignKey(Immeuble, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50, null=True)
    prix=models.IntegerField(null=True)
    salon= models.ForeignKey(Salon, on_delete=models.CASCADE,null=True)
    chambre= models.ForeignKey(Chambre, on_delete=models.CASCADE,null=True)
    cuisine= models.ForeignKey(Cuisine, on_delete=models.CASCADE,null=True)
    douche= models.ForeignKey(Douche, on_delete=models.CASCADE,null=True)
    balcon= models.ForeignKey(Balcon, on_delete=models.CASCADE,null=True)   
    
    

class ImagesImmeuble(models.Model):
    immeuble= models.ForeignKey(Immeuble, on_delete=models.CASCADE,null=True)
    images= models.ImageField(upload_to="images_immeuble",blank=True, null=True)
    
    def __str__(self):
         return str(self.images)
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)         

class Images(models.Model):
    chambres= models.ForeignKey(Chambres, on_delete=models.CASCADE,null=True)
    images = models.ImageField(upload_to="images_chambre",blank=True, null=True)
    
    def __str__(self):
         return str(self.images)
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)    
    
    class Meta:
        verbose_name_plural=('Chambres')
        
    def __str__(self):
        return str(self.images)
     
class Terrain(models.Model):
    departement= models.ForeignKey(Departement, on_delete=models.CASCADE,null=True)
    commune= models.ForeignKey(Commune, on_delete=models.CASCADE,null=True)
    arrondissement= models.ForeignKey(Arrondissement, on_delete=models.CASCADE,null=True)
    quartier= models.ForeignKey(Quartier, on_delete=models.CASCADE,null=True)
    operation= models.ForeignKey(Operation, on_delete=models.CASCADE,null=True)
    proprietaire= models.ForeignKey(AuteurUser, on_delete=models.CASCADE,null=True)
    # ambassadeur= models.ForeignKey(Ambassadeur, on_delete=models.CASCADE,null=True)
    images=models.ImageField(upload_to="images_terrain",blank=True, null=True)
    croquis=models.FileField(upload_to="pdf_terrain")
    prix=models.IntegerField(null=True)
    description=RichTextUploadingField(blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural=('Terrains')
        
    def __str__(self):
         return self.departement

class Plan(models.Model):
    name=models.CharField(max_length=100, null=True)
    proprietaire= models.ForeignKey(AuteurUser, on_delete=models.CASCADE,null=True)
    # images=models.ImageField(upload_to="images_terrain",blank=True, null=True)
    croquis=models.FileField(upload_to="pdf_terrain")
    prix=models.IntegerField(null=True)
    description=RichTextUploadingField(blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural=('Plans')
        
    def __str__(self):
         return self.name
    
class ImagesPlan(models.Model):
    plan= models.ForeignKey(Plan, on_delete=models.CASCADE,null=True)
    images= models.ImageField(upload_to="images_plan",blank=True, null=True)
    
    def __str__(self):
         return str(self.images)
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

class Porte(models.Model):
    proprietaire= models.ForeignKey(AuteurUser, on_delete=models.CASCADE,null=True)
    
    class Meta:
        verbose_name_plural=('Portes')

class Offre(models.Model):
    name=models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name
    

    
class ContactezNous(models.Model):
    name=models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    message=RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    
class Devis(models.Model):
    message=RichTextUploadingField(blank=True, null=True)  
    def __str__(self):
        return self.message
    
class Expertise(models.Model):
    message=RichTextUploadingField(blank=True, null=True)  
    def __str__(self):
        return self.message
    
class Annonce(models.Model):
    name=models.CharField(max_length=50, null=True)
    description=RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return self.name
    
class ImagesAnnonce(models.Model):
    annonce= models.ForeignKey(Annonce, on_delete=models.CASCADE,null=True)
    images= models.ImageField(upload_to="images_annomces",blank=True, null=True)
    
    def __str__(self):
         return str(self.images)
     
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   
    
#************************* Divertissement ************************


class Zone(models.Model):
    
    name=models.CharField(max_length=100, null=True)
    description=RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
class Divertissement(models.Model):
    departement= models.ForeignKey(Departement, on_delete=models.CASCADE,null=True)
    commune= models.ForeignKey(Commune, on_delete=models.CASCADE,null=True)
    arrondissement= models.ForeignKey(Arrondissement, on_delete=models.CASCADE,null=True)
    quartier=models.ForeignKey(Quartier, on_delete=models.CASCADE,null=True)
    name=models.ForeignKey(Zone, on_delete=models.CASCADE,null=True)
    titre=models.CharField(max_length=100, null=True)
    images=models.ImageField(upload_to="images_divertissement",blank=True, null=True)
    description=RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Qualite(models.Model):
    qualite=models.CharField(max_length=100, null=False)    
    def __str__(self):
        return self.qualite
    
class RejoindreContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    telephone = models.CharField(max_length=20, blank=True, null=True)  # Champ pour le numéro de téléphone
    qualite = models.ForeignKey(Qualite, on_delete=models.SET_NULL, null=True) 
    Photo=models.ImageField(upload_to="photos",blank=True, null=True )  
    piece=models.FileField(upload_to='piece')
    message =models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name