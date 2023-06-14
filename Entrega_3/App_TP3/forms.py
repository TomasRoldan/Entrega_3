from django import forms

class CamisetaForm(forms.Form):
    equipo = forms.CharField(max_length=30)
    año = forms.IntegerField()
    equipación = forms.CharField(max_length= 10)
    talle = forms.CharField(max_length=4)
    precio = forms.IntegerField()

class PantalonForm(forms.Form):
    equipo = forms.CharField(max_length=30)
    año = forms.IntegerField()
    equipación = forms.CharField(max_length= 10)
    modelo = forms.CharField(max_length=10)
    talle = forms.CharField(max_length=4)  
    precio = forms.IntegerField()



class AbrigoForm(forms.Form):
    equipo = forms.CharField(max_length=30)
    año = forms.IntegerField()
    modelo = forms.CharField(max_length=15)
    talle = forms.CharField(max_length=4)
    precio = forms.IntegerField()

class BuscarCamisetaForm(forms.Form):
    equipo = forms.CharField()