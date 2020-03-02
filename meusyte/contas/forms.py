from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    
   first primeiro_nome = forms.CharFiel('Primeiro Nome', max_length=50, required=True, help_text= 'Campo de nome Obrigatório')
   last  ultimo_nome =forms.CharFiel( 'Ultimo Nome',max_length=50, required=True, help_text= 'Obrigatório')
    email = forms.EmailField ('E-mail' ,max_length=50, required=True, help_text= 'Por favor insira o email')

class Meta:
    models = User
    fields = ['Username', 'primeiro_nome', 'ultimo_name','email','password1','password2']