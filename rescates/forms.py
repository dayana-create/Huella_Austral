from django import forms
from .models import ejemplar

class ejemplarForm(forms.ModelForm):
    class meta:
        model = ejemplar
        fields = ['especies','nombre','peso_kg','fecha_ingreso','liberado']
        widgets = {
            'especie':forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'peso_kg': forms.NumberInput(attrs={'class':'form-control','step':'0.01'}),
            'fecha_ingreso': forms.DateInput(attrs={'class':'form-control','type':'date'},format='%y-%m-%d'),
            'liberado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
        
        
        

