
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
from Dashboard.models import Categorie, CategoriePresse, DocumentairePresse, EditionContact, EditionLivre, Evenement, EvenementEdition, InterviewPresse, Qualite, RejoindrContact,  RevusPresse,  Thematiques, TypeeDition
from accounts.models import AuteurUser
from cia.forms import UtilisateurForm
from immobilier.forms import ContactezNousForm
from immobilier.models import Annonce, Immeuble
from .forms import CategoryPresseForm, DocumentairePresseForm, EditionContactForm, EditionLivreStatutForm, EvenementEditionForm, EvenementForm, InterviewPresseForm, QualiteForm, RejoindreContactForm, RevusPresseForm,  ThematiquesForm, TypeeDitionForm
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
    auteurs_list = AuteurUser.objects.filter(is_auteur=True).order_by('-pk')
    paginator = Paginator(auteurs_list, 10)  # Afficher 10 auteurs par page

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
            nom = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['agenda@ciagroupafrica.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'edition/accueil.html')
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
            nom = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['agenda@ciagroupafrica.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'edition/propos.html')
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
            nom = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['agenda@ciagroupafrica.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'edition/accueil.html')
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
        'auteurss': AuteurUser.objects.filter(is_auteur='True').order_by('-id')
    }
     return render(request, 'edition/auteurs.html',context)

def detail_auteurs(request, auteur_id):
    auteur = AuteurUser.objects.get(pk=auteur_id)
    context={
        'detailAuteur': auteur
    }
    return render(request, "edition/detail_auteur.html", context)

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
            nom = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['agenda@ciagroupafrica.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'ciagroup/agenda.html')
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
            nom = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            sujet = f"Nouveau message depuis le formulaire de contact de {nom}"
            contenu = f"De : {email}\nMessage : {message}"
            destinataires = ['agenda@ciagroupafrica.com']  # Liste des adresses e-mail
            
            send_mail(sujet, contenu, email, destinataires)
            
            return render(request, 'ciagroup/propos.html')
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
                            #Presse-clients#
def presse(request):
    context={
        'revus':RevusPresse.objects.all().order_by('-id')[:1],
        'revuss':RevusPresse.objects.all().order_by('-id')[:3],
        'documentaire':DocumentairePresse.objects.all().order_by('-id')[:3],
        'interview':InterviewPresse.objects.all().order_by('-id')[:3],

    }
    return render(request, 'presse/press.html',context)

def revus(request):
    context={
        'revus':RevusPresse.objects.all().order_by('-id')[:1],
        'revuss':RevusPresse.objects.all().order_by('-id')[:10],
        'categories':Categorie.objects.all().order_by('-id')[:10]

    }
    return render(request, 'presse/revus.html',context)


def documentaire(request):
    context={
        'documentaires': DocumentairePresse.objects.all().order_by('-id')[:1],
        'documentaire':DocumentairePresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/documentaire.html',context)


def interviews(request):
    context={
        'interviews':InterviewPresse.objects.all().order_by('-id')[:1],
        'interview':InterviewPresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/interviews.html',context)

#-------------------------Revus------------------------
def categories_interview(request,pk):
    context={
        'interviews':InterviewPresse.objects.all().order_by('-id')[:1],
        'interview':InterviewPresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/categories/categories_interview.html',context)

def categories_revus(request,pk):
    context={
        'revus':RevusPresse.objects.all().order_by('-id')[:1],
        'revuss':RevusPresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]

    }
    return render(request, 'presse/categories/categories_revus.html',context)

def categories_documentaire(request,pk):
    context={
        'documentaires': DocumentairePresse.objects.all().order_by('-id')[:1],
        'documentaire':DocumentairePresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/categories/categories_documentaire.html',context)





#--------------------------------------Recent------------------------------------
def recent_documentaire(request,pk):
    context={
        'documentaires': DocumentairePresse.objects.get(pk=pk),
        'documentaire':DocumentairePresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/recent/recent_documentaire.html',context)

def recent_revus(request,pk):
    context={
        'revus':RevusPresse.objects.get(pk=pk),
        'revuss':RevusPresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]

    }
    return render(request, 'presse/recent/recent_revus.html',context)


def recent_interview(request,pk):
    context={
        'interviews':InterviewPresse.objects.get(pk=pk),
        'interview':InterviewPresse.objects.all().order_by('-id')[:10],
        'categories':CategoriePresse.objects.all().order_by('-id')[:10]
    }
    return render(request, 'presse/recent/recent_interview.html',context)

                                    #Presse Admin#
def categories_presse(request):
    if request.method == 'POST':
        form = CategoryPresseForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("categories_presse")
    else:
        data={
            'categories': CategoriePresse.objects.all().order_by('-id'),
            'form':CategoryPresseForm()
        }
    return render(request, 'categories_presse.html',data)

def revus_presse(request):
    form = RevusPresseForm
    if request.method == 'POST':
        form = RevusPresseForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect("revus_presse")
    else:
        context={
           
            'form': RevusPresseForm(),
        }
    return render(request, 'revus_presse.html',context)

def liste_revus(request):
    context={
                       
            'listerevus':RevusPresse.objects.all().order_by('-id'),
        }
    return render(request, 'liste_revus.html',context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_revus(request,):
    if request.method=='POST':
        id=request.POST['revusId']
        RevusPresse.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('liste_revus') 

@login_required
def update_revus(request,pk):
    if request.method=='POST':
        id=id = request.POST['id_revus']
        obj = get_object_or_404(RevusPresse, id=id)
        formrevus = RevusPresseForm(request.POST, request.FILES, instance=obj)
        if formrevus.is_valid():
            formrevus.save()
            return redirect('liste_revus')
    else:
        obj = get_object_or_404(RevusPresse, id=pk)
        context={
            'form': RevusPresseForm(instance=obj),
            'obj': obj}
        return render(request, 'update_revus.html',context)

def documentaire_presse(request):
    form = DocumentairePresseForm
    if request.method == 'POST':
        form = DocumentairePresseForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect("documentaire_presse")
    else:
        context={
           
            'form': DocumentairePresseForm(),
        }
    return render(request, 'documentaire_presse.html',context)

def liste_documentaire(request):
    context={
                       

            'listedocumentaires':DocumentairePresse.objects.all().order_by('-id'),
        }
    return render(request, 'liste_documentaire.html',context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_documentaire(request,):
    if request.method=='POST':
        id=request.POST['documentaireId']
        DocumentairePresse.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('liste_documentaire')  


@login_required
def update_documentaire(request,pk):
    if request.method=='POST':
        id=id = request.POST['id_documentaire']
        obj = get_object_or_404(DocumentairePresse, id=id)
        formdocumentaire = DocumentairePresseForm(request.POST, request.FILES, instance=obj)
        if formdocumentaire.is_valid():
            formdocumentaire.save()
            return redirect('liste_documentaire')
    else:
        obj = get_object_or_404(DocumentairePresse, id=pk)
        context={
            'form': DocumentairePresseForm(instance=obj),
            'obj': obj}
        return render(request, 'update_documentaire.html',context)
    
def interview_presse(request):
    form = InterviewPresseForm
    if request.method == 'POST':
        form = InterviewPresseForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect("interview_presse")
    else:
        context={
           
            'form': InterviewPresseForm(),
        }
    return render(request, 'interview_presse.html',context)

def liste_interview(request):
    context={
                       

            'listerinterviews':InterviewPresse.objects.all().order_by('-id'),
        }
    return render(request, 'liste_interview.html',context)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_interview(request,):
    if request.method=='POST':
        id=request.POST['interviewId']
        InterviewPresse.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('liste_interview')  


@login_required
def update_interview(request,pk):
    if request.method=='POST':
        id=id = request.POST['id_interview']
        obj = get_object_or_404(InterviewPresse, id=id)
        forminterview = InterviewPresseForm(request.POST, request.FILES, instance=obj)
        if forminterview.is_valid():
            forminterview.save()
            return redirect('liste_interview')
    else:
        obj = get_object_or_404(InterviewPresse, id=pk)
        context={
            'form': InterviewPresseForm(instance=obj),
            'obj': obj}
        return render(request, 'update_interview.html',context)


##################### evénements ########################

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def evenemen(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("evenemen")
    else:
        data={
            'pris': Evenement.objects.all().order_by('-id'),
            'form':EvenementForm()
        }
        return render(request, "evenement.html", data)
    
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
           
            'form': EvenementEditionForm(),
        }
        return render(request, 'evenement_edition.html', context)
    
@login_required
def liste_evenemenent(request):
    data={
        'listeEvenements': EvenementEdition.objects.all().order_by('-id'),
    }
    return render(request, 'list_evenement.html',data)


##################### evénements ########################

def evenement(request):
    context ={
        'evenements': EvenementEdition.objects.all().order_by('-id')[:9],
        }
    return render(request, 'evenement/evenement.html',context)


def prix(request):
    evenements_prix = EvenementEdition.objects.filter(evenement__evenement='Prix').order_by('-id')[:9]
    context = {
        'listePrixs': evenements_prix,
    }
    return render(request, 'evenement/prix.html', context)

def festival(request):
    evenements_festival = EvenementEdition.objects.filter(evenement__evenement='Salons/Festivals').order_by('-id')[:9]
    context={
            'listeFestivals': evenements_festival
        }
    return render(request,'evenement/festival.html',context)


def projet(request):
    evenements_projet = EvenementEdition.objects.filter(evenement__evenement='Projets').order_by('-id')[:9]
    context={
            'evenementsProjets': evenements_projet
        }
    return render(request,'evenement/projet.html',context)


def detail_evenement(request, evenement_id):
    evenements = get_object_or_404(EvenementEdition, pk=evenement_id)
    context = {
        'evenements': evenements,
    }
    return render(request, 'evenement/detail_evenement.html', context)

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


@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error')) 
def contact_editer(request):
    context = {
        'EditionContacts': EditionContact.objects.all().order_by('-id'),
    }
    return render(request, 'contact_editer.html', context)


@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_contactediter(request,):
    if request.method=='POST':
        id=request.POST['EditionContactsId']
        EditionContact.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('contact_editer')  
    

#----------------------------------Rejondre notre equipe ------------------------------


def rejoindre(request):
    if request.method == 'POST':
        form = RejoindreContactForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("rejoindre")
    else:
        context = {
            'form': RejoindreContactForm()
        }

    return render(request, 'edition/rejoindre.html', context)


def liste_rejoindre(request):
        context={
                    'listeRejoindres':RejoindrContact.objects.all().order_by('-id')
                }
        return render(request,'liste_rejoindre.html',context)

def qualite(request):
    if request.method == 'POST':
        form = QualiteForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("qualite")
    else:
        data={
            'categories': Qualite.objects.all().order_by('-id'),
            'form':QualiteForm()
        }
    return render(request, 'qualite.html',data)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_rejoindre(request,):
    if request.method=='POST':
        id=request.POST['rejoindreId']
        RejoindrContact.objects.get(id=int(id)).delete()
        # return redirect('liste_edition')
    return redirect('liste_rejoindre') 