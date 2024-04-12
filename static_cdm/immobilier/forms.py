from django import forms
from multiupload.fields import MultiFileField
from django.forms import ClearableFileInput, FileInput, ModelForm
from Dashboard.models import Categorie
from accounts.models import AuteurUser
from immobilier.models import *


class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = ("nom",)
    nom= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom de la département')
    
class CommuneForm(ModelForm):
    class Meta:
        model = Commune
        fields = ("departement","nom",)
    departement= forms.ModelChoiceField(queryset=Departement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    nom= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom de la Commune')


class ArrondissementForm(ModelForm):
    class Meta:
        model = Arrondissement
        fields = ("commune","nom",)
    commune= forms.ModelChoiceField(queryset=Commune.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    nom= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label="Nom de l'arrondissement")


class QuartierForm(ModelForm):
    class Meta:
        model = Quartier
        fields = ("arrondissement","nom",)
    arrondissement= forms.ModelChoiceField(queryset=Arrondissement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    nom= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom du quartier')
    
    
class OperationFrom(ModelForm):
    class Meta:
        model=Operation
        fields=("type",)
    type= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label="Nom de l'Operation")
        
    
# class ProprietaireForm(ModelForm):
#     class Meta:
#         model = AuteurUser
#         fields = ("last_name","first_name","telephone","adresse","images","piece",)
#     last_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom')
#     first_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='prenom')
#     telephone= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control',}), label='Téléphone')
#     adresse= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Residence')
#     images= forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'name':'images',} ))
#     piece= forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'form-control',} ))


class GroupeForm(ModelForm):
    class Meta:
        model = Types
        fields = ("name",)
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom de la catégorie')

from django import forms
from .models import AuteurUser  # Remplacez par le nom réel de votre modèle

class ProprietaireForm(forms.ModelForm):
    username= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom')
    last_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom')
    first_name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='prenom')
    telephone= forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control',}), label='Téléphone')
    adresse= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Residence')
    images= forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'name':'images',} ))
    piece= forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control',} ))
    class Meta:
        model = AuteurUser
        fields = ("username","last_name","first_name","telephone","adresse","images","piece",) # Remplacez par les champs que vous souhaitez permettre à l'utilisateur de modifier


