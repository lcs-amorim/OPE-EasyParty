from django import forms

from core.models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["nome_u","user_name","email_u","cpf","telefone_u","endereco_u","news"]