from django import forms
from .models import Contacto, Comic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Contacto
        fields = '__all__'

class ComicForm(forms.ModelForm):

    class Meta:
        model = Comic
        fields = '__all__'

        widgets = {
            "fecha_lanzamiento": forms.SelectDateWidget()
        }
class CustomUserCrationForm(UserCreationForm):
    pass
    