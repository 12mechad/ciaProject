from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    # path('', views.index, name='home'),
    path('error', views.error, name='error'),
    path('erreur-auteur', views.error_auteur, name='error_auteur'),
     #Les Categories
    path('dashboard', views.add_categorie, name='categorie'),
    path('update_category/<int:pk>', views.update_category, name='update_category'),
    path('update_statut/<int:pk>', views.edit_statut, name='update_statut'),
    path('delete', views.delete, name='delete'),
    
    #Les AUteurs
    path('auteur', views.add_auteur, name='auteur'),
   
    path('liste_auteurs', views.publicationAdmin, name='liste_auteurs'),
    
    
    #Les Edtions
    path('liste_editions', views.listEdition, name='liste_editions'),
    path('editer', views.editer, name='editer'),
    path('update_edition/<int:pk>', views.update_edition, name='update_edition'),
    path('delete_edition', views.delete_edition, name='delete_edition'),
    
    path('passer_statut/<int:statut_id>/',views.statut, name='passer_statut'),
    # Autres URLs
 
    path('inscription', views.inscription, name='inscription'),
    
    
    # Menu Utilisateurs
    path('utilisateur', views.auteur, name='utilisateur'),
    path('editeur', views.editeur, name='editeur'),
    path('liste', views.publication, name='publication'),
    
    # Pour la partie vue client du site d'edition
    path('racines', views.accueil, name='racines'),
    
      # Pour la partie vue client du site d'edition
    path('propos', views.propos, name='propos'),
    
    # Pour les edition disponible
    path('edition', views.edition, name='edition'),
     path('editions', views.editions, name='editions'),
     # Pour les edition disponible
    path('librairie', views.librairie, name='librairie'),
    
       # Pour les contacts 
    path('contact', views.contact, name='contact'),
    
      # Pour les contacts 
    path('modal', views.mod, name='modal'),
    
     # Pour les auteurs
    path('listes_auteurs', views.listes_auteurs, name='listes_auteurs'),
    
     # Pour les auteurs
    path('auteur/<int:id>/blogauteur', views.blogAuteurs, name='blogauteur'),
    
    
    # Deatil des actualité
    path('livre/<int:id>/detail', views.DetailActualite, name='detail_actualite'),
    # Detail Edition 
    path('categorie/<int:id>/blog', views.detailblog, name='blog'),
    path('agenda/<int:id>/detaille', views.detaille, name='detaille'),
    path('listes/<int:id>/listeseditions',views.listesEdition,name='listeseditions'),

  
########################################################################################"
# Les vue de la page principale de cigroup
 # Detail Edition 
  path('', views.agenda, name='agenda'),
  path('propos_agenda',views.propos_agenda, name='propos_agenda'),
  path('service_agenda',views.propos_agenda, name='service_agenda'),


  #########################"------------Presse"############################################
  path('presse',views.presse, name='presse'),
  #########################----------Evénements ###########################################
  path('evenement',views.evenement, name='evenement'),
  path('type_evenement', views.typeEvenement, name='type_evenement'),
  path('evenement_Edition', views.evenementEdition, name='evenement_Edition'),
  path('prix', views.prix, name='prix'),
  path('festival', views.festival, name='festival'),
  path('projet', views.projet, name='projet'),
  path('Type_edition', views.Type_edition, name='Type_edition'),
  path('thematiques', views.thematiques, name='thematiques'),
  path('list_contacts', views.list_contacts, name='list_contacts'),
  ################################ Formulaire pour edition ##########################
  

]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)