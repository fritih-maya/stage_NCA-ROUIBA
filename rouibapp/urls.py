from django.urls import path
from .views import login_view
from . import views 
from .views import ProductionListView
from .views import get_temps_arret, get_duree_arret_programme, get_siroperie, get_utilite

urlpatterns = [
  # LES URLS DE LA SIDEBAR
  path('', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('home/', views.home, name='home'),
  path('equipe/', views.equipe, name='equipe'),
  path('statistiques/', views.statistiques, name='statistiques'),
  path('carton/', views.carton, name='carton'),
  path('production/', views.production_view, name='production'),
  path('dm/', views.dm, name='dm'), 
  path('PET/', views.PET, name='PET'),
  path('home_pet/', views.home_pet, name='home_pet'),
  path('statistiques_pet/', views.statistiques_pet, name='statistiques_pet'),


  #LES URLS DE L'AJOUT ET MODIFICATION DES EMPLOYES  
  path('ajouter_employe/', views.ajouter_employe, name='ajouter_employe'),
  path('modifier_employe/<int:id_equipe>/', views.modifier_employe, name='modifier_employe'),
  path('supprimer_employe/<int:id_equipe>/', views.supprimer_employe, name='supprimer_employe'),

   
  #LES URLS DE L'AJOUT ET MODIFICATION DES ARRETS 
  path('carton/ajouter_arret/', views.ajouter_arret_carton, name='ajouter_arret_carton'),
  path('carton/modifier_arret/<int:id_arret>/', views.modifier_arret_carton, name='modifier_arret_carton'),
  path('carton/supprimer_arret/<int:id_arret>/', views.supprimer_arret_carton, name='supprimer_arret_carton'),


  #LES URLS DE L'AJOUT ET MODIFICATION DES PRODUCTIONS 
  path('productions/', ProductionListView.as_view(), name='production_list'),
  path('ajouter_production/', views.ajouter_production, name='ajouter_production'),
  path('supprimer_production/<int:id>/', views.supprimer_production, name='supprimer_production'),
  path('modifier_production/<int:id>/', views.modifier_production, name='modifier_production'),


  #LES URLS SEPCIAUX ARRET ET PRODUCTION 
  path('get_equipe_by_date_quart_ligne/', views.get_equipe_by_date_quart_ligne, name='get_equipe_by_date_quart_ligne'),
  path('get_duree_arret_carton/', views.get_duree_arret_carton, name='get_duree_arret_carton'),
  path('get_durees_arret_types/', views.get_durees_arret_types, name='get_durees_arret_types'),


  #LES URLS SEPCIAUX DM
  path('get_temps_arret/', get_temps_arret, name='get_temps_arret'),
  path('get_duree_arret_programme/', get_duree_arret_programme, name='get_duree_arret_programme'),
  path('get_siroperie/', get_siroperie, name='get_siroperie'),
  path('get_utilite/', get_utilite, name='get_utilite'),
  path('get_perte/', views.get_perte, name='get_perte'),
  path('get_realise/', views.get_realise, name='get_realise'),
  path('get_cadence/', views.get_cadence, name='get_cadence'),
  path('get_perte_pourcentage/', views.get_perte_pourcentage, name='get_perte_pourcentage'),
  path('get_hk/', views.get_hk, name='get_hk'),
  path('get_trs/', views.get_trs, name='get_trs'),
  path('get_prevu/', views.get_prevu, name='get_prevu'),

  

  #LES URLS DE L'AJOUT ET MODIFICATION ET SUPPRESSION DES DM  
  path('ajouter_dm/', views.ajouter_dm, name='ajouter_dm'),
  path('supprimer_dm/<int:id_dm>/', views.supprimer_dm, name='supprimer_dm'),
  path("modifier_dm/<int:id_dm>/", views.modifier_dm, name="modifier_dm"),



  #LES URLS DE L'AJOUT ET MODIFICATION DES EMPLOYES PET  
  path('modifier_employe_pet/<int:id_equipe>/', views.modifier_employe_pet, name='modifier_employe_pet'),
  path('supprimer_employe_pet/<int:id_equipe>/', views.supprimer_employe_pet, name='supprimer_employe_pet'),

  
  #LES URLS DE L'AJOUT ET MODIFICATION DES ARRETS PET 
  path('PET_arret/ajouter_arret_pet/', views.ajouter_arret_pet, name='ajouter_arret_pet'),
  path('PET_arret/modifier_arret_pet/<int:id_arret_pet>/', views.modifier_arret_pet, name='modifier_arret_pet'),
  path('PET_arret/supprimer_arret_pet/<int:id_arret_pet>/', views.supprimer_arret_pet, name='supprimer_arret_pet'),


  #LES URLS DE L'AJOUT ET MODIFICATION DES PRODUCTION PET
  path('production_pet/', views.production_pet, name='production_pet'),
  path('production_pet/ajouter/', views.ajouter_production_pet, name='ajouter_production_pet'),
  path('production_pet/modifier/<int:id_production>/', views.modifier_production_pet, name='modifier_production_pet'),
  path('production_pet/supprimer/<int:id_production>/', views.supprimer_production_pet, name='supprimer_production_pet'),

  # URLs pour DM PET
  path('dm-pet/', views.dm_pet, name='dm_pet'),
  path('ajouter-dm-pet/', views.ajouter_dm_pet, name='ajouter_dm_pet'),
  path('modifier_dm_pet/<int:id_dm>/', views.modifier_dm_pet, name='modifier_dm_pet'),
  path('supprimer-dm-pet/<int:id_dm>/', views.supprimer_dm_pet, name='supprimer_dm_pet'),
  
  #LES URLS SPECIAUX PRODUCTION PET
  path('ajax/get_equipe_by_date_quart_ligne_pet/', views.get_equipe_by_date_quart_ligne_pet, name='get_equipe_by_date_quart_ligne_pet'),
  path('ajax/get_duree_arret_by_date_quart_pet/', views.get_duree_arret_by_date_quart_pet, name='get_duree_arret_by_date_quart_pet'),
  path('ajax/get_duree_arret_type_pet/', views.get_duree_arret_type_pet, name='get_duree_arret_type_pet'),
  path('ajax/get_lignepet_by_date_quart_pet/', views.get_lignepet_by_date_quart_pet, name='get_lignepet_by_date_quart_pet'),
  

  #LES URLS SPECIAUX DM PET
  path('get_temps_arret_pet/', views.get_temps_arret_pet, name='get_temps_arret_pet'),
  path('get_duree_arret_programme_dm_pet/', views.get_duree_arret_programme_dm_pet, name='get_duree_arret_programme_dm_pet'),
  path('get_siroperie_pet/', views.get_siroperie_pet, name='get_siroperie_pet'),
  path('get_utilite_pet/', views.get_utilite_pet, name='get_utilite_pet'),
  path('get_trg_pet/', views.get_trg_pet, name='get_trg_pet'),
  path('get_perte_pet/', views.get_perte_pet, name='get_perte_pet'),
  path('get_perte_pourcentage_pet/', views.get_perte_pourcentage_pet, name='get_perte_pourcentage_pet'),
  path('get_hk_pet/', views.get_hk_pet, name='get_hk_pet'),
  path('get_cadence_pet/', views.get_cadence_pet, name='get_cadence_pet'),
  path('get_trs_pet/', views.get_trs_pet, name='get_trs_pet'),
  path('get_realise_pet/', views.get_realise_pet, name='get_realise_pet'),
  path('get_prevu_dm_pet/', views.get_prevu_dm_pet, name='get_prevu_dm_pet'),

  #LES URLS D EXPORT EXCEL
  path('carton/export_arrets_excel/', views.export_arrets_excel, name='export_arrets_excel'),
  path('carton/export_production_excel/', views.export_production_excel, name='export_production_excel'),
  path('carton/export_dm_excel/', views.export_dm_excel, name='export_dm_excel'),
  path('pet/export_arrets_pet_excel/', views.export_arrets_pet_excel, name='export_arrets_pet_excel'),
  path('pet/export_production_pet_excel/', views.export_production_pet_excel, name='export_production_pet_excel'),
  path('pet/export_dm_pet_excel/', views.export_dm_pet_excel, name='export_dm_pet_excel'),
 
]