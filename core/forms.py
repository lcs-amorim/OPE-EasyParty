from django import forms

from core.models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'