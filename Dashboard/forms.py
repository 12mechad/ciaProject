from django import forms

from .models import *
from django.forms import ModelForm
from django import forms
from .models import Categorie,EditionLivre
from ckeditor.widgets import CKEditorWidget
from ckeditor.widgets import CKEditorWidget



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
    biographie= forms.CharField(required=True,  widget=CKEditorWidget(
        attrs={'class': 'form-control col-12', 'placeholder': 'biographie','rows':"5"}
         ))
    bibliographie= forms.CharField(required=True,  widget=CKEditorWidget(
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
    


from django import forms
from .models import EditionLivre, AuteurUser

class EditionLivreForm(forms.ModelForm):
    class Meta:
        model = EditionLivre
        fields = ('auteur', 'titre', 'prix', 'images', 'pdf_file', 'categorie', 'description')
        
    auteur = forms.ModelChoiceField(required=True, queryset=AuteurUser.objects.filter(is_auteur=True), widget=forms.Select(attrs={'class':"form-control col-12"}))
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
        fields = ['evenement']
    evenement = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': "Type d'evenement", 'id': 'complaintinput1'}))




class DateInput(forms.DateInput):
    input_type = 'date'

class EvenementEditionForm(forms.ModelForm):
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    evenement = forms.ModelChoiceField(queryset=Evenement.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
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

#**********************************Presse*******************************************
class CategoryPresseForm(ModelForm):
    class Meta:
        model = CategoriePresse
        fields= ("name",)
    name= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control',}
    ), label='Nom de la catégorie:')

class RevusPresseForm(forms.ModelForm):
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    categories = forms.ModelChoiceField(queryset=CategoriePresse.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={'class': 'form-control col-12', 'placeholder': 'Description du livre', 'rows': '5'}))

    class Meta:
        model = RevusPresse
        fields = '__all__'
    
class DocumentairePresseForm(forms.ModelForm):
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    categories = forms.ModelChoiceField(queryset=CategoriePresse.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={'class': 'form-control col-12', 'placeholder': 'Description du livre', 'rows': '5'}))

    class Meta:
        model = DocumentairePresse
        fields = '__all__'

class InterviewPresseForm(forms.ModelForm):
    titre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control col-12', 'placeholder': 'Titre', 'id': 'complaintinput1'}))
    categories = forms.ModelChoiceField(queryset=CategoriePresse.objects.all(), widget=forms.Select(attrs={'class':"form-control col-12"}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={'class': 'form-control col-12', 'placeholder': 'Description du livre', 'rows': '5'}))

    class Meta:
        model = InterviewPresse
        fields = '__all__'


class RejoindreContactForm(forms.ModelForm):
    class Meta:
        model = RejoindrContact
        fields = '__all__'

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Nom et Prenom'}))
    telephone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Téléphone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Email'}))
    qualite = forms.ModelChoiceField(queryset=Qualite.objects.all(), widget=forms.Select(attrs={'class': 'custom-select border-0 px-4', 'style': 'height: 47px;'}))
    images = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12', 'name': 'images'}))
    piece = forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'form-control col-12'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Message'}))

class QualiteForm(ModelForm):
    class Meta:
        model = Qualite
        fields= ("name",)
    name= forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control',}
    ), label='Nom de la catégorie:')


class CommanderEditionFrom(ModelForm):
    class Meta:
        model = CommanderEdition
        fields = '__all__'
    name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Nom et Prenom'}))
    adresse= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4','placeholder': 'Adresse de Livraison'}))
    telephone= forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Téléphone'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Email'}))
    quantite= forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Quantité à Commander'}))
