from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save


# Create your models here.

class Article(models.Model):
    titulo = models.CharField(max_length=150, verbose_name ='Titulo')
    contenido  = models.TextField() 
    imagen = models.ImageField(default='null', verbose_name='Pic',upload_to = 'articulos/')
    
    user = models.ForeignKey(User,editable=False, verbose_name='Usuario', on_delete=models.CASCADE,related_name='publicacaciones')
    
    createdo_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')
    atualizado_el = models.DateTimeField(auto_now=True, verbose_name='Actualizado el :')

    
    class Meta:
            verbose_name='Articulo'
            verbose_name_plural='Articulos'
            ordering= ['-createdo_el']

    def __str__(self):
        return self.titulo


#CLASE PARA CREAR UN PERFIL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='usuario')
    img = models.ImageField(default='LOGO.png', verbose_name='foto')
    position = models.CharField(max_length=20,verbose_name='Cargo',default='Ceo')

    def __str__(self):
        return f'Perfil de {self.user.username}' 


class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE ,verbose_name='posts',related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(verbose_name='contenido',max_length=200)

    class Meta:
        ordering =['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'    



#FUNCION USANDO SIGNALS PARA QUE SE EJECUTE UNA FUNCION UNA VEZ SE FUARDE UN MODELO 
"""def created_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(created_profile,sender=User)"""