class ImmeubleForm(ModelForm):
    class Meta:
        model = Immeuble
        fields = ("name","departement","commune","arrondissement","quartier","operation","proprietaire","type","description") # Remplacez par les champs que vous souhaitez permettre à l'utilisateur de modifier

    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Nom de immeulble')
    departement= forms.ModelChoiceField(required=True,queryset=Departement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",  }))
    commune= forms.ModelChoiceField(required=True,queryset=Commune.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    arrondissement= forms.ModelChoiceField(required=True,queryset=Arrondissement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    quartier= forms.ModelChoiceField(required=True,queryset=Quartier.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    operation= forms.ModelChoiceField(required=True,queryset=Operation.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    proprietaire= forms.ModelChoiceField(required=True,queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    description= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Description de immeuble','rows':"5",}))
    type= forms.ModelChoiceField(required=True,queryset=Types.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    
    
# class ImmeubleImagesForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         fields = ['images']
#         widgets = {
#             'images': FileInput(attrs={'multiple': True}),
#         }
# 

class ImmeubleStatutForm(forms.ModelForm):
    class Meta:
        model = Immeuble
        fields = ['statut']
        widgets = {
                'statut': forms.CheckboxInput(attrs={'class': 'form-check-input mx-1', 'checked': False}),
            }
        labels={
            'statut': 'Cliquer pour publier',
        } 
        
class OffreForm(ModelForm):
    class Meta:
        model = Offre
        fields = ("name",)
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label="Nom de l'offre")


# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ("name","email","operation","type","rdv","message",)
#     name= forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control',}
#     ), label='Nom')
#     email= forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control',}), label='Adresse e-mail')
#     operation= forms.ModelChoiceField(queryset=Operation.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}),label='Mise en location ou en vente')
#     type= forms.ModelChoiceField(required=True,queryset=Types.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}),label='Choisez le type de mise ne location ou en vende')
#     message= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Message','rows':"5",}))
#     rdv = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'ex: Lundi 4 septembre 2023 à 11h10',}),label='Prendez-vous avec nous')
    
    
class DevisForm(ModelForm):
    class Meta:
        model = Devis
        fields = ("message",)
    message= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Message','rows':"5",}))


class ExpertiseForm(ModelForm):
    class Meta:
        model = Expertise
        fields = ("message",)
    message= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Message','rows':"10",} ))
    
class ChambreForm(ModelForm):
     class Meta:
         model = Chambre
         fields  =("nombre",)
     nombre=forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de chambre'}), label='Nombre de chambre')
    
class SalonForm(ModelForm):
     class Meta:
         model = Salon
         fields  =("nombre",)
     nombre=forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de salon'}), label='Nombre de Salon')   
     
class CuisineForm(ModelForm):
     class Meta:
         model = Cuisine
         fields  =("nombre",)
     nombre=forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de cuisine'}), label='Nombre de Cuisine') 
     
class DoucheForm(ModelForm):
     class Meta:
         model = Douche
         fields  =("nombre",)
     nombre=forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de douche'}), label='Nombre de douche')  

class BalconForm(ModelForm):
     class Meta:
         model = Balcon
         fields  =("nombre",)
     nombre=forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de balcon'}), label='Nombre de Balcon ')  

class ChambresForm(ModelForm):
    class Meta:
        model = Chambres
        fields = '__all__' 
    proprietaire= forms.ModelChoiceField(required=True,queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    immeuble= forms.ModelChoiceField(required=True,queryset=Immeuble.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='N°')
    prix= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Prix'}))
    salon= forms.ModelChoiceField(required=True,queryset=Salon.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    chambre= forms.ModelChoiceField(required=True,queryset=Chambre.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    cuisine= forms.ModelChoiceField(required=True,queryset=Cuisine.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    douche= forms.ModelChoiceField(required=True,queryset=Douche.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    balcon= forms.ModelChoiceField(required=True,queryset=Balcon.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
   

# class PortesForm(ModelForm):
#     class Meta:
#         model = Porte
#         fields=("proprietaire",)
#     proprietaire= forms.ModelChoiceField(required=True,queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control ",})) 
                             
class AccueilForm(ModelForm):
    class Meta:
        model = Immeuble
        fields = ("type","operation")
    type= forms.ModelChoiceField(required=True,queryset=Types.objects.all(), widget=forms.Select(attrs={'class': "form-control col-6 ",'style': 'width: 300px;',}),label="Choisiez votre type Ex: villa")   
    operation= forms.ModelChoiceField(required=True,queryset=Operation.objects.all(), widget=forms.Select(attrs={'class': "form-control col-6",'style': 'width: 300px; margin-left:2px',}),label="Choisiez votre operation (Location ou Achat)")

class TerrainForm(ModelForm):
    class Meta:
        model = Terrain
        fields = '__all__' 
    departement= forms.ModelChoiceField(required=True,queryset=Departement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",  }))
    commune= forms.ModelChoiceField(required=True,queryset=Commune.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    arrondissement= forms.ModelChoiceField(required=True,queryset=Arrondissement.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    quartier= forms.ModelChoiceField(required=True,queryset=Quartier.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    operation= forms.ModelChoiceField(required=True,queryset=Operation.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    proprietaire= forms.ModelChoiceField(required=True,queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    images= forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'name':'images',}))
    croquis= forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'form-control',} ))
    prix= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Prix'}))
    description= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Description de immeuble','rows':"5",}))
    
class ChambreImagesForm(ModelForm):
    
    class Meta:
        model = Images
        fields = ['images']
        
    images=forms.FileField(required=False,  widget=forms.FileInput(
        attrs={'class':"form-control",'multiple': True}
        ))

class ImmeubleImagesForm(ModelForm):
    
    class Meta:
        model = ImagesImmeuble
        fields = ['images']
        
    images=forms.FileField(required=False,  widget=forms.FileInput(
        attrs={'class':"form-control",'multiple': True}
        ))
    

# class ContactSimpleForm(ModelForm):
#     class Meta:
#         model = Contactez
#         fields = ("name","email","message",)
#     name= forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control',}
#     ), label='Nom')
#     email= forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control',}), label='Adresse e-mail')
#     message= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Message','rows':"5",}))

class PlanForm(ModelForm):

    class Meta:
        model=Plan
        fields = '__all__'
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}), label='Designation du plan')
    proprietaire= forms.ModelChoiceField(required=True,queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control ",}))
    croquis= forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'form-control',} ))
    prix= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Prix'}))
    description= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Description de immeuble','rows':"5",}))

class PlanImagesForm(ModelForm):
    
    class Meta:
        model = ImagesPlan
        fields = ['images']
        
    images=forms.FileField(required=False,  widget=forms.FileInput(
        attrs={'class':"form-control",'multiple': True}
        ))
    
class ContactezNousForm(ModelForm):
    class Meta:
        model = ContactezNous
        fields = '__all__'
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom','style': 'margin-bottom: 10px;'}), label='Nom')
    email= forms.EmailField( widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'margin-bottom: 10px;'}), label='Adresse e-mail',)
    message= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '10','style': 'margin-bottom: 10px;'}))

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['name', 'description']  # Remplacez par les champs réels de votre modèle
    name= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control',}),)
    description= forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control ', 'placeholder': 'Description de immeuble','rows':"5",}))

class AnnonceImagesForm(ModelForm):
    class Meta:
        model = ImagesAnnonce
        fields = ['images']
        
    images=forms.FileField(required=False,  widget=forms.FileInput(
        attrs={'class':"form-control",'multiple': True}
        ))
