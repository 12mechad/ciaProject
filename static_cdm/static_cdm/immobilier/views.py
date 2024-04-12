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
    return render(request, 'interface/propos.html', data)

def beninLandLouer(request):
    operations_immeubles = Immeuble.objects.filter(operation__type='Location')
    operations_terrains = Terrain.objects.filter(operation__type='Location')
    quartier_search = request.GET.get('quartier')
    
    if quartier_search:
        operations_immeubles = operations_immeubles.filter(quartier__nom__icontains=quartier_search)
        operations_terrains = operations_terrains.filter(quartier__nom__icontains=quartier_search)
    
    context = {
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
        formContact = ContactezNousForm(request.POST)
        if formContact.is_valid():
           formContact.save()
        return redirect("contact_immobilier")
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