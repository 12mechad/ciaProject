from django.contrib.auth.models import User
from django.db import models

from django.conf import settings

from accounts.models import AuteurUser
# from ckeditor.fields import RichTextField
from  ckeditor_uploader.fields import RichTextUploadingField

# from accounts import forms

# from accounts.models import AuteurUser

# Create your models here.
   
class Categorie(models.Model):
    name=models.CharField(max_length=100, null=False)
    description=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    

    
class EditionLivre(models.Model):
    categorie=models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True) 
    auteur=models.ForeignKey(AuteurUser,on_delete=models.CASCADE,null=True)
    titre=models.CharField(max_length=200)
    prix=models.IntegerField(null=True)
    images=models.ImageField(upload_to="images",blank=True, null=True )  
    pdf_file=models.FileField(upload_to='pdfs')
    description=RichTextUploadingField(blank=True, null=True)
    statut=models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.titre
    


class Evenement(models.Model):
    evenement=models.CharField(max_length=200)

    def __str__(self):
        return self.evenement
    
class EvenementEdition(models.Model):
    titre = models.CharField(max_length=200)
    evenement=models.ForeignKey(Evenement, on_delete=models.SET_NULL, null=True) 
    date_evenement = models.DateTimeField()  
    images = models.ImageField(upload_to="images", blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
   
    def __str__(self):
        return self.titre


class Thematiques(models.Model):
    titre =models.CharField(max_length=100)

    def __str__(self):
        return self.titre

class TypeeDition(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

from django.db import models

class EditionContact(models.Model):
    name = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    telephone = models.CharField(max_length=20, blank=True, null=True)  # Champ pour le numéro de téléphone
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True) 
    thematique = models.ForeignKey(Thematiques, on_delete=models.SET_NULL, null=True) 
    typeedition = models.ForeignKey(TypeeDition, on_delete=models.SET_NULL, null=True)
    soumettre = models.FileField(upload_to='documents/')  # Champ pour le fichier Word
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

#***************************************Presse**********************
class CategoriePresse(models.Model):
    name=models.CharField(max_length=100, null=False)
    description=models.TextField(blank=True, null=True)
    date=models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.name

class RevusPresse(models.Model):
    titre = models.CharField(max_length=200)
    categories=models.ForeignKey(CategoriePresse, on_delete=models.SET_NULL, null=True) 
    images = models.ImageField(upload_to="images", blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
   
    def __str__(self):
        return self.titre
    
class DocumentairePresse(models.Model):
    titre = models.CharField(max_length=200)
    categories=models.ForeignKey(CategoriePresse, on_delete=models.SET_NULL, null=True) 
    images = models.ImageField(upload_to="images", blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
   
    def __str__(self):
        return self.titre

class InterviewPresse(models.Model):
    titre = models.CharField(max_length=200)
    categories=models.ForeignKey(CategoriePresse, on_delete=models.SET_NULL, null=True) 
    images = models.ImageField(upload_to="images", blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
   
    def __str__(self):
        return self.titre


class Qualite(models.Model):
    name=models.CharField(max_length=100, null=False)    
    def __str__(self):
        return self.name
    
class RejoindrContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    telephone = models.CharField(max_length=20, blank=True, null=True)  # Champ pour le numéro de téléphone
    qualite = models.ForeignKey(Qualite, on_delete=models.SET_NULL, null=True) 
    images=models.ImageField(upload_to="photos",blank=True, null=True )  
    piece=models.FileField(upload_to='piece')
    message =models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class CommanderEdition(models.Model):
    name = models.CharField(max_length=100, null=False)
    adresse = models.EmailField(null=False)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=False)
    quantite = models.IntegerField(null=True)

    def __str__(self):
        return self.name