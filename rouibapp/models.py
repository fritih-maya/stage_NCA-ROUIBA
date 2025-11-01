from django.db import models
from django.core.exceptions import ValidationError
import calendar

from django.db import models

class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"



class Machine(models.Model):
    id_machine = models.AutoField(primary_key=True)
    format = models.CharField(max_length=100)
    nom_machine = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_machine
    
class Causes(models.Model):
    id_cause = models.AutoField(primary_key=True)
    nom_cause = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_cause
    
class Responsable(models.Model):
    id_resp = models.AutoField(primary_key=True)
    nom_resp = models.CharField(max_length=100)  

    def __str__(self):
        return self.nom_resp
    
class Type(models.Model):
    id_Type = models.AutoField(primary_key=True)
    nom_type = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_type
    
class Ligne(models.Model):
    id_ligne = models.AutoField(primary_key=True)
    nom_ligne = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_ligne
    
class faction(models.Model):
    id_faction = models.AutoField(primary_key=True)
    faction = models.CharField(max_length=100)

    def __str__(self):
        return self.faction



    
class Arret(models.Model):
    id_arret = models.AutoField(primary_key=True)
    date_arret = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    ligne = models.ForeignKey(Ligne, on_delete=models.SET_NULL, null=True)
    quart = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True)
    duree_arret = models.CharField(max_length=50)
    responsable = models.ForeignKey(Responsable, on_delete=models.SET_NULL, null=True)
    cause = models.ForeignKey(Causes, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Arret {self.id_arret} - {self.date_arret}"




class Production (models.Model):
    id_production = models.AutoField(primary_key=True)
    date = models.DateField()
    ligne = models.ForeignKey(Ligne, on_delete=models.SET_NULL, null=True)
    quart = models.CharField(max_length=50 , default= "Matin")
    equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True)
    cadence = models.FloatField(default=0) 
    temps_brut = models.IntegerField(null=True)
    temps_programme =  models.IntegerField(null=True)
    temps_non_programme =  models.IntegerField(null=True)
    theorique = models.IntegerField(null=True)
    realise =  models.IntegerField(null=True)
    ecart = models.IntegerField(null=True)
    trs = models.FloatField(null=True)
    temps_productif = models.FloatField(null=True)
    heure_arrets = models.FloatField(null=True)
    C = models.FloatField(null=True)
    intrants = models.FloatField(null=True)
    technique = models.FloatField(null=True)
    operationnel = models.FloatField(null=True)
    siroperie = models.FloatField(null=True)
    utilite = models.FloatField(null=True)
    espace = models.FloatField(null=True)
    Transports = models.FloatField(null=True)
    perte = models.IntegerField(null=True)
    nep_complet_mp_theorique = models.FloatField(null=True)
    nep_complet_mp_reel = models.FloatField(null=True)
    nep_complet_ecart = models.FloatField(null=True)
    nep_soude_mp_theorique = models.FloatField(null=True)
    nep_soude_mp_reel = models.FloatField(null=True)
    nep_soude_ecart = models.FloatField(null=True)
    nia_theorique = models.FloatField(null=True)
    nia_reel = models.FloatField(null=True)
    nia_ecart = models.FloatField(null=True)
    total_arrets_theorique_program = models.FloatField(null=True)
    total_arrets_reels_program = models.FloatField(null=True)
    total_depass = models.FloatField( null=True)
    revision_theorique = models.FloatField(null=True)
    revision_reel = models.FloatField(null=True)
    revision_ecart = models.FloatField(null=True)
    total_arrets_non_progr = models.FloatField(null=True)
    total_arrets = models.FloatField(null=True)
    temps_productif = models.FloatField(null=True)
    total = models.FloatField(null=True)


    def save(self, *args, **kwargs):
       if self.ligne == "F":
            self.cadence = 24000
       elif self.ligne == "N":
            self.cadence = 12000  
       elif self.ligne == "H":
            self.cadence = 24000
       elif self.ligne == "G":
            self.cadence = 9000
         
         
         # tu peux ajuster la valeur
       super().save(*args, **kwargs)

    def __str__(self):
        return f"Production {self.id_production} - {self.date}"


