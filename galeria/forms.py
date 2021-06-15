from django import forms
from django.forms import ModelForm
from .models import obradearte



class obradearteForm(ModelForm):

    class Meta:
        model = obradearte
        fields = ['nombreobra', 'dimenciones', 'añocreacion', 'categoria']