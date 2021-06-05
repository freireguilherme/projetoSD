from Django import forms
from models import *

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        widgets = {
        'senha': forms.PasswordInput()
    }
