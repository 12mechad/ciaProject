from django import forms

from .models import *
from django.forms import ModelForm
from django import forms
from .models import Categorie,EditionLivre,Evenement
# from accounts.models import AuteurUser
# from django.contrib.auth.forms import UserCreationForm

class AuteurForm(ModelForm):
    class Meta:
        model = ''
        fields = ('last_name','email','first_name','telephone','biographie','bibliographie','images')
    last_name= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control col-12', 'placeholder': 'last_name','id':'complaintinput1'}
         ))
    email= forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control col-12', 'placeholder': 'Email','id':'complaintinput1'}
         ))
    first_name= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control col-12', 'placeholder': 'first_name',}
         ))
    telephone= forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control col-12', 'placeholder': 'Téléphone',}
         ))
    biographie= forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control col-12', 'placeholder': 'biographie','rows':"5"}
         ))
    bibliographie= forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control col-12', 'placeholder': 'bibliographie','rows':"5",}
         ))
    images= forms.ImageField(required=True, widget=forms.FileInput(
        attrs={'class': 'form-control col-12', 'name':'images',}
         ))
    

class CategoryForm(ModelForm):
    class Meta:
        model = Categorie
        fields= ("name",)
    name= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control',}
    ), label='Nom de la catégorie:')
    


from ckeditor.widgets import CKEditorWidget


class EditionLivreForm(forms.ModelForm):
   

    class Meta:
        model = EditionLivre
        fields = ('auteur', 'titre', 'prix', 'images', 'pdf_file', 'categorie', 'description')
        
    auteur = forms.ModelChoiceField(required=True, queryset=AuteurUser.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    prix = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control col-12', 'placeholder': 'Prix'}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    pdf_file = forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12'}))
    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={'class': 'form-control col-12', 'placeholder': 'Description du livre', 'rows': '5'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personnaliser les choix du champ auteur avec le nom et le prénom
        self.fields['auteur'].label_from_instance = lambda obj: f"{obj.last_name} {obj.first_name}"

    
class EditionLivreStatutForm(forms.ModelForm):
    class Meta:
        model = EditionLivre
        fields = ['statut']
        widgets = {
                'statut': forms.CheckboxInput(attrs={'class': 'form-check-input mx-1', 'checked': False}),
            }
        labels={
            'statut': 'Cliquer pour publier',
        }

     

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ['typeEvenement']
    typeEvenement = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': "Type d'evenement", 'id': 'complaintinput1'}))


class DateInput(forms.DateInput):
    input_type = 'date'

class EvenementEditionForm(forms.ModelForm):
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    date_evenement = forms.DateField(required=True, widget=DateInput(attrs={'class':'form-control', 'name':'date', 'id':'timesheetinput3' }))
    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={'class': 'form-control col-12', 'placeholder': 'Description du livre', 'rows': '5'}))

    class Meta:
        model = EvenementEdition
        fields = '__all__'



class ThematiquesForm(forms.ModelForm):
    class Meta:
        model = Thematiques
        fields = '__all__'
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': "Type d'evenement", 'id': 'complaintinput1'}))

class TypeeDitionForm(forms.ModelForm):
    class Meta:
        model = TypeeDition
        fields = '__all__'
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': "Type d'evenement", 'id': 'complaintinput1'}))




from django import forms
from .models import EditionContact

class EditionContactForm(forms.ModelForm):
    class Meta:
        model = EditionContact
        fields = ('name', 'titre', 'email', 'telephone', 'categorie', 'thematique', 'typeedition', 'soumettre', 'message')

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Nom et Prenom'}))
    titre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Titre du manuscrit'}))
    telephone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Téléphone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Email'}))
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all(), widget=forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}))
    thematique = forms.ModelChoiceField(queryset=Thematiques.objects.all(), widget=forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}))
    typeedition = forms.ModelChoiceField(queryset=TypeeDition.objects.all(), widget=forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}))
    soumettre = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control border-0 p-4'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Message'}))

