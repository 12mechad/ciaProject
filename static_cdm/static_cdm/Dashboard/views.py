
from audioop import reverse
from multiprocessing import context
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
import json
from django.core.paginator import Paginator

from django.views import View
from Dashboard.forms import AuteurForm, CategoryForm, EditionLivreForm
from Dashboard.models import Categorie, EditionContact, EditionLivre, Evenement, EvenementEdition, Thematiques, TypeeDition
from accounts.models import AuteurUser
from cia.forms import UtilisateurForm
from immobilier.forms import ContactezNousForm
# from immobilier.forms import ContactezNousForm
#from immobilier.forms import ContactezNousForm
from immobilier.models import Annonce, Immeuble
from .forms import EditionContactForm, EditionLivreStatutForm, EvenementEditionForm, EvenementForm, ThematiquesForm, TypeeDitionForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import render


def is_admin(user):
    return user.is_authenticated and user.is_staff

def error(request):
    return render(request, 'error-400.html')


def error_auteur(request):
    return render(request, 'error_auteur.html')


def is_auteur(user):
    return user.is_authenticated and user.is_auteur

# context={}
# context["auteurs"]= AuteurUser.objects.order_by('-id')



# Principal Admin
@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def add_categorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("categorie")
    else:
        data={
            'categories': Categorie.objects.all().order_by('-id'),
            'form':CategoryForm()
        }
        return render(request, "add_categorie.html", data)
    
@login_required
def delete(request):
    if request.method=='POST':
        id=request.POST['categorieId']
        Categorie.objects.get(id=int(id)).delete()
    return redirect('categorie')
    
