from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('departement', views.departement, name='departement'),
    path('update_departement/<int:pk>', views.update_departement, name='update_departement'),
    
    #Arrondissement
    path('arrondissement', views.arrondissement, name='arrondissement'),
    path('update_arrondissement/<int:pk>', views.update_arrondissement, name='update_arrondissement'),
    
    #Commune
    path('commune', views.commune, name='commune'),
    path('update_commune/<int:pk>', views.update_commune, name='update_commune'),
    
    #Proprietaire
    # path('proprietaire', views.proprietaire, name='proprietaire'),
    path('liste_proprietaire', views.listeProprietaire, name='liste_proprietaire'),
    path('delete_proprietaire', views.deleteProporietaire, name='delete_proprietaire'),
    path('update_proprietaire/<int:pk>', views.update_profile, name='update_proprietaire'),
    
    #Operation
    path('operation', views.operation, name='operation'),
    path('delete', views.deleteOperation, name='delete'),
    path('update_operation/<int:pk>', views.update_operation, name='update_operation'),
    
    #Quartier
    path('quartier', views.quartier, name='quartier'),
    path('update_quartier/<int:pk>', views.update_quartier, name='update_quartier'),
    
    #Immeuble
    path('immeuble', views.immeuble, name='immeuble'),
    path('departemenCommune/<int:id>', views.departemenCommune, name='departemenCommune'),
    path('communeArrondissement/<int:id>', views.communeArrondissement, name='communeArrondissement'),
    path('arrondissementQuartier/<int:id>', views.arrondissementQuartier, name='arrondissementQuartier'),
    path('liste_immeuble', views.listeImmeuble, name='liste_immeuble'),
    path('delete_immeuble', views.deleteimmeuble, name='delete_immeuble'),
    path('update_immeuble/<int:pk>', views.update_immeuble, name='update_immeuble'),
    path('update_statut/<int:pk>', views.edit_statut, name='update_statut'),
    
    #Annonce
    path('annonce', views.annonce, name='annonce'),
    path('delete_annonce', views.deleteAnnonce, name='delete_annonce'),
    path('update_annonce/<int:pk>', views.update_annonce, name='update_annonce'),

    #Terrain
    path('terrain', views.terrain, name='terrain'),
    path('liste_terrain', views.listeTerrain, name='liste_terrain'),
     path('delete_terrain', views.deleteterrain, name='delete_terrain'),
    path('update_terrain/<int:pk>', views.update_terrain, name='update_terrain'),
    
    #habital
    path('habitat', views.habitat, name='habitat'),
    
    #logement
    path('logement', views.chambre, name='logement'),
    
     #salon
    path('salon', views.salon, name='salon'),
    
     #salon
    path('cuisine', views.cuisine, name='cuisine'),
    
     #douche
    path('douche', views.douche, name='douche'),
    
    #douche
    path('balcon', views.balcon, name='balcon'),
    
    #Chambre
    # path('chambres', views.chambres, name='chambres'),
     path('modifier/', views.modify_profile, name='modifier'), 
    path('proprietaireImmeuble/<int:id>', views.proprietaireImmeuble, name='proprietaireImmeuble'),
    path('liste_chambre', views.listeChambres, name='liste_chambre'),
    path('delete_chambre',views.deletechambre, name='delete_chambre'),
    path('immobilier/update_chambre/<int:pk>/', views.update_chambre, name='update_chambre'),
    
    #Types
    path('types', views.types, name='types'),
    path('delete_types', views.deletetypes, name='delete_types'),
    path('update_types/<int:pk>', views.update_types, name='update_types'),
    
    #Offre
    path('offre', views.offre, name='offre'),
    path('update_offre/<int:pk>', views.update_offre, name='update_offre'),
    
    #devis
    path('devisConstruction', views.devis, name='devisConstruction'),
    path('liste_devis', views.listeDevis, name='liste_devis'),
    path('update_devis/<int:pk>', views.update_devis, name='update_devis'),
    
    #Expertise
    path('expertiseImmobilier', views.expertise, name='expertiseImmobilier'),
    path('liste_expertise', views.listeExpertise, name='liste_expertise'),
    path('update_expertise/<int:pk>', views.update_expertise, name='update_expertise'),
    
    # La gestions est propriétaire 
    #Mon Espace
    path('compte', views.monEspace, name="compte"),
    path('detailspace/<int:chambre_id>/', views.detailEspace, name='detailspace'),
    
    #Construiction BTP
    path('plan', views.plan, name='plan'),
    path('liste_plan', views.listePlan, name='liste_plan'),
    
    # Les urls sur l'interface de beninland
    path('accueil', views.beninLand, name='accueil'),
    path('faq', views.faq, name='faq'),
    # path('accueil_recherche', views.beninLandRechercher, name='accueil_recherche'),
    path('propos_immobilier', views.beninLandPropos, name='propos_immobilier'),
    path('louer', views.beninLandLouer, name='louer'),
    path('acheter', views.beninLandAcheter, name='acheter'),
    path('terrains', views.beninLandterrain, name='terrains'),
    path('construire', views.beninLandPlan, name='construire'),
    path('liste_plan/<int:plan_id>/', views.liste_plan, name='liste_plan'),
    path('detail_plan/<int:plan_id>/', views.detail_plan, name='detail_plan'),
    path('expertise', views.beninLandExpertise, name='expertise'),
    path('devis', views.beninLandDevis, name='devis'),
    path('contact_immobilier', views.beninLandContact, name='contact_immobilier'),
    path('contact', views.Contact, name='contact'),
    path('chambre/<int:id>/detail', views.chambreDetail, name='detail'),
    path('terrain/<int:id>/detail', views.terrainDetail, name='detail'),
    path('liste_chambres_immeubles/<int:immeuble_id>/', views.liste_chambres_immeubles, name='liste_chambres_immeubles'),
    path('details_chambre/<int:chambre_id>/', views.details_chambre, name='details_chambre'),

    
    
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)