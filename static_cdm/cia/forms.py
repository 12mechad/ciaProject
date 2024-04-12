from django import forms 

class UtilisateurForm(forms.Form):
    nom =forms.CharField( max_length= 200, required=True, strip=True)
    prenom =forms.CharField( max_length=200, required=True,strip=True)
    email= forms.EmailField()
    password1 =forms.CharField(max_length=10, required=True, widget=forms.PasswordInput())
    password2 =forms.CharField(max_length=10, required=True,  widget=forms.PasswordInput())
    cgu_accept =forms.BooleanField(initial=True)


class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)