@login_required
def update_category(request, pk):
    if request.method == 'POST':
        id = request.POST['id_category']
        obj = get_object_or_404(Categorie, id=id)
        formCategory= CategoryForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('categorie')
    else:
        obj = get_object_or_404(Categorie, id=pk)
        data={
            'form': CategoryForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modalCategory/modal.html', data)

  
@login_required
def edit_statut(request, pk):
    livre = EditionLivre.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = EditionLivreStatutForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('liste_editions')
    else:
        form = EditionLivreStatutForm(instance=livre)
    
    return render(request, 'publishBook.html', {'form': form,'obj':livre })

@login_required
@user_passes_test(is_auteur, login_url=reverse_lazy('error_auteur'))
def add_auteur(request):
    # Ajouts des auteurs par l'admin
    if request.method=='POST':
        id = request.user.pk
        print(id)
        obj = get_object_or_404(AuteurUser, id=id)
        form= AuteurForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("auteur")
    else:
        id = request.user.pk
        obj = get_object_or_404(AuteurUser, id=id)
        data={
            'form': AuteurForm(instance=obj)
        }

        return render(request, "add_auteur.html",data)
    
# Selction des livre pour la page notre librairie 
def select_livre(request):
    editer=EditionLivre.objects.all()
    context={
          'editers':editer,
        
    }
    return render(request, 'edition/librairie.html',context)


@login_required  # Utilisez ce décorateur pour s'assurer que seul un utilisateur connecté peut accéder à cette vue
def editer(request):
    form = EditionLivreForm
    if request.method == 'POST':
        form = EditionLivreForm(request.POST, request.FILES)
        if form.is_valid():
            livre = form.save(commit=False)  # Ne sauvegardez pas encore l'objet
            livre.auteur = request.user  # Définissez l'auteur sur l'utilisateur connecté
            livre.save()  # Maintenant, enregistrez l'objet avec l'auteur défini
            return redirect("liste_editions")
    else:
        form = EditionLivreForm()
    return render(request, 'editer.html', {'form': form})

@login_required  # Utilisez ce décorateur pour s'assurer que seul un utilisateur connecté peut accéder à cette vue
def list_contacts(request):
   
    context ={
            'contacts':EditionContact.objects.all().order_by('-id')
        }
    return render(request, 'liste_contact.html', context)


# Modifiecation des editions
@login_required
def update_edition(request,pk):
    if request.method=='POST':
        id=id = request.POST['id_edition']
        obj = get_object_or_404(EditionLivre, id=id)
        formEdition = EditionLivreForm(request.POST, request.FILES, instance=obj)
        if formEdition.is_valid():
            formEdition.save()
            return redirect('liste_editions')
    else:
        obj = get_object_or_404(EditionLivre, id=pk)
        context={
            'form': EditionLivreForm(instance=obj),
            'obj': obj}
        return render(request, 'update_edition.html',context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_edition(request,):
    if request.method=='POST':
        id=request.POST['editionId']
        EditionLivre.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('liste_editions')  



@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def statut(request, statut_id):
    if request.method=="POST":
        statut=request.POST['categorieId']
        print(statut)
        statut = get_object_or_404(EditionLivre, pk=statut_id)
        statut.valeur = 1  # Mettre à jour la valeur du statut
        statut.save()      # Sauvegarder les modifications
        return redirect('liste_editions')  # Rediriger vers la vue appropriée
        
#Formulaire de conntact 

@login_required
def contact_view(request):
    #if request.method == 'POST':
        # form = ContactezNousForm(request.POST)
        # if form.is_valid():
        #     nom = form.cleaned_data['nom']
        #     email = form.cleaned_data['email']
        #     message = form.cleaned_data['message']
            
        #     sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
        #     contenu = f"De : {email}\nMessage : {message}"
        #     destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
        #     send_mail(sujet, contenu, email, destinataires)
            
        #     return render(request, 'contact/success.html')
    
        # # form = ContactezNousForm()
    
    return render(request, 'contact/contact.html')

#afficher les informations sur la page d'accueil
# @login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('error'))
# def accueil(request):
#     librairie=EditionLivre.objects.all()
#     return render(request,'edition.librairie.html', context={"librairie":librairie})

#  Autentification
def inscription(request):
    if request.method=="POST":
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            return HttpResponse( 'categorie')
    else:
        form = UtilisateurForm()

        return render(request, 'inscription.html', {"form": form})

 #Editeur ajouter des edition


# @login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('error'))
# def publicationAdmin(request):
#     context={
#         'auteurs':AuteurUser.objects.all().order_by('-pk')
#     }
#     return render(request, 'liste_auteurs.html',context)

@login_required
def publicationAdmin(request):
    auteurs_list = AuteurUser.objects.all().order_by('-pk')
    paginator = Paginator(auteurs_list, 2)  # Afficher 10 auteurs par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'auteurs': page_obj,
    }
    return render(request, 'liste_auteurs.html', context)


@login_required
def listEdition(request):
    data={
        'listEditions':EditionLivre.objects.filter(auteur=request.user).order_by('-id')
    }
    return render(request, 'liste_edition.html',data)
#Pour Gérer la liste des livres publiée par un m'auteur

def listesEdition(request,id):
   
        auteur=AuteurUser.objects.get(id=id)
        livresauteurs=EditionLivre.objects.filter(auteur=auteur).order_by('-id')
        context={
            'livresauteurs':livresauteurs
        }
        return render(request, 'listes_editions.html',context)

# Utilisateur
@login_required
@user_passes_test(is_auteur, login_url=reverse_lazy('error'))
def auteur(request):
      context={
        'auteurs':AuteurUser.objects.all()
    }
      return render(request, 'utilisateur/auteur.html',context)

def editeur(request):
    return render(request, 'utilisateur/editer.html')

def publication(request):
    return render(request, 'utilisateur/list_publication.html')

# Accueil pour le site l'edition

# fonction pour la page d'accueil
def accueil(request):
    if request.method == 'POST':
        form = ContactezNousForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'contact/success.html')
    else:
        context={
            'accueils':EditionLivre.objects.all().order_by('-id'),
            'form':ContactezNousForm()
        }
    
    return render(request, 'edition/accueil.html',context)

def propos(request):
    if request.method == 'POST':
        form = ContactezNousForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'contact/success.html')
    else:
        
     
        context={
            
            'form' : ContactezNousForm()

        }
    
    return render(request, 'edition/propos.html',context)

def editions(request):
    context={
            'accueils':EditionLivre.objects.all().order_by('-id'),
            
        }
    return render(request, 'edition/editions.html',context)


def edition(request):
    if request.method == 'POST':
        form = form = EditionContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('edition')  
    else:
        form = EditionContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'edition/edition.html', context)


# fonction pour la page vue client pour de notre librairie
def librairie(request): 
    editer=EditionLivre.objects.all()
    context={
          'editers':editer,     
    }
    return render(request, 'edition/librairie.html',context)

# fonction pour la page vue client pour de nos contact
def contact(request):
    if request.method == 'POST':
        form = ContactezNousForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'contact/success.html')
    else:
        # if request.method == 'POST':
        #     nom = request.POST.get('nom', '')
        #     email = request.POST.get('email', '')
        #     message_text = request.POST.get('message', '')

        #     # Valider le formulaire (vous pouvez ajouter vos propres règles de validation ici)

        #     # Sauvegarder le message dans la base de données
        #     message = ContactezNousForm(nom=nom, email=email, message=message_text)
        #     message.save()

        #     # Envoyer l'e-mail
        #     send_mail(
        #         'Nouveau message de contact',
        #         f'Nom: {nom}\nEmail: {email}\nMessage: {message_text}',
        #         email,  # Expéditeur (utilisation de l'adresse e-mail fournie dans le formulaire)
        #         ['secretariat@ciagroupafrica.com'],  # Destinataire (remplacez par votre adresse e-mail de destinataire)
        #         fail_silently=False,
        #     )

        #     # Rediriger après l'envoi du formulaire
        #     return HttpResponseRedirect(reverse('confirmation_contact'))

        return render(request, 'edition/contact.html')
    

