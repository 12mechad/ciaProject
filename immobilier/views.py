from operator import attrgetter
import platform
from django.http import Http404, HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from Dashboard.views import auteur, is_admin
from accounts.models import AuteurUser
from django.contrib.auth.models import User
from accounts.forms import CustomUserCreationForm
from immobilier.utile import send_email_with_html_body 
from django.contrib.auth.decorators import login_required,user_passes_test, permission_required
from .decorators import group_required
from django.contrib import messages
from .forms import ProprietaireForm  
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.urls import reverse_lazy
import json
from django.core.mail import send_mail


def creat_views(request):
    if request.method =="POST":     
        email= request.POST.get('email')

        subjet = "Test Email "
        template ='email.html'
        context={
            'date': datetime.today().date,
            'email': email
        }
        receivers =[email]
        

        has_sent=send_email_with_html_body(
            subjet=subjet,
            receivers=receivers,
            template=template,
            context= context)
        if has_sent:

            return render(request, 'Email envoyé  avec success',    ) 
        return render(request,'interface/accueil.html')

@login_required
# @user_passes_test(is_admin, login_url=reverse_lazy('error'))
def index(request):
    
    return render(request,'dashboards/index.html')


@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def departement(request):
    if request.method == 'POST':
         form = DepartementForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("departement")
    else:
        data={
           'departements': Departement.objects.all().order_by('-id'),
           'form':DepartementForm()
        }
    return render(request,'dashboards/departement.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_departement(request, pk):
    if request.method == 'POST':
        id = request.POST['id_departement']
        obj = get_object_or_404(Departement, id=id)
        formCategory= DepartementForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('departement')
    else:
        obj = get_object_or_404(Departement, id=pk)
        data={
            'form': DepartementForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_departement.html', data)

#******************************** Commune ***************************#
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def commune(request):
    if request.method == 'POST':
         form = CommuneForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("commune")
    else:
        data={
           'communes': Commune.objects.all().order_by('-id'),
           'form':CommuneForm()
        }
    return render(request,'dashboards/commune.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_commune(request, pk):
    if request.method == 'POST':
        id = request.POST['id_commune']
        obj = get_object_or_404(Commune, id=id)
        formCategory= CommuneForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('commune')
    else:
        obj = get_object_or_404(Commune, id=pk)
        data={
            'form': CommuneForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_commune.html', data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def arrondissement(request):
    if request.method == 'POST':
         form = ArrondissementForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("arrondissement")
    else:
        data={
           'arrondissements': Arrondissement.objects.all().order_by('-id'),
           'form':ArrondissementForm()
        }
    return render(request,'dashboards/arrondissement.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_arrondissement(request, pk):
    if request.method == 'POST':
        id = request.POST['id_arrondissement']
        obj = get_object_or_404(Arrondissement, id=id)
        formCategory= ArrondissementForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('arrondissement')
    else:
        obj = get_object_or_404(Arrondissement, id=pk)
        data={
            'form': ArrondissementForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_arrondissement.html', data)

    #*************************Quartier**********************************#
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def quartier(request):
    if request.method == 'POST':
         form = QuartierForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("quartier")
    else:
        data={
           'quartiers': Quartier.objects.all().order_by('-id'),
           'form':QuartierForm()
        }
    return render(request,'dashboards/quartier.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_quartier(request, pk):
    if request.method == 'POST':
        id = request.POST['id_quartier']
        obj = get_object_or_404(Quartier, id=id)
        formCategory= QuartierForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('quartier')
    else:
        obj = get_object_or_404(Quartier, id=pk)
        data={
            'form': QuartierForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_quartier.html', data)
    
#************************** Divertissement *************************
    
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def zone(request):
    if request.method == 'POST':
         form = ZoneForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("zone")
    else:
        data={
           'zones': Zone.objects.all().order_by('-id'),
           'form':ZoneForm()
        }
    return render(request,'dashboards/zone.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def divertissement(request):
    if request.method == 'POST':
        form = DiverdissementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('divertissement')
    else:
        data = {
            'form':DiverdissementForm(),
             }
        return render(request,'dashboards/divertissement.html',data)

#****************************** Types ************************
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def types(request):
    if request.method=="POST":
        form =GroupeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("types")
    else:
        data={
           'groupes': Types.objects.all().order_by('-id'),
           'form':GroupeForm()
        }
        return render(request,'dashboards/types.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deletetypes(request):
    if request.method=='POST':
        id=request.POST['typesId']
        Types.objects.get(id=int(id)).delete()
    return redirect('types')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_types(request, pk):
    if request.method == 'POST':
        id = request.POST['id_groupe']
        obj = get_object_or_404(Types, id=id)
        formGroupe= GroupeForm(request.POST,instance=obj)
        if formGroupe.is_valid():
            formGroupe.save()
            return redirect('types')
    else:
        obj = get_object_or_404(Types, id=pk)
        data={
            'form': GroupeForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_types.html', data)

#******************************* Les Offres **************************************
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def offre(request):
    if request.method == 'POST':
        formOffre = OffreForm(request.POST)
        if formOffre.is_valid():
           formOffre.save()
        return redirect("offre")
    else:
        data={
           'offres': Offre.objects.all().order_by('-id'),
           'form':OffreForm()
        }
    return render(request,'dashboards/offre.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_offre(request, pk):
    if request.method == 'POST':
        id = request.POST['id_offre']
        obj = get_object_or_404(offre, id=id)
        formCategory= OffreForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('offre')
    else:
        obj = get_object_or_404(offre, id=pk)
        data={
            'form': OffreForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_offre.html', data)



@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deleteProporietaire(request):
    if request.method=='POST':
        id=request.POST['listProprietaireId']
        AuteurUser.objects.get(id=int(id)).delete()
    return redirect('liste_proprietaire')

# # @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeProprietaire(request):
    
    data={

            'listProprietaires':AuteurUser.objects.filter(is_proprietaire=True).all().order_by('-id'),
        }

    return render(request,'dashboards/liste_proprietaire.html',data)
# Assurez-vous de remplacer par le nom réel de votre formulaire


# views.py
@login_required
def update_profile(request, pk):
    try:
        obj = AuteurUser.objects.get(id=pk)
    except AuteurUser.DoesNotExist:
        raise Http404 

    formAuteurUser = ProprietaireForm(request.POST or None, request.FILES or None, instance=obj)

    print("request.POST:", request.POST)
    print("request.FILES:", request.FILES)

    messages = ''
    if formAuteurUser.is_valid():
        formAuteurUser.save()
        messages = "Vos modifications ont été effectuées avec succès!"
        return redirect('liste_proprietaire')

    print("formAuteurUser.errors:", formAuteurUser.errors)

    context = {
        'form': formAuteurUser,
        'obj': obj,
        'messages': messages
    }

    return render(request, 'modifiers/update_proprietaire.html', context)


#***************************** Operation ******************************
# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def operation(request):
    if request.method == 'POST':
         form = OperationFrom(request.POST)
         if form.is_valid():
            form.save()
         return redirect("operation")
    else:
        data={
           'operations': Operation.objects.all().order_by('-id'),
           'form':OperationFrom()
        }
    return render(request,'dashboards/operation.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deleteOperation(request):
    if request.method=='POST':
        id=request.POST['operationId']
        Operation.objects.get(id=int(id)).delete()
    return redirect('operation')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_operation(request, pk):
    if request.method == 'POST':
        id = request.POST['id_operation']
        obj = get_object_or_404(Operation, id=id)
        formCategory= OperationFrom(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('operation')
    else:
        obj = get_object_or_404(Operation, id=pk)
        data={
            'form': OperationFrom(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_operation.html', data)

#************************ Habitat ***********************
@login_required
def habitat(request):
    return render(request,'dashboards/habitat.html')


@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def chambre(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('logement')
    else:
        data = {
            'form':ChambreForm()
            }
        return render(request,'dashboards/logement.html',data)
    

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deletechambre(request):
    if request.method=='POST':
        id=request.POST['chambreId']
        Chambres.objects.get(id=int(id)).delete()
    return redirect('liste_chambre')


@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_chambre(request, pk):
    if request.method == 'POST':
        id = request.POST['id_chambre']
        obj = get_object_or_404(Chambres, id=id)
        formChambres= ChambresForm(request.POST,instance=obj)
        if formChambres.is_valid():
            formChambres.save()
            return redirect('liste_chambre')
    else:
        obj = get_object_or_404(Chambres, id=pk)
        data={
            'form': ChambresForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modifiers/update_chambre.html', data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def salon(request):
    if request.method == 'POST':
        form = SalonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('logement')
    else:
        data = {
            'form':SalonForm()
            }
        return render(request,'dashboards/logement.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def cuisine(request):
    if request.method == 'POST':
        form = CuisineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('logement')
    else:
        data = {
            'form':CuisineForm()
            }
        return render(request,'dashboards/logement.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def douche(request):
    if request.method == 'POST':
        form = DoucheForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('logement')
    else:
        data = {
            'form':DoucheForm()
            }
        return render(request,'dashboards/logement.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def balcon(request):
    if request.method == 'POST':
        form = BalconForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('logement')
    else:
        data = {
            'form':BalconForm()
            }
        return render(request,'dashboards/logement.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeChambres(request):
    if request.method == 'POST':
        form = ChambresForm(request.POST, request.FILES)
        formImage =ChambreImagesForm(request.POST, request.FILES)
        images=request.FILES.getlist('images')
        if form.is_valid() and formImage.is_valid():
            chambresCreats=form.save()
            for i in images:
                Images.objects.create(chambres=chambresCreats,images=i)
            messages.success(request,'Chambre ajouter !')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            errors= form.errors
            for field, error in errors.items():
                messages.error(request, f'{error}')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        data = {
            'chambres':Chambres.objects.all().order_by('-id'),
            'formChambre':ChambresForm(),
            'formImages':ChambreImagesForm()
            }
        return render(request,'dashboards/liste_chambre.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def immeuble(request):
    if request.method == 'POST':
        form = ImmeubleForm(request.POST,request.FILES)
        formImage =ImmeubleImagesForm(request.POST, request.FILES)
        images=request.FILES.getlist('images')
        if form.is_valid() and formImage.is_valid():
            immeubleCreats=form.save()
            for i in images:
                ImagesImmeuble.objects.create(immeuble=immeubleCreats,images=i)
            messages.success(request,'Immeuble ajouter !')
            return redirect('liste_chambre')
        else:
            errors= form.errors
            for field, error in errors.items():
                messages.error(request, f'{error}')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        data = {
            'form':ImmeubleForm(),
            'formImages':ImmeubleImagesForm(),

             }
        return render(request,'dashboards/immeuble.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_immeuble(request, pk):
    try:
        obj = Immeuble.objects.get(id=pk)
    except Immeuble.DoesNotExist:
        raise Http404 
    formImmeubre = ImmeubleForm(request.POST, request.FILES, instance=obj)
    messages=''
    if formImmeubre.is_valid():
        formImmeubre.save()
        messages ="Your modifiactions was  succesfully done!"
        return redirect('liste_immeuble')
   
    context={
        'form': ImmeubleForm(instance=obj),
        'obj': obj,
        'messagers':messages}
    return render(request, 'modifiers/update_immeuble.html',context)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeImmeuble(request):

    data = {
            'form':ImmeubleForm(),
            'immeubles':Immeuble.objects.all().order_by('-id')
            }
    return render(request,'dashboards/liste_immeuble.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deleteimmeuble(request):
    if request.method=='POST':
        id=request.POST['immeubleId']
        Immeuble.objects.get(id=int(id)).delete()
    return redirect('liste_immeuble')

@login_required
def edit_statut(request, pk):
    immeuble = Immeuble.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ImmeubleStatutForm(request.POST, instance=immeuble)
        if form.is_valid():
            form.save()
            return redirect('liste_immeuble')
    else:
        form = ImmeubleStatutForm(instance=immeuble)
    
    return render(request, 'publishBuilding.html', {'form': form,'obj':immeuble })


# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def terrain(request):
    if request.method == 'POST':
        form = TerrainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('terrain')
    else:
        data = {
            'form':TerrainForm(),
             }
        return render(request,'dashboards/terrain.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeTerrain(request):
        data ={
             'listeTerrain':Terrain.objects.all().order_by('-id')[:3],
        }
        return render(request,'dashboards/liste_terrain.html',data)


# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deleteterrain(request):
    if request.method=='POST':
        id=request.POST['terrainId']
        Terrain.objects.get(id=int(id)).delete()
    return redirect('liste_terrain')

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))



def update_terrain(request, pk):
    try:
        obj = Terrain.objects.get(id=pk)
    except Terrain.DoesNotExist:
        raise Http404 
    formTerrain = TerrainForm(request.POST, request.FILES, instance=obj)
    print(formTerrain)
    messages=''
    if formTerrain.is_valid():
        formTerrain.save()
        messages ="Your modifiactions was  succesfully done!"
        return redirect('liste_terrain')
   
    context={
        'form': TerrainForm(instance=obj),
        'obj': obj,
        'messagers':messages}
    return render(request, 'modifiers/update_terrain.html',context)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        formImage =PlanImagesForm(request.POST, request.FILES)
        images=request.FILES.getlist('images')
        if form.is_valid() and formImage.is_valid():
            planCreats=form.save()
            for i in images:
                ImagesPlan.objects.create(plan=planCreats,images=i)
            messages.success(request,'Plan ajouter !')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            errors= form.errors
            for field, error in errors.items():
                messages.error(request, f'{error}')
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        data = {
            # 'plans':Plan.objects.all().order_by('-id'),
            'form':PlanForm(),
            'imageForm':PlanImagesForm()
             }
        return render(request,'dashboards/construire.html',data)

# @group_required('administrateur')
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listePlan(request):
        data ={
            'listePlan':Plan.objects.all().order_by('-id')[:3],
        }
        return render(request,'dashboards/liste_plan.html',data)



#*************************Devis**********************************#
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def devis(request):
    if request.method == 'POST':
         form = DevisForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("liste_devis")
    else:
        data={
           'form':DevisForm()
        }
    return render(request,'dashboards/devis.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_devis(request, pk):
    if request.method == 'POST':
        id = request.POST['id_devis']
        obj = get_object_or_404(devis, id=id)
        formCategory= DevisForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('devis')
    else:
        obj = get_object_or_404(devis, id=pk)
        data={
            'form': DevisForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_devis.html', data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeDevis(request):
        data={
        #    'devis': Devis.objects.all().order_by('-id'),

        }
        return render(request,'dashboards/liste_devis.html',data)

#*************************Expertise**********************************#
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def expertise(request):
    if request.method == 'POST':
         form = ExpertiseForm(request.POST)
         if form.is_valid():
            form.save()
         return redirect("liste_expertise")
    else:
        data={
           'expertises': Expertise.objects.all().order_by('-id'),
           'form':ExpertiseForm()
        }
    return render(request,'dashboards/expertise.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def listeExpertise(request):
        data={
           'expertises': Expertise.objects.all().order_by('-id'),

        }
        return render(request,'dashboards/liste_expertise.html',data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_expertise(request, pk):
    if request.method == 'POST':
        id = request.POST['id_expertise']
        obj = get_object_or_404(expertise, id=id)
        formCategory= ExpertiseForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('expertise')
    else:
        obj = get_object_or_404(expertise, id=pk)
        data={
            'form': ExpertiseForm(instance=obj),
            'obj': obj

        }
        return render(request, 'modal/modal_expertise.html', data)




def beninLand(request):
    selectImmeuble = Immeuble.objects.all().order_by('-id')[:3]
    selectTerrain = Terrain.objects.all().order_by('-id')[:3]
     
    error_message = None 
    error_message_terrain = None
  

    if request.method == "GET":
        quartier = request.GET.get("quartier")
        quartier_terrain = request.GET.get("quartier_terrain")
        if quartier:
            quartier = quartier.title()
            print(f"Recherche de quartier : {quartier}")
            # Utilisez quartier__nom pour accéder au champ nom du modèle Quartier
            selectImmeuble = Immeuble.objects.filter(quartier__nom=quartier)
            # Vérifier si des résultats ont été trouvés
            if not selectImmeuble.exists():
                error_message = f"Nous n'avons pas d'oeuvre dans cette zone souhaitée : {quartier}"
                print(error_message)
        if quartier_terrain:
            quartier_terrain = quartier_terrain.title()
            print(f"Recherche de quartier pour terrains : {quartier_terrain}")
            selectTerrain = Terrain.objects.filter(quartier__nom=quartier_terrain)
         
            if not selectTerrain.exists():
                error_message_terrain = f"Aucun terrain trouvé dans ce quartier : {quartier_terrain}"
                print(error_message_terrain)      
        
    data = {
        'communes': Commune.objects.all().order_by('-id'),
        'departements': Departement.objects.all().order_by('-id'),
        'chambres': selectImmeuble,
        'terrains': selectTerrain,
        'error_messages': error_message,
        'error_messages_terrain': error_message_terrain,
    }
    return render(request, 'interface/accueil.html', data)

def liste_chambres_immeubles(request, immeuble_id):
    immeuble = Immeuble.objects.get(id=immeuble_id)
    chambres = Chambres.objects.filter(immeuble=immeuble)
    listeTerrains=Terrain.objects.all().order_by('-id')[:3]

    context = {
        'immeuble': immeuble,
        'chambres': chambres,
        'listeTerrain':listeTerrains,
    }
    return render(request, 'interface/liste_chambres_immeubles.html', context)

def details_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambres, id=chambre_id)

    context = {
        'chambre': chambre,
    }

    return render(request, 'interface/details_chambre.html', context)

#************************* Mon Espace **********************************
@login_required
def monEspace(request,):

    # Retrieve Chambres instances for the currently logged-in user with is_proprietaire set to True
    proprietaire_properties = Chambres.objects.filter(proprietaire=request.user, proprietaire__is_proprietaire=True)
    
    # Prepare the context to pass to the template
    context = {
        'proprietaire_properties': proprietaire_properties
    }

    # Render the template with the provided context
    return render(request, 'dashboards/compte.html', context)

def detailEspace(request,  chambre_id):
    chambre = get_object_or_404(Chambres, id=chambre_id)

    context = {
        'chambre': chambre,
    }
    return render(request, 'dashboards/detail.html',context)
#***************************************************************************
def beninLandPropos(request):
 
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
            
            return render(request, 'interface/propos.html')
    else:
        context={
            
            'formContact':ContactezNousForm()
        }
    
    return render(request, 'interface/propos.html', context)

def beninLandLouer(request):
    operations_immeubles = Immeuble.objects.filter(operation__type='Location')
    operations_terrains = Terrain.objects.filter(operation__type='Location')
    quartier_search = request.GET.get('quartier')
    
    if quartier_search:
        operations_immeubles = operations_immeubles.filter(quartier__nom__icontains=quartier_search)
        operations_terrains = operations_terrains.filter(quartier__nom__icontains=quartier_search)
    
    context = {
        'immeubles':operations_immeubles,
        'chambres': Chambres.objects.filter(immeuble__in=operations_immeubles),
        'terrains': operations_terrains,
        'quartier_search': quartier_search,
    }
    
    return render(request, 'interface/louer.html', context)




def beninLandAcheter(request):
    operations_immeubles = Immeuble.objects.filter(operation__type='Acheter')
    operations_terrains = Terrain.objects.filter(operation__type='Acheter')
    quartier_search = request.GET.get('quartier')
    
    if quartier_search:
        operations_immeubles = operations_immeubles.filter(quartier__nom__icontains=quartier_search)
        operations_terrains = operations_terrains.filter(quartier__nom__icontains=quartier_search)
    
    context = {
        'immeubles':operations_immeubles,
        'chambres': Chambres.objects.filter(immeuble__in=operations_immeubles),
        'terrains': operations_terrains,
        'quartier_search': quartier_search,
    }
    
    return render(request, 'interface/acheter.html', context)



def beninLandterrain(request):
        selectTerrain=Terrain.objects.all().order_by('-id')
        if request.method == "GET":
          
            terrain = request.GET.get("terrain")
        
            if terrain:
                terrain = terrain.title()
                print(f"Recherche de quartier pour terrains : {terrain}")
                selectTerrain = Terrain.objects.filter(quartier__nom=terrain)
            
                if not selectTerrain.exists():
                    error_message_terrain = f"Aucun terrain trouvé dans ce quartier : {terrain}"
                    print(error_message_terrain)   
        context={
         'terrains':selectTerrain
        }
        return render(request,'interface/terrain.html',context)

def beninLandPlan(request):
        context={

            'plans':Plan.objects.all().order_by('-id')
        }
        return render(request,'interface/plan.html',context)

def beninLandExpertise(request):
    if request.method == 'POST':
        formContact = ContactezNousForm(request.POST)
        if formContact.is_valid():
            formContact.save()
        else:
            # Gérer les erreurs du formulaire ici si nécessaire
            print(formContact.errors)
    else:
        data = {
            'formContact': ContactezNousForm()
        }
    return render(request,'interface/expertise.html',data)

def beninLandDevis(request):
    if request.method == 'POST':
        formContact = ContactezNousForm(request.POST)
        if formContact.is_valid():
            formContact.save()
        else:
            # Gérer les erreurs du formulaire ici si nécessaire
            print(formContact.errors)
    else:
        data = {
            'formContact': ContactezNousForm()
        }
    return render(request,'interface/devis.html',data)


def details_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambres, id=chambre_id)

    context = {
        'chambre': chambre,
    }

    return render(request, 'interface/detail_chambre.html', context)

def details_immeuble(request, immeuble_id):
    immeuble = get_object_or_404(Immeuble, id=immeuble_id)

    context = {
        'immeubles': immeuble,
    }

    return render(request, 'interface/detail_immeuble.html', context)


def detail_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'interface/detail_plan.html', context)

def liste_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'interface/detail_plan.html', context)

def beninLandContact(request):
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
            
            return render(request, 'interface/contactez.html')
    else:
        data={

           'formContact':ContactezNousForm()
        }
    return render(request,'interface/contactez.html',data)



def chambreDetail(request,id):
    context={
        'detailchambres':Chambres.objects.get(id=id)
    }
    return render(request,'interface/detail.html',context)

def terrainDetail(request,id):
    context={
        'detailterrain':Terrain.objects.get(id=id)
    }
    return render(request,'interface/detailTerrain.html',context)

def faq(request):
    
    return render(request,'interface/faq.html')


#Annonce 
@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def annonce(request):
        if request.method == 'POST':
            form = AnnonceForm(request.POST,request.FILES)
            formImage =AnnonceImagesForm(request.POST, request.FILES)
            images=request.FILES.getlist('images')
            if form.is_valid() and formImage.is_valid():
                AnnonceCreats=form.save()
                for i in images:
                   ImagesAnnonce.objects.create(annonce=AnnonceCreats, images=i)

                messages.success(request,'Annonce ajouter !')
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                errors= form.errors
                for field, error in errors.items():
                    messages.error(request, f'{error}')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            data = {
            'annonces': Annonce.objects.all().order_by('-id'),
            'form': AnnonceForm(), # Assurez-vous que votre formulaire est correctement défini
            'formImages':AnnonceImagesForm()
            }
        return render(request, 'dashboards/annonce.html', data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def update_annonce(request, pk):
    if request.method == 'POST':
        id = request.POST['id_annonce']
        obj = get_object_or_404(Annonce, id=id)
        formCategory= AnnonceForm(request.POST,instance=obj)
        if formCategory.is_valid():
            formCategory.save()
            return redirect('annonce')
    else:
        obj = get_object_or_404(Annonce, id=pk)
        data={
            'form': AnnonceForm(instance=obj),
            'obj': obj,
            'formImages':AnnonceImagesForm()
        }
        return render(request, 'modal/modal_annonce.html', data)

@login_required(login_url='login')
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def deleteAnnonce(request):
    if request.method=='POST':
        id=request.POST['annonceId']
        Annonce.objects.get(id=int(id)).delete()
    return redirect('annonce')

@login_required(login_url='login')
def modify_profile(request):
    if request.method == 'POST':
        form = ProprietaireForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("liste_proprietaire")  # Redirigez vers la page souhaitée après la modification du profil
    else:
        form = ProprietaireForm(instance=request.user)

    return render(request, 'dashboards/proprietaire.html', {"form": form})


@login_required(login_url='login')
def Contact(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'dashboards/liste_contact.html',context)


#*************************----- Departement ----**********************

def alibori(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/alibori.html',context)

def atacora(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/atacora.html',context)

def atlantique(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/atlantique.html',context)
def borgou(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/borgou.html',context)
def colline(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/colline.html',context)

def couffo(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/couffo.html',context)

def donga(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/donga.html',context)

def littora(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/littoral.html',context)

def mono(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/mono.html',context)

def oueme(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/oueme.html',context)

def plateau(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/plateau.html',context)

def zou(request):
    listeContact=ContactezNous.objects.all().order_by('-id')[:3]
    context ={
        'listeContacts':listeContact
    }
    return render(request, 'interface/departement/zou.html',context)

#********************************** Les communes pour les departement****************
def banikoara(request):
    banikoaraImmeubles=Immeuble.objects.filter(commune__nom='Banikoara').order_by('-id')[:3]
    banikoaraQuartier=Chambres.objects.filter(immeuble__commune__nom='Banikoara').order_by('-id')[:3]
    content = {
        'banikoaraImmeubles':banikoaraImmeubles,
        'banikoaraQuartiers':banikoaraQuartier,
    }
    return render(request, 'interface/communes/banikoara.html',content)

def gogounou(request):
    gogounouImmeubles=Immeuble.objects.filter(commune__nom='Gogounou').order_by('-id')[:3]
    gogounouQuartier=Chambres.objects.filter(immeuble__commune__nom='Gogounou').order_by('-id')[:3]
    content = {
        'gogounouImmeubles':gogounouImmeubles,
        'gogounouQuartiers':gogounouQuartier,
    }
    return render(request, 'interface/communes/gogounou.html',content)

def kandi(request):
    kandiImmeubles=Immeuble.objects.filter(commune__nom='Kandi').order_by('-id')[:3]
    kandiQuartier=Chambres.objects.filter(immeuble__commune__nom='Kandi').order_by('-id')[:3]
    content = {
        'kandiImmeubles':kandiImmeubles,
        'kandiQuartiers':kandiQuartier,
    }
    return render(request, 'interface/communes/kandi.html',content)

def karimama(request):
    karimamanImmeubles=Immeuble.objects.filter(commune__nom='Karimama').order_by('-id')[:3]
    karimamanQuartier=Chambres.objects.filter(immeuble__commune__nom='Karimama').order_by('-id')[:3]
    content = {
        'karimamanImmeubles':karimamanImmeubles,
        'karimamanQuartiers':karimamanQuartier,
    }
    return render(request, 'interface/communes/karimama.html',content)

def malanville(request):
    malanvilleImmeubles=Immeuble.objects.filter(commune__nom='Malanville').order_by('-id')[:3]
    malanvilleQuartier=Chambres.objects.filter(immeuble__commune__nom='Malanville').order_by('-id')[:3]
    content = {
        'malanvilleImmeubles':malanvilleImmeubles,
        'malanvilleQuartiers':malanvilleQuartier,
    }
    return render(request, 'interface/communes/malanville.html',content)

def segbana(request):
    segbanaImmeubles=Immeuble.objects.filter(commune__nom='Segbana').order_by('-id')[:3]
    segbanaQuartier=Chambres.objects.filter(immeuble__commune__nom='Segbana').order_by('-id')[:3]
    content = {
        'segbanaImmeubles':segbanaImmeubles,
        'segbanaQuartiers':segbanaQuartier,
    }
    return render(request, 'interface/communes/segbana.html',content)

def boukoumbe(request):
    boukoumbeImmeubles=Immeuble.objects.filter(commune__nom='Boukoumbé').order_by('-id')[:3]
    boukoumbeQuartier=Chambres.objects.filter(immeuble__commune__nom='Boukoumbé').order_by('-id')[:3]
    content = {
        'boukoumbeImmeubles':boukoumbeImmeubles,
        'boukoumbeQuartiers':boukoumbeQuartier,
    }
    return render(request, 'interface/communes/boukoumbe.html',content)

def cobly(request):
    coblyImmeubles=Immeuble.objects.filter(commune__nom='Cobly').order_by('-id')[:3]
    coblyQuartier=Chambres.objects.filter(immeuble__commune__nom='Cobly').order_by('-id')[:3]
    content = {
        'coblyImmeubles':coblyImmeubles,
        'coblyQuartiers':coblyQuartier,
    }
    return render(request, 'interface/communes/cobly.html',content)

def kerou(request):
    kerouImmeubles=Immeuble.objects.filter(commune__nom='Kerou').order_by('-id')[:3]
    kerouQuartier=Chambres.objects.filter(immeuble__commune__nom='Kerou').order_by('-id')[:3]
    content = {
        'kerouImmeubles':kerouImmeubles,
        'kerouQuartiers':kerouQuartier,
    }
    return render(request, 'interface/communes/kerou.html',content)

def kouande(request):
    kouandeImmeubles=Immeuble.objects.filter(commune__nom='Kouandé').order_by('-id')[:3]
    kouandeQuartier=Chambres.objects.filter(immeuble__commune__nom='Kouandé').order_by('-id')[:3]
    content = {
        'kouandeImmeubles':kouandeImmeubles,
        'kouandeQuartiers':kouandeQuartier,
    }
    return render(request, 'interface/communes/kouande.html',content)


def materi(request):
    materiImmeubles=Immeuble.objects.filter(commune__nom='Matéri').order_by('-id')[:3]
    materiQuartier=Chambres.objects.filter(immeuble__commune__nom='Matéri').order_by('-id')[:3]
    content = {
        'materiImmeubles':materiImmeubles,
        'materiQuartiers':materiQuartier,
    }
    return render(request, 'interface/communes/materi.html',content)

def natitingou(request):
    natitingouImmeubles=Immeuble.objects.filter(commune__nom='Natitingou').order_by('-id')[:3]
    natitingouQuartier=Chambres.objects.filter(immeuble__commune__nom='Natitingou').order_by('-id')[:3]
    content = {
        'natitingouImmeubles':natitingouImmeubles,
        'natitingouQuartiers':natitingouQuartier,
    }
    return render(request, 'interface/communes/natitingou.html',content)

def pehunco(request):
    pehuncoImmeubles=Immeuble.objects.filter(commune__nom='Péhunco').order_by('-id')[:3]
    pehuncoQuartier=Chambres.objects.filter(immeuble__commune__nom='Péhunco').order_by('-id')[:3]
    content = {
        'pehuncoImmeubles':pehuncoImmeubles,
        'pehuncoQuartiers':pehuncoQuartier,
    }
    return render(request, 'interface/communes/pehunco.html',content)

def tanguieta(request):
    tanguietaImmeubles=Immeuble.objects.filter(commune__nom='Tanguieta').order_by('-id')[:3]
    tanguietaQuartier=Chambres.objects.filter(immeuble__commune__nom='Téhunco').order_by('-id')[:3]
    content = {
        'tanguietaImmeubles':tanguietaImmeubles,
        'tanguietaQuartiers':tanguietaQuartier,
    }
    return render(request, 'interface/communes/tanguieta.html',content)

def toucountouna(request):
    toucountounaImmeubles=Immeuble.objects.filter(commune__nom='Toucountouna').order_by('-id')[:3]
    toucountounaQuartier=Chambres.objects.filter(immeuble__commune__nom='Toucountouna').order_by('-id')[:3]
    content = {
        'toucountounaImmeubles':toucountounaImmeubles,
        'toucountounaQuartiers':toucountounaQuartier,
    }
    return render(request, 'interface/communes/toucountouna.html',content)

def ouidah(request):
    ouidahImmeubles=Immeuble.objects.filter(commune__nom='Ouidah').order_by('-id')[:3]
    ouidahQuartier=Chambres.objects.filter(immeuble__commune__nom='Ouidah').order_by('-id')[:3]
    content = {
        'ouidahImmeubles':ouidahImmeubles,
        'ouidahQuartiers':ouidahQuartier,
    }
    return render(request, 'interface/communes/ouidah.html',content)

def allada(request):
    alladaImmeubles=Immeuble.objects.filter(commune__nom='Allada').order_by('-id')[:3]
    alladaQuartier=Chambres.objects.filter(immeuble__commune__nom='Allada').order_by('-id')[:3]
    content = {
        'alladaImmeubles':alladaImmeubles,
        'alladaQuartiers':alladaQuartier,
    }
    return render(request, 'interface/communes/allada.html',content)

def tori(request):
    toriImmeubles=Immeuble.objects.filter(commune__nom='Tori-Bossito').order_by('-id')[:3]
    toriQuartier=Chambres.objects.filter(immeuble__commune__nom='Tori-Bossito').order_by('-id')[:3]
    content = {
        'toriImmeubles':toriImmeubles,
        'toriQuartiers':toriQuartier,
    }
    return render(request, 'interface/communes/tori.html',content)

def toffo(request):
    toffoImmeubles=Immeuble.objects.filter(commune__nom='Toffo').order_by('-id')[:3]
    toffoQuartier=Chambres.objects.filter(immeuble__commune__nom='Toffo').order_by('-id')[:3]
    content = {
        'toffoImmeubles':toffoImmeubles,
        'toffoQuartiers':toffoQuartier,
    }
    return render(request, 'interface/communes/toffo.html',content)

def zee(request):
    zeImmeubles=Immeuble.objects.filter(commune__nom='Ze').order_by('-id')[:3]
    zeQuartier=Chambres.objects.filter(immeuble__commune__nom='Ze').order_by('-id')[:3]
    content = {
        'zeImmeubles':zeImmeubles,
        'zeQuartiers':zeQuartier,
    }
    return render(request, 'interface/communes/ze.html',content)

def soava(request):
    soavaImmeubles=Immeuble.objects.filter(commune__nom='So-Ava').order_by('-id')[:3]
    soavaQuartier=Chambres.objects.filter(immeuble__commune__nom='So-Ava').order_by('-id')[:3]
    content = {
        'soavaImmeubles':soavaImmeubles,
        'soavaQuartiers':soavaQuartier,
    }
    return render(request, 'interface/communes/soava.html',content)

def kpomasse(request):
    kpomasseImmeubles=Immeuble.objects.filter(commune__nom='Kpomassè').order_by('-id')[:3]
    kpomasseQuartier=Chambres.objects.filter(immeuble__commune__nom='Kpomassè').order_by('-id')[:3]
    content = {
        'kpomasseImmeubles':kpomasseImmeubles,
        'kpomasseQuartiers':kpomasseQuartier,
    }
    return render(request, 'interface/communes/kpomasse.html',content)

def abomey_Calavi(request):
    calaviImmeubles=Immeuble.objects.filter(commune__nom='Abomey-Calavi').order_by('-id')[:3]
    calaviQuartier=Chambres.objects.filter(immeuble__commune__nom='Abomey-Calavi').order_by('-id')[:3]
    content = {
        'calaviImmeubles':calaviImmeubles,
        'calaviQuartiers':calaviQuartier,
    }
    return render(request, 'interface/communes/calavi.html',content)

def bembereque(request):
    bemberequeImmeubles=Immeuble.objects.filter(commune__nom='Bembereque').order_by('-id')[:3]
    bemberequeQuartier=Chambres.objects.filter(immeuble__commune__nom='Bembereque').order_by('-id')[:3]
    content = {
        'bemberequeImmeubles':bemberequeImmeubles,
        'bemberequeQuartiers':bemberequeQuartier,
    }
    return render(request, 'interface/communes/bembereque.html',content)

def parakou(request):
    parakouImmeubles=Immeuble.objects.filter(commune__nom='Parakou').order_by('-id')[:3]
    parakouQuartier=Chambres.objects.filter(immeuble__commune__nom='Parakou').order_by('-id')[:3]
    content = {
        'parakouImmeubles':parakouImmeubles,
        'parakouQuartiers':parakouQuartier,
    }
    return render(request, 'interface/communes/parakou.html',content)

def kalale(request):
    kalaleImmeubles=Immeuble.objects.filter(commune__nom='Kalalé').order_by('-id')[:3]
    kalaleQuartier=Chambres.objects.filter(immeuble__commune__nom='Kalalé').order_by('-id')[:3]
    content = {
        'kalaleImmeubles':kalaleImmeubles,
        'kalaleQuartiers':kalaleQuartier,
    }
    return render(request, 'interface/communes/kalale.html',content)

def perere(request):
    perereImmeubles=Immeuble.objects.filter(commune__nom='pèrèrè').order_by('-id')[:3]
    perereQuartier=Chambres.objects.filter(immeuble__commune__nom='pèrèrè').order_by('-id')[:3]
    content = {
        'perereImmeubles':perereImmeubles,
        'perereQuartiers':perereQuartier,
    }
    return render(request, 'interface/communes/perere.html',content)

def tchaorou(request):
    tchaorouImmeubles=Immeuble.objects.filter(commune__nom='Tchaorou').order_by('-id')[:3]
    tchaorouQuartier=Chambres.objects.filter(immeuble__commune__nom='Tchaorou').order_by('-id')[:3]
    content = {
        'tchaorouImmeubles':tchaorouImmeubles,
        'tchaorouQuartiers':tchaorouQuartier,
    }
    return render(request, 'interface/communes/tchaorou.html',content)

def sinande(request):
    sinandeImmeubles=Immeuble.objects.filter(commune__nom='Sinandé').order_by('-id')[:3]
    sinandeQuartier=Chambres.objects.filter(immeuble__commune__nom='Sinandé').order_by('-id')[:3]
    content = {
        'sinandeImmeubles':sinandeImmeubles,
        'sinandeQuartiers':sinandeQuartier,
    }
    return render(request, 'interface/communes/sinande.html',content)

def bante(request):
    banteImmeubles=Immeuble.objects.filter(commune__nom='Banté').order_by('-id')[:3]
    banteQuartier=Chambres.objects.filter(immeuble__commune__nom='Banté').order_by('-id')[:3]
    content = {
        'banteImmeubles':banteImmeubles,
        'banteQuartiers':banteQuartier,
    }
    return render(request, 'interface/communes/bante.html',content)


def dassa(request):
    dassaImmeubles=Immeuble.objects.filter(commune__nom='Dassa-Zoumé').order_by('-id')[:3]
    dassaQuartier=Chambres.objects.filter(immeuble__commune__nom='Dassa-Zoumé').order_by('-id')[:3]
    content = {
        'dassaImmeubles':dassaImmeubles,
        'dassaQuartiers':dassaQuartier,
    }
    return render(request, 'interface/communes/dassa.html',content)   

def glazoue(request):
    glazoueImmeubles=Immeuble.objects.filter(commune__nom='Glazoué').order_by('-id')[:3]
    glazoueQuartier=Chambres.objects.filter(immeuble__commune__nom='Glazoué').order_by('-id')[:3]
    content = {
        'glazoueImmeubles':glazoueImmeubles,
        'glazoueQuartiers':glazoueQuartier,
    }
    return render(request, 'interface/communes/glazoue.html',content)  

def ouesse(request):
    ouesseImmeubles=Immeuble.objects.filter(commune__nom='Ouèssé').order_by('-id')[:3]
    ouesseQuartier=Chambres.objects.filter(immeuble__commune__nom='Ouèssé').order_by('-id')[:3]
    content = {
        'ouesseImmeubles':ouesseImmeubles,
        'ouesseQuartiers':ouesseQuartier,
    }
    return render(request, 'interface/communes/ouesse.html',content)  

def savalou(request):
    savalouImmeubles=Immeuble.objects.filter(commune__nom='Savalou').order_by('-id')[:3]
    savalouQuartier=Chambres.objects.filter(immeuble__commune__nom='Savalou').order_by('-id')[:3]
    content = {
        'savalouImmeubles':savalouImmeubles,
        'savalouQuartiers':savalouQuartier,
    }
    return render(request, 'interface/communes/savalou.html',content)  

def dassa(request):
    dassaImmeubles=Immeuble.objects.filter(commune__nom='Dassa').order_by('-id')[:3]
    dassaQuartier=Chambres.objects.filter(immeuble__commune__nom='Dassa').order_by('-id')[:3]
    content = {
        'dassaImmeubles':dassaImmeubles,
        'dassaQuartiers':dassaQuartier,
    }
    return render(request, 'interface/communes/dassa.html',content)  

def save(request):
    saveImmeubles=Immeuble.objects.filter(commune__nom='Savè').order_by('-id')[:3]
    saveQuartier=Chambres.objects.filter(immeuble__commune__nom='Savè').order_by('-id')[:3]
    content = {
        'saveImmeubles':saveImmeubles,
        'saveQuartiers':saveQuartier,
    }
    return render(request, 'interface/communes/save.html',content)  

def aplahoue(request):
    aplahoueImmeubles=Immeuble.objects.filter(commune__nom='Aplahoué').order_by('-id')[:3]
    aplahoueQuartier=Chambres.objects.filter(immeuble__commune__nom='Aplahoué').order_by('-id')[:3]
    content = {
        'aplahoueImmeubles':aplahoueImmeubles,
        'aplahoueQuartiers':aplahoueQuartier,
    }
    return render(request, 'interface/communes/aplahoue.html',content)  



def djakotomey(request):
    djakotomeyImmeubles=Immeuble.objects.filter(commune__nom='Djakotomey').order_by('-id')[:3]
    djakotomeyQuartier=Chambres.objects.filter(immeuble__commune__nom='Djakotomey').order_by('-id')[:3]
    content = {
        'djakotomeyImmeubles':djakotomeyImmeubles,
        'djakotomeyQuartiers':djakotomeyQuartier,
    }
    return render(request, 'interface/communes/djakotomey.html',content)  


def dogbo(request):
    dogboImmeubles=Immeuble.objects.filter(commune__nom='Dogbo').order_by('-id')[:3]
    dogboQuartier=Chambres.objects.filter(immeuble__commune__nom='Dogbo').order_by('-id')[:3]
    content = {
        'dogboImmeubles':dogboImmeubles,
        'dogboQuartiers':dogboQuartier,
    }
    return render(request, 'interface/communes/dogbo.html',content)  

def lola(request):
    lolaImmeubles=Immeuble.objects.filter(commune__nom='lola').order_by('-id')[:3]
    lolaQuartier=Chambres.objects.filter(immeuble__commune__nom='lola').order_by('-id')[:3]
    content = {
        'lolaImmeubles':lolaImmeubles,
        'lolaQuartiers':lolaQuartier,
    }
    return render(request, 'interface/communes/lola.html',content)  

def toviklin(request):
    toviklinImmeubles=Immeuble.objects.filter(commune__nom='Toviklin').order_by('-id')[:3]
    toviklinQuartier=Chambres.objects.filter(immeuble__commune__nom='Toviklin').order_by('-id')[:3]
    content = {
        'toviklinImmeubles':toviklinImmeubles,
        'toviklinQuartiers':toviklinQuartier,
    }
    return render(request, 'interface/communes/toviklin.html',content) 

def djougou(request):
    djougouImmeubles=Immeuble.objects.filter(commune__nom='Djougou').order_by('-id')[:3]
    djougouQuartier=Chambres.objects.filter(immeuble__commune__nom='Djougou').order_by('-id')[:3]
    content = {
        'djougouImmeubles':djougouImmeubles,
        'djougouQuartiers':djougouQuartier,
    }
    return render(request, 'interface/communes/djougou.html',content) 

def ouake(request):
    ouakeImmeubles=Immeuble.objects.filter(commune__nom='Ouaké').order_by('-id')[:3]
    ouakeQuartier=Chambres.objects.filter(immeuble__commune__nom='Ouaké').order_by('-id')[:3]
    content = {
        'ouakeImmeubles':ouakeImmeubles,
        'ouakeQuartiers':ouakeQuartier,
    }
    return render(request, 'interface/communes/ouake.html',content) 

def copargo(request):
    copargoImmeubles=Immeuble.objects.filter(commune__nom='Copargo').order_by('-id')[:3]
    copargoQuartier=Chambres.objects.filter(immeuble__commune__nom='Copargo').order_by('-id')[:3]
    content = {
        'copargoImmeubles':copargoImmeubles,
        'copargoQuartiers':copargoQuartier,
    }
    return render(request, 'interface/communes/copargo.html',content) 

def bassila(request):
    bassilaImmeubles=Immeuble.objects.filter(commune__nom='Bassila').order_by('-id')[:3]
    bassilaQuartier=Chambres.objects.filter(immeuble__commune__nom='Bassila').order_by('-id')[:3]
    content = {
        'bassilaImmeubles':bassilaImmeubles,
        'bassilaQuartiers':bassilaQuartier,
    }
    return render(request, 'interface/communes/bassila.html',content) 

def cotonou(request):
    cotonouImmeubles=Immeuble.objects.filter(commune__nom='Cotonou').order_by('-id')[:3]
    cotonouQuartier=Chambres.objects.filter(immeuble__commune__nom='Cotonou').order_by('-id')[:3]
    content = {
        'cotonouImmeubles':cotonouImmeubles,
        'cotonouQuartiers':cotonouQuartier,
    }
    return render(request, 'interface/communes/cotonou.html',content) 

def athieme(request):
    athiemeImmeubles=Immeuble.objects.filter(commune__nom='Athiémé').order_by('-id')[:3]
    athiemeQuartier=Chambres.objects.filter(immeuble__commune__nom='Athiémé').order_by('-id')[:3]
    content = {
        'athiemeImmeubles':athiemeImmeubles,
        'athiemeQuartiers':athiemeQuartier,
    }
    return render(request, 'interface/communes/athieme.html',content) 

def bopa(request):
    bopaImmeubles=Immeuble.objects.filter(commune__nom='Bopa').order_by('-id')[:3]
    bopaQuartier=Chambres.objects.filter(immeuble__commune__nom='Bopa').order_by('-id')[:3]
    content = {
        'bopaImmeubles':bopaImmeubles,
        'bopaQuartiers':bopaQuartier,
    }
    return render(request, 'interface/communes/bopa.html',content) 

def come(request):
    comeImmeubles=Immeuble.objects.filter(commune__nom='Comè').order_by('-id')[:3]
    comeQuartier=Chambres.objects.filter(immeuble__commune__nom='Comè').order_by('-id')[:3]
    content = {
        'comeImmeubles':comeImmeubles,
        'comeQuartiers':comeQuartier,
    }
    return render(request, 'interface/communes/come.html',content) 

def grand_popo(request):
    grandImmeubles=Immeuble.objects.filter(commune__nom='Grand_Popo').order_by('-id')[:3]
    grandQuartier=Chambres.objects.filter(immeuble__commune__nom='Grand_Popo').order_by('-id')[:3]
    content = {
        'grandImmeubles':grandImmeubles,
        'grandQuartiers':grandQuartier,
    }
    return render(request, 'interface/communes/grand_popo.html',content) 

def houeyogbe(request):
    houeyogbeImmeubles=Immeuble.objects.filter(commune__nom='houéyogbé').order_by('-id')[:3]
    houeyogbeQuartier=Chambres.objects.filter(immeuble__commune__nom='houéyogbé').order_by('-id')[:3]
    content = {
        'houeyogbeImmeubles':houeyogbeImmeubles,
        'houeyogbeQuartiers':houeyogbeQuartier,
    }
    return render(request, 'interface/communes/houeyogbe.html',content) 

def lokossa(request):
    lokossaImmeubles=Immeuble.objects.filter(commune__nom='Lokossa').order_by('-id')[:3]
    lokossaQuartier=Chambres.objects.filter(immeuble__commune__nom='Lokossa').order_by('-id')[:3]
    content = {
        'lokossaImmeubles':lokossaImmeubles,
        'lokossaQuartiers':lokossaQuartier,
    }
    return render(request, 'interface/communes/lokossa.html',content) 

def adjarra(request):
    adjarraImmeubles=Immeuble.objects.filter(commune__nom='Adjarra').order_by('-id')[:3]
    adjarraQuartier=Chambres.objects.filter(immeuble__commune__nom='Adjarra').order_by('-id')[:3]
    content = {
        'adjarraImmeubles':adjarraImmeubles,
        'adjarraQuartiers':adjarraQuartier,
    }
    return render(request, 'interface/communes/adjarra.html',content) 

def adjohoun(request):
    adjohounImmeubles=Immeuble.objects.filter(commune__nom='Adjohoun').order_by('-id')[:3]
    adjohounQuartier=Chambres.objects.filter(immeuble__commune__nom='Adjohoun').order_by('-id')[:3]
    content = {
        'adjohounImmeubles':adjohounImmeubles,
        'adjohounQuartiers':adjohounQuartier,
    }
    return render(request, 'interface/communes/adjohoun.html',content)
def aguegues(request):
    agueguesImmeubles=Immeuble.objects.filter(commune__nom='Aguégués').order_by('-id')[:3]
    agueguesQuartier=Chambres.objects.filter(immeuble__commune__nom='Aguégués').order_by('-id')[:3]
    content = {
        'agueguesImmeubles':agueguesImmeubles,
        'agueguesQuartiers':agueguesQuartier,
    }
    return render(request, 'interface/communes/aguegues.html',content) 
def misserete(request):
    missereteImmeubles=Immeuble.objects.filter(commune__nom='Akpro-Missérété').order_by('-id')[:3]
    missereteQuartier=Chambres.objects.filter(immeuble__commune__nom='Akpro-Missérété').order_by('-id')[:3]
    content = {
        'missereteImmeubles':missereteImmeubles,
        'missereteQuartiers':missereteQuartier,
    }
    return render(request, 'interface/communes/misserete.html',content) 
def avrankou(request):
    avrankouImmeubles=Immeuble.objects.filter(commune__nom='Avrankou').order_by('-id')[:3]
    avrankouQuartier=Chambres.objects.filter(immeuble__commune__nom='Avrankou').order_by('-id')[:3]
    content = {
        'avrankouImmeubles':avrankouImmeubles,
        'avrankouQuartiers':avrankouQuartier,
    }
    return render(request, 'interface/communes/avrankou.html',content) 
def bonou(request):
    bonouImmeubles=Immeuble.objects.filter(commune__nom='Bonou').order_by('-id')[:3]
    bonouQuartier=Chambres.objects.filter(immeuble__commune__nom='Bonou').order_by('-id')[:3]
    content = {
        'bonouImmeubles':bonouImmeubles,
        'bonouQuartiers':bonouQuartier,
    }
    return render(request, 'interface/communes/bonou.html',content) 
def dangbo(request):
    dangboImmeubles=Immeuble.objects.filter(commune__nom='Dangbo').order_by('-id')[:3]
    dangboQuartier=Chambres.objects.filter(immeuble__commune__nom='Dangbo').order_by('-id')[:3]
    content = {
        'dangboImmeubles':dangboImmeubles,
        'dangboQuartiers':dangboQuartier,
    }
    return render(request, 'interface/communes/dangbo.html',content) 
def ouere(request):
    ouereImmeubles=Immeuble.objects.filter(commune__nom='Adja-Ouèrè').order_by('-id')[:3]
    ouereQuartier=Chambres.objects.filter(immeuble__commune__nom='Adja-Ouèrè').order_by('-id')[:3]
    content = {
        'ouereImmeubles':ouereImmeubles,
        'ouereQuartiers':ouereQuartier,
    }
    return render(request, 'interface/communes/ouere.html',content) 
def ifangni(request):
    ifangniImmeubles=Immeuble.objects.filter(commune__nom='Ifangni').order_by('-id')[:3]
    ifangniQuartier=Chambres.objects.filter(immeuble__commune__nom='Ifangni').order_by('-id')[:3]
    content = {
        'ifangniImmeubles':ifangniImmeubles,
        'ifangniQuartiers':ifangniQuartier,
    }
    return render(request, 'interface/communes/ifangni.html',content) 
def ketou(request):
    ketouImmeubles=Immeuble.objects.filter(commune__nom='ketou').order_by('-id')[:3]
    ketouQuartier=Chambres.objects.filter(immeuble__commune__nom='ketou').order_by('-id')[:3]
    content = {
        'ketouImmeubles':ketouImmeubles,
        'ketouQuartiers':ketouQuartier,
    }
    return render(request, 'interface/communes/ketou.html',content) 
def pobe(request):
    pobeImmeubles=Immeuble.objects.filter(commune__nom='Pobè').order_by('-id')[:3]
    pobeQuartier=Chambres.objects.filter(immeuble__commune__nom='pobè').order_by('-id')[:3]
    content = {
        'pobeImmeubles':pobeImmeubles,
        'pobeQuartiers':pobeQuartier,
    }
    return render(request, 'interface/communes/pobe.html',content) 
def sakete(request):
    saketeImmeubles=Immeuble.objects.filter(commune__nom='Sakété').order_by('-id')[:3]
    saketeQuartier=Chambres.objects.filter(immeuble__commune__nom='Sakété').order_by('-id')[:3]
    content = {
        'saketeImmeubles':saketeImmeubles,
        'saketeQuartiers':saketeQuartier,
    }
    return render(request, 'interface/communes/sakete.html',content) 
def abomey(request):
    abomeyImmeubles=Immeuble.objects.filter(commune__nom='Abomey').order_by('-id')[:3]
    abomeyQuartier=Chambres.objects.filter(immeuble__commune__nom='Abomey').order_by('-id')[:3]
    content = {
        'abomeyImmeubles':abomeyImmeubles,
        'abomeyQuartiers':abomeyQuartier,
    }
    return render(request, 'interface/communes/abomey.html',content) 
def agbangnizoun(request):
    agbangnizounImmeubles=Immeuble.objects.filter(commune__nom='Agbangnizoun').order_by('-id')[:3]
    agbangnizounQuartier=Chambres.objects.filter(immeuble__commune__nom='Agbangnizoun').order_by('-id')[:3]
    content = {
        'agbangnizounImmeubles':agbangnizounImmeubles,
        'agbangnizounQuartiers':agbangnizounQuartier,
    }
    return render(request, 'interface/communes/agbangnizoun.html',content)

def bohicon(request):
    bohiconImmeubles=Immeuble.objects.filter(commune__nom='Bohicon').order_by('-id')[:3]
    bohiconQuartier=Chambres.objects.filter(immeuble__commune__nom='Bohicon').order_by('-id')[:3]
    content = {
        'bohiconImmeubles':bohiconImmeubles,
        'bohiconQuartiers':bohiconQuartier,
    }
    return render(request, 'interface/communes/bohicon.html',content)

def cove(request):
    coveImmeubles=Immeuble.objects.filter(commune__nom='Covè').order_by('-id')[:3]
    coveQuartier=Chambres.objects.filter(immeuble__commune__nom='Covè').order_by('-id')[:3]
    content = {
        'coveImmeubles':coveImmeubles,
        'coveQuartiers':coveQuartier,
    }
    return render(request, 'interface/communes/cove.html',content) 

def djidja(request):
    djidjaImmeubles=Immeuble.objects.filter(commune__nom='Djidja').order_by('-id')[:3]
    djidjaQuartier=Chambres.objects.filter(immeuble__commune__nom='Djidja').order_by('-id')[:3]
    content = {
        'djidjaImmeubles':djidjaImmeubles,
        'djidjaQuartiers':djidjaQuartier,
    }
    return render(request, 'interface/communes/djidja.html',content) 

def ouinhi(request):
    ouinhiImmeubles=Immeuble.objects.filter(commune__nom='Ouinhi').order_by('-id')[:3]
    ouinhiQuartier=Chambres.objects.filter(immeuble__commune__nom='Ouinhi').order_by('-id')[:3]
    content = {
        'ouinhiImmeubles':ouinhiImmeubles,
        'ouinhiQuartiers':ouinhiQuartier,
    }
    return render(request, 'interface/communes/ouinhi.html',content) 

def zagnanado(request):
    zagnanadoImmeubles=Immeuble.objects.filter(commune__nom='Zagnanado').order_by('-id')[:3]
    zagnanadoQuartier=Chambres.objects.filter(immeuble__commune__nom='Zagnanado').order_by('-id')[:3]
    content = {
        'zagnanadoImmeubles':zagnanadoImmeubles,
        'zagnanadoQuartiers':zagnanadoQuartier,
    }
    return render(request, 'interface/communes/zagnanado.html',content) 

def zakpota(request):
    zakpotaImmeubles=Immeuble.objects.filter(commune__nom='Za-Kpota').order_by('-id')[:3]
    zakpotaQuartier=Chambres.objects.filter(immeuble__commune__nom='Za-Kpota').order_by('-id')[:3]
    content = {
        'zakpotaImmeubles':zakpotaImmeubles,
        'zakpotaQuartiers':zakpotaQuartier,
    }
    return render(request, 'interface/communes/zakpota.html',content) 

def zogbodomey(request):
    zogbodomeyImmeubles=Immeuble.objects.filter(commune__nom='Zogbodomey').order_by('-id')[:3]
    zogbodomeyQuartier=Chambres.objects.filter(immeuble__commune__nom='Zogbodomey').order_by('-id')[:3]
    content = {
        'zogbodomeyImmeubles':zogbodomeyImmeubles,
        'zogbodomeyQuartiers':zogbodomeyQuartier,
    }
    return render(request, 'interface/communes/zogbodomey.html',content)


def dali(request):
    daliImmeubles=Immeuble.objects.filter(commune__nom='dali').order_by('-id')[:3]
    daliQuartier=Chambres.objects.filter(immeuble__commune__nom='dali').order_by('-id')[:3]
    content = {
        'daliImmeubles':daliImmeubles,
        'daliQuartiers':daliQuartier,
    }
    return render(request, 'interface/communes/dali.html',content) 

def klouekanme(request):
    klouekanmeImmeubles=Immeuble.objects.filter(commune__nom='Klouékanmè').order_by('-id')[:3]
    klouekanmeQuartier=Chambres.objects.filter(immeuble__commune__nom='Klouékanmè').order_by('-id')[:3]
    content = {
        'klouekanmeImmeubles':klouekanmeImmeubles,
        'klouekanmeQuartiers':klouekanmeQuartier,
    }
    return render(request, 'interface/communes/klouekanme.html',content) 

def porto(request):
    portoImmeubles=Immeuble.objects.filter(commune__nom='Porto-Novo').order_by('-id')[:3]
    portoQuartier=Chambres.objects.filter(immeuble__commune__nom='Porto-Novo').order_by('-id')[:3]
    print(portoQuartier)
    content = {
        'portoImmeubles':portoImmeubles,
        'portoQuartiers':portoQuartier,
    }
    return render(request, 'interface/communes/porto.html',content) 

def seme(request):
    semeImmeubles=Immeuble.objects.filter(commune__nom='Sèmè-Kpodji').order_by('-id')[:3]
    semeQuartier=Chambres.objects.filter(immeuble__commune__nom='Sèmè-Kpodji').order_by('-id')[:3]
    content = {
        'semeImmeubles':semeImmeubles,
        'semeQuartiers':semeQuartier,
    }
    return render(request, 'interface/communes/seme.html',content) 

#----------------------Rejoindre------------------------

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

    return render(request, 'interface/rejoindre.html', context)


def liste_rejoindre(request):
        context={
                    'listeRejoindres':RejoindreContact.objects.all().order_by('-id')
                }
        return render(request,'dashboards/liste_rejoindre.html',context)

def qualite(request):
    if request.method == 'POST':
        form = QualiteForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect("qualite")
    else:
        data={
            'qualites': Qualite.objects.all().order_by('-id'),
            'form':QualiteForm()
        }
    return render(request, 'dashboards/qualite.html',data)

@login_required
@user_passes_test(is_admin, login_url=reverse_lazy('error'))
def delete_rejoindre(request,):
    if request.method=='POST':
        id=request.POST['listeRejoindresId']
        RejoindreContact.objects.get(id=int(id)).delete()
        return redirect('liste_rejoindre')
    return render(request,'dashboards/liste_rejoindre.html') 


#******************************JSON Ajax********************************
def departemenCommune(request,id):
    commune=Commune.objects.filter(departement=id)
    serialized_data=serialize("json",commune)
    serialized_data=json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False,status=200)

def communeArrondissement(request,id):
    arrondissement=Arrondissement.objects.filter(commune=id)
    serialized_data=serialize("json",arrondissement)
    serialized_data=json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False,status=200)

def arrondissementQuartier(request,id):
    quartier=Quartier.objects.filter(arrondissement=id)
    serialized_data=serialize("json",quartier)
    serialized_data=json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False,status=200)

def proprietaireImmeuble(request,id):
    maison=Immeuble.objects.filter(proprietaire=id)
    serialized_data=serialize("json",maison)
    serialized_data=json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False,status=200)


#******************************* Pgination ****************************