class DemoRequest(models.Model):
    DateProduction= models.DateField()
    Ligne = models.CharField(max_length=100)
    quart = models.CharField(max_length=100)
    Cadence = models.IntegerField()
    Temps_Brut = models.IntegerField()
    Temps_Programmes = models.IntegerField()
    Temps_non_Programmes = models.IntegerField()
    Theorique = models.IntegerField()
    Realise = models.IntegerField()
    ecart = models.IntegerField(default=0)
    Trs = models.IntegerField()
    heure_arrets = models.FloatField(default=0)
    C = models.FloatField()
    intrants = models.FloatField(default=0)
    technique = models.FloatField(default=0)
    operationnel = models.FloatField(default=0)
    siroperie = models.FloatField(default=0)
    utilite = models.FloatField(default=0)
    espace = models.FloatField(default=0)
    transports = models.FloatField(default= 0)
    perte = models.IntegerField()
    NEP_Complet_MP_theorique = models.FloatField()
    NEP_Complet_MP_Reel = models.IntegerField()
    NEP_Complet_Ecart = models.FloatField()
    NEP_Soude_MP_theorique = models.FloatField()
    NEP_Soude_MP_Reel = models.FloatField()
    NEP_Soude_MP_Ecart = models.FloatField()
    NIA_theorique = models.FloatField()
    NIA_Reel = models.FloatField()
    NIA_Ecart = models.FloatField()
    Total_ARRETS_THEORIQUE_PROGRAM = models.FloatField()
    Total_ARRETS_REELS_PROGRAM = models.FloatField()
    Total_DEPASSEMENTS = models.FloatField()
    Revision_theorique = models.FloatField()
    Revision_Reel = models.FloatField()
    Revision_Ecart = models.FloatField()
    total_arrets_non_progr = models.FloatField()
    total_arrets = models.FloatField()
    Temps_productif = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"Demo Request {self.id} - {self.name}"
    
class Dm(models.Model):
    id_dm = models.AutoField(primary_key=True)
    date_dm = models.DateField()
    ligne = models.ForeignKey(Ligne, on_delete=models.SET_NULL, null=True)
    nbr_arret = models.CharField(max_length=50)
    duree_arret = models.FloatField(null=True, blank=True) 
    duree_arret_programme = models.CharField(max_length=50)
    temps_requis = models.CharField(max_length=50)
    siroperie = models.FloatField(null=True, blank=True)
    utilite = models.FloatField(null=True, blank=True)
    MTBF = models.FloatField()
    MTTR = models.FloatField()
    DS = models.FloatField ()
    DE = models.FloatField()
    DM = models.FloatField()
    taux_panne = models.FloatField()
    TRS = models.FloatField()
    TRG = models.FloatField()
    perte_pourcentage = models.FloatField()
    TU = models.FloatField()
    TUBIS = models.FloatField()
    TRP = models.FloatField()
    TRL = models.FloatField()
    TRO = models.FloatField()
    TRE = models.FloatField()
    perte = models.FloatField(null=True, blank=True)
    realise = models.FloatField(null=True, blank=True)
    Prevu = models.FloatField()
    cadence = models.FloatField(null=True, blank=True)
    HK = models.FloatField()

    def _str_(self):
        return f"DM {self.id_dm} - {self.date_dm}"
    