# fonction pour la page vue client pour de notre librairie
def mod(request):
    return render(request, 'edition/modal.html')

# fonction pour la page vue client pour nos auteurs

def listes_auteurs(request):
     context={
        'auteurss':AuteurUser.objects.all()
    }
     return render(request, 'edition/auteurs.html',context)
   

# fonction pour la page vue client pour nos auteurs
def blogAuteurs(request,id):
     context={
        'detailauteur':AuteurUser.objects.get(id=id)
    }
    
     return render(request, 'edition/blog_auteurs.html',context)

# fonction pour la page vue client pour nos auteurs
def detailblog(request,id):
    context={
        'categorie':Categorie.objects.get(id=id)
    }
    return render(request, 'edition/detail_blog.html')

# fonction pour la page deatail des actualité
def DetailActualite(request,id):
    context={
        'detail':EditionLivre.objects.get(id=id)
    }
    
    return render(request, 'edition/detail_actualite.html',context)
# Fin accueil pour le site d'edition


#La principale de Ciagroup
# fonction pour la page deatail des actualité
def agenda(request):
    if request.method == 'POST':
        form = ContactezNousForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'contact/success.html')
    else:
        
     
        context={
            'editions':EditionLivre.objects.all().order_by("id")[:6],
            'immeubles': Immeuble.objects.all().order_by('-id')[:6],
            'annonces': Annonce.objects.all().order_by('-id'),
            'form' : ContactezNousForm()

        }
        return render(request, 'ciagroup/agenda.html',context)
 
def detaille(request,id):
    context={
        'detaille':EditionLivre.objects.get(id=id)
    }
    # print(EditionLivre.objects.get(id=id))
    return render(request, 'ciagroup/detaille.html',context)

# fonction pour la page a propos de l'agenda
def propos_agenda(request):
    if request.method == 'POST':
        form = ContactezNousForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['votre@email.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'contact/success.html')
    else:
        
     
        context={
            
            'form' : ContactezNousForm()

        }

    return render(request, 'ciagroup/propos.html',context)

# fonction pour la page a servece de l'agenda
def service_agenda(request):
    return render(request, 'ciagroup/service.html')





#########################################################
                #  Les fonction relative au investissement


########################## Presse ########################
def presse(request):
    return render(request, 'presse/presse.html')

##################### evénements ########################

def evenement(request):
    return render(request, 'evenement/evenement.html')




@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def typeEvenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("type_evenement")
    else:
        data={
            'Evenements': Evenement.objects.all().order_by('-id'),
            'form':EvenementForm()
        }
        return render(request, "typeEvenement.html", data)
 # Utilisez ce décorateur pour s'assurer que seul un utilisateur connecté peut accéder à cette vue
def evenementEdition(request):
    form = EvenementEditionForm
    if request.method == 'POST':
        form = EvenementEditionForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect("evenement_Edition")
    else:
        context={
            'listeEvenements': EvenementEdition.objects.all().order_by('-id'),
            'form': EvenementEditionForm(),
        }
        return render(request, 'evenement_edition.html', context)

def prix(request):
    context={
            'listePrixs': EvenementEdition.objects.all().order_by('-id'),
        }
    return render(request,'evenement/prix.html',context)

def festival(request):
    context={
            'listeFestivals': EvenementEdition.objects.all().order_by('-id'),
        }
    return render(request,'evenement/festival.html',context)

def projet(request):
    context={
            'listeProjets': EvenementEdition.objects.all().order_by('-id'),
        }
    return render(request,'evenement/projet.html',context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def Type_edition(request):
    if request.method == 'POST':
        form = TypeeDitionForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("Type_edition")
    else:
        data={
            'TypeeDitions': TypeeDition.objects.all().order_by('-id'),
            'form':TypeeDitionForm()
        }
        return render(request, "Type_edition.html", data)
    
@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def thematiques(request):
    if request.method == 'POST':
        form = ThematiquesForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("thematiques")
    else:
        data={
            'Thematiques': Thematiques.objects.all().order_by('-id'),
            'form':ThematiquesForm()
        }
        return render(request, "thematiques.html", data)