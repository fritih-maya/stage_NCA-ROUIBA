from django import forms
from .models import Production, Ligne

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = ['date', 'ligne']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ligne': forms.Select(attrs={'class': 'form-control'}),
            
            
        }
    
    # Champs manuels pour les valeurs numériques
    cadence_value = forms.IntegerField(label="Cadence", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    temps_brut_value = forms.IntegerField(label="Temps Brut", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    temps_programme_value = forms.IntegerField(label="Temps Programme", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    temps_non_programme_value = forms.IntegerField(label="Temps Non Programme", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    theorique_value = forms.IntegerField(label="Théorique", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    realise_value = forms.IntegerField(label="Réalisé", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    trs_value = forms.FloatField(label="TRS", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    heure_arrets_value = forms.FloatField(label="Heure Arrêts", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    ecart_value = forms.IntegerField(label="Ecart", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    c_value = forms.FloatField(label="C", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    perte_value = forms.FloatField(label="Perte", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_complet_mp_theorique_value = forms.FloatField(label="NEP Complet MP Théorique", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_complet_mp_reel_value = forms.FloatField(label="NEP Complet MP Réel", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_complet_ecart_value = forms.FloatField(label="NEP Complet Écart", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_soude_mp_theorique_value = forms.FloatField(label="NEP Soudé MP Théorique", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_soude_mp_reel_value = forms.FloatField(label="NEP Soudé MP Réel", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nep_soude_ecart_value = forms.FloatField(label="NEP Soudé Écart", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nia_theorique_value = forms.FloatField(label="NIA Théorique", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nia_reel_value = forms.FloatField(label="NIA Réel", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    nia_ecart_value = forms.FloatField(label="NIA Écart", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_arrets_theorique_program_value = forms.FloatField(label="Total Arrêts Théorique Program", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_arrets_reels_program_value = forms.FloatField(label="Total Arrêts Réels Program", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_depass_value = forms.FloatField(label="Total Dépassements", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    revision_theorique_value = forms.FloatField(label="Révision Théorique", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    revision_reel_value = forms.FloatField(label="Révision Réel", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    revision_ecart_value = forms.FloatField(label="Révision Écart", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_arrets_non_progr_value = forms.FloatField(label="Total Arrêts Non Progr", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_arrets_value = forms.FloatField(label="Total Arrêts", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    temps_productif_value = forms.FloatField(label="Temps Productif", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    total_value = forms.FloatField(label="Total", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))

    

# Dans forms.py
from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'type_equipe']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'type_equipe': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'type_equipe': 'Type d\'équipe',
        }