class EquipePET(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class MachinePET(models.Model):
    id_machine = models.AutoField(primary_key=True)
    format = models.CharField(max_length=100)
    nom_machine = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_machine
    
class CausesPET(models.Model):
    id_cause = models.AutoField(primary_key=True)
    nom_cause = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_cause
    
class ResponsablePET(models.Model):
    id_resp = models.AutoField(primary_key=True)
    nom_resp = models.CharField(max_length=100)  

    def __str__(self):
        return self.nom_resp
    

class LignePET(models.Model):
    id_ligne = models.AutoField(primary_key=True)
    nom_ligne = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_ligne
    
    
class ArretPET(models.Model):
    id_arretPET = models.AutoField(primary_key=True)
    date_arret = models.DateField()
    equipe = models.ForeignKey(EquipePET, on_delete=models.SET_NULL, null=True)
    ligne = models.ForeignKey(LignePET, on_delete=models.SET_NULL, null=True)
    quart = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    machine = models.ForeignKey(MachinePET, on_delete=models.SET_NULL, null=True)
    duree_arret = models.CharField(max_length=50)
    responsable = models.ForeignKey(ResponsablePET, on_delete=models.SET_NULL, null=True)
    cause = models.ForeignKey(CausesPET, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Arret {self.id_arret} - {self.date_arret}"



class Employe(models.Model):
    TYPE_CHOICES = [
        ('PET', 'PET'),
        ('CARTON', 'Carton'),
    ]
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    type_equipe = models.CharField(max_length=10, choices=TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.type_equipe}"
    




# ===== MODELS.PY - AJOUT DU MODÈLE PRODUCTION PET =====

class ProductionPET(models.Model):
    id_production = models.AutoField(primary_key=True)
    
    # Informations de base
   
    date = models.DateField()
   
    
    # Relations
    faction = models.ForeignKey('FactionPET', on_delete=models.SET_NULL, null=True, blank=True)
    equipe = models.ForeignKey(EquipePET, on_delete=models.SET_NULL, null=True)
    ligne = models.ForeignKey(LignePET, on_delete=models.SET_NULL, null=True)
    
    # Données de production
    format_produit = models.CharField(max_length=100, blank=True)
    cadence = models.FloatField(default=0)
    temps_brut = models.IntegerField(default=8)
    temps_programme = models.IntegerField(default=0)
    temps_non_programme = models.IntegerField(default=0)
    theorique = models.IntegerField(default=0)
    realise = models.IntegerField(default=0)
    ecart = models.IntegerField(default=0)
    trs_pourcentage = models.FloatField(default=0)
    temps_productif = models.FloatField(default=0)
    heures_arrets = models.FloatField(default=0)
    
    # Coefficients et variables
    c = models.FloatField(default=0)
    intrants = models.FloatField(default=0)
    technique = models.FloatField(default=0)
    operationnel = models.FloatField(default=0)
    siroperie = models.FloatField(default=0)
    utilite = models.FloatField(default=0)
    espace = models.FloatField(default=0)
    transports = models.FloatField(default=0)
    
    # Personnel (peut être étendu selon vos besoins)
    chef_ligne = models.CharField(max_length=100, blank=True)
    conducteur_souffleuse = models.CharField(max_length=100, blank=True)
    conducteur_remplisseuse = models.CharField(max_length=100, blank=True)
    conducteur_etiqueteuse = models.CharField(max_length=100, blank=True)
    conducteur_fardeleuse = models.CharField(max_length=100, blank=True)
    conducteur_robot = models.CharField(max_length=100, blank=True)
    operateur = models.CharField(max_length=100, blank=True)
    mireur_ligne = models.CharField(max_length=100, blank=True)
    cariste = models.CharField(max_length=100, blank=True)
    
    # Pertes
    c_pertes = models.FloatField(default=0)
    pertes_vides = models.IntegerField(default=0)
    pertes_pleines = models.IntegerField(default=0)
    total_perte = models.IntegerField(default=0)
    perte_conducteur_fardeleuse = models.FloatField(default=0)
    perte_conducteur_robot = models.FloatField(default=0)
    perte_operateur = models.FloatField(default=0)
    supply_chain = models.FloatField(default=0)
    technicien_labo = models.FloatField(default=0)
    
    # Arrêts programmés
    fermeture = models.FloatField(default=0)
    changement_format_theorique = models.FloatField(default=0)
    changement_format_reel = models.FloatField(default=0)
    changement_format_ecart = models.FloatField(default=0)
    
    entretien_hebdo_theorique = models.FloatField(default=0)
    entretien_hebdo_reel = models.FloatField(default=0)
    entretien_hebdo_ecart = models.FloatField(default=0)
    
    nep_complet_mp_theorique = models.FloatField(default=0)
    nep_complet_mp_reel = models.FloatField(default=0)
    nep_complet_ecart = models.FloatField(default=0)
    
    nep_soude_mp_theorique = models.FloatField(default=0)
    nep_soude_mp_reel = models.FloatField(default=0)
    nep_soude_mp_ecart = models.FloatField(default=0)
    
    nia_theorique = models.FloatField(default=0)
    nia_reel = models.FloatField(default=0)
    nia_ecart = models.FloatField(default=0)
    
    revision_theorique = models.FloatField(default=0)
    revision_reel = models.FloatField(default=0)
    revision_ecart = models.FloatField(default=0)
    
    # Totaux
    total_arrets_theorique_program = models.FloatField(default=0)
    total_arrets_reels_program = models.FloatField(default=0)
    total_depassements = models.FloatField(default=0)
    total_arrets_non_progr = models.FloatField(default=0)
    total_arrets = models.FloatField(default=0)
    temps_productif_total = models.FloatField(default=0)
    total_final = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        # Calculs automatiques
        self.temps_non_programme = self.temps_brut - self.temps_programme
        self.ecart = self.theorique - self.realise
        if self.theorique > 0:
            self.trs_pourcentage = (self.realise / self.theorique) * 100
        if self.cadence > 0:
            self.temps_productif = self.realise / self.cadence
            self.heures_arrets = self.ecart / self.cadence
        
        # Calcul des écarts
        self.changement_format_ecart = self.changement_format_reel - self.changement_format_theorique
        self.entretien_hebdo_ecart = self.entretien_hebdo_reel - self.entretien_hebdo_theorique
        self.nep_complet_ecart = self.nep_complet_mp_reel - self.nep_complet_mp_theorique
        self.nep_soude_mp_ecart = self.nep_soude_mp_reel - self.nep_soude_mp_theorique
        self.nia_ecart = self.nia_reel - self.nia_theorique
        self.revision_ecart = self.revision_reel - self.revision_theorique
        
        # Calcul des totaux
        self.total_perte = self.pertes_vides + self.pertes_pleines
        self.total_arrets_theorique_program = (
            self.changement_format_theorique + self.entretien_hebdo_theorique + 
            self.nep_complet_mp_theorique + self.nep_soude_mp_theorique + 
            self.nia_theorique + self.revision_theorique
        )
        self.total_arrets_reels_program = (
            self.changement_format_reel + self.entretien_hebdo_reel + 
            self.nep_complet_mp_reel + self.nep_soude_mp_reel + 
            self.nia_reel + self.revision_reel
        )
        self.total_depassements = (
            self.changement_format_ecart + self.entretien_hebdo_ecart + 
            self.nep_complet_ecart + self.nep_soude_mp_ecart + 
            self.nia_ecart + self.revision_ecart
        )
        self.total_arrets = self.total_arrets_reels_program + self.total_arrets_non_progr
        self.temps_productif_total = self.temps_productif
        self.total_final = self.temps_productif_total + self.total_arrets

        def save(self, *args, **kwargs):
         if self.format_produit == "25cl":
            self.cadence = 24000
         elif self.format_produit == "33cl":
            self.cadence = 24000  
         elif self.format_produit == "75cl":
            self.cadence = 18000
         elif self.format_produit == "100cl":
            self.cadence = 15000
         elif self.format_produit == "200cl":
              self.cadence = 7500
         
         
         
         # tu peux ajuster la valeur
        super().save(*args, **kwargs)
      
    
    def __str__(self):
        return f"Production PET {self.id_production} - {self.date}"


class FactionPET(models.Model):
    id_faction = models.AutoField(primary_key=True)
    nom_faction = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_faction

# Ajoutez ce modèle dans votre fichier models.py

class DmPET(models.Model):
    id_dm = models.AutoField(primary_key=True)
    date_dm = models.DateField()
    ligne = models.ForeignKey(LignePET, on_delete=models.CASCADE)
    nbr_arret = models.IntegerField(null=True, blank=True)
    duree_arret = models.FloatField(null=True, blank=True)
    duree_arret_programme = models.FloatField(null=True, blank=True)
    temps_requis = models.FloatField(null=True, blank=True)
    siroperie = models.FloatField(null=True, blank=True)
    utilite = models.FloatField(null=True, blank=True)
    MTBF = models.CharField(max_length=100, null=True, blank=True)
    MTTR = models.CharField(max_length=100, null=True, blank=True)
    DS = models.CharField(max_length=100, null=True, blank=True)
    DE = models.CharField(max_length=100, null=True, blank=True)
    DM = models.CharField(max_length=100, null=True, blank=True)
    taux_panne = models.CharField(max_length=100, null=True, blank=True)
    TRS = models.CharField(max_length=100, null=True, blank=True)
    TRG = models.CharField(max_length=100, null=True, blank=True)
    perte_pourcentage = models.CharField(max_length=100, null=True, blank=True)
    TU = models.CharField(max_length=100, null=True, blank=True)
    TUBIS = models.CharField(max_length=100, null=True, blank=True)
    TRP = models.CharField(max_length=100, null=True, blank=True)
    TRL = models.CharField(max_length=100, null=True, blank=True)
    TRO = models.CharField(max_length=100, null=True, blank=True)
    TRE = models.CharField(max_length=100, null=True, blank=True)
    perte = models.CharField(max_length=100, null=True, blank=True)
    realise = models.CharField(max_length=100, null=True, blank=True)
    cadence = models.CharField(max_length=100, null=True, blank=True)
    Prevu = models.CharField(max_length=100, null=True, blank=True)
    HK = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'dm_pet'
        verbose_name = "DM PET"
        verbose_name_plural = "DMs PET"

    def __str__(self):
        return f"DM PET {self.date_dm} - Ligne {self.ligne.nom_ligne if self.ligne else 'N/A'}"