from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Profile



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username','email', 'first_name', 'last_name', 'password1','password2'
        ]


#formulario para postear
class postForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Que estas pensando ?'}),required=True)        

    class Meta:
        model=Post
        fields = ['content']


#formulario para cambiar imgane de el perfil
class Pic_profile(forms.ModelForm):
    img = forms.ImageField(label="Cambiar imagen de perfil")

    class Meta:
           model=Profile
           fields = ['img']




#formulario para publicar noticias desde el admin para la comunidad
class FormArticulo(forms.Form):
    
    titulo = forms.CharField(
        label ="Titulo",
        max_length=30,
         required=True
        
     )
    contenido = forms.TimeField(label="Articulo",required=True,widget=forms.Textarea(attrs={'rows':4,'cols':50}))
    imagen = forms.ImageField(label="Subir imagen")
    
    #input select
   
    """
     validators = [
             validators.MinLengthValidator(5,'capturaste mas de 20 '),
             validators.RegexValidator('^[A-Za-z0-9]*$', 'los caracreters capturados no son validos')
         ]
    
    
    
    """