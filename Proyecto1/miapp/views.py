from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd
import os.path
from django.core.paginator import Page, Paginator
import functools
from functools import reduce
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, FormArticulo,Pic_profile,postForm
from .models import Article,Profile,Post
from django.contrib import messages
from django.views.generic import CreateView, DeleteView,UpdateView,ListView
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.db.models import Q


"""
Vistas basadas en clases en lugar de funciones

"""

#vistas con clases para usarlos en los form hay q usar fields solo funciona si n usas un usaurio asignado
class CrearArticulo(CreateView):

    model = Post
    form_class = postForm
    template_name = 'post.html'
    success_url = reverse_lazy('articulos')



# Create your views here.
titulo = "CERATTI_TEC"

ruta = os.path.abspath('client.json')
if not os.path.isfile(ruta):
   ruta =os.path.abspath('../client.json')


@login_required(login_url='index')
def data(request):
     scope = ["https://spreadsheets.google.com/feeds"]
     creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
     client=gspread.authorize(creds)
     indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=426780618")    
     fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1857978173")
     fileName =('BASE CLIENTES PR SAPI')
     sheet = client.open_by_url(indicadores).sheet1
     pp = pprint.PrettyPrinter()
     valores = sheet.get_all_values() 

    #  valoresUnicos =map(lambda indi: valores[0], valores)

     

    
     #cabezera=sheet.col_values(1)
     #montos=sheet.col_values(2)
      
     
    #  sheet.update_acell('A1',"CERATTI")
    #  dato =sheet.acell('A1').value
     status = "CONECTT whit GOOGLE SHEETS INDICADORES DAJER"
     print(status)
     #print(dato)
     #print("\n")
     #alert.showinfo("Alerta de coneccion","Acceso google") 
     df =pd.DataFrame(valores)
     #print(df)
     #print("\n")
     return render(request, 'tabla.htm',{
         'resultado':valores,         
         'titulo': titulo,

     })


@login_required(login_url='index')
def lista (request):
     scope = ["https://spreadsheets.google.com/feeds"]
     creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
     client=gspread.authorize(creds)
     indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=2100685177")    
     fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1154589727")
     clientes =("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=1240240398")
     fileName =('BASE CLIENTES PR SAPI')
     sheet = client.open_by_url(fileActive).sheet1
     
     pp = pprint.PrettyPrinter()
     valores = sheet.get_all_values()     
     
     #indcadores= paythonglide fileactive=reportes hojagestion=python
    
     mayoresCero = list(filter(lambda mayor:int(mayor[5])>0, valores))
     total = reduce(lambda inicial,fila:int(fila[5])+inicial,mayoresCero,0)
     casos =len(mayoresCero)
     #nombres = list(map(lambda fila:fila[5],valores))

     #print(nombres)   
     
     dato =sheet.acell('A1').value
     status = "CONECTT whit GOOGLE SHEETS LISTADO DAJER"
     print(status)
     #print(dato)
     #print("\n") 
     #alert.showinfo("Alerta de coneccion","Acceso google")
     df =pd.DataFrame(valores)
    #  print(df)
     #print("\n")
     return render(request, 'vigentes.htm',{
         'vigentes':mayoresCero,
         'titulo': titulo,
         'todos': valores,
         'total': total,
         'casos': casos,
     })





def index(request):

    return render(request, 'index.htm',{
        'titulo': titulo
    })



def acceso(request):

    return render(request,'login.htm',{
         'titulo': titulo,
    })




  
@login_required(login_url='index')
def dashboard(request):
    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
    client=gspread.authorize(creds)
    indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=426780618")    
    fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1857978173")
    hojagestion =("https://docs.google.com/spreadsheets/d/1MpCu_rF7vWjoMHj08DBZhMYk-fi6MeMDeQJ2LZJhoMg/edit#gid=273768678")
    fileName =('BASE CLIENTES PR SAPI')
    #indcadores= paythonglide fileactive=reportes hojagestion=python
    sheet = client.open_by_url(hojagestion).sheet1
    shhet2 = client.open_by_url(indicadores).sheet1
    pp = pprint.PrettyPrinter()
    valores = sheet.get_all_values() 
    resultado = shhet2.get_all_values()

    year_nueve = valores[0]
    year_veinte = valores[1]
    year_veintiuno = valores[2]
    colocacion = valores[4][0]
    col = int(colocacion)
    num = format(col,",d")
    # print(num)
     #cabezera=sheet.col_values(1)
     #montos=sheet.col_values(2)
      
     
    #  sheet.update_acell('A1',"CERATTI")
    #  dato =sheet.acell('A1').value
    status = "CONECTT whit GOOGLE SHEETS INDICADORES DAJER"
    #print(year_nueve)
     #print(dato)
     #print("\n")
     #alert.showinfo("Alerta de coneccion","Acceso google") 
    df =pd.DataFrame(valores)
     #print(df)
     #print("\n")

    
    return render(request, 'dashboard.htm',{
       
        "indicadores": valores,
        "diezynueve": year_nueve,
        "dosmilviente": year_veinte,
        "dosmilveintiuno":year_veintiuno,
        "mesactual":resultado,
        "num":num,
        
    })       


#funcion para matrizar el dato de dashboard





"""def login(request):
    if request.method == 'POST':
        usuario = request.POST['email'] 
        password = request.POST['password']

        if usuario == 'robertoceratti@gmail.com' and password == '2702':

            return render(request,  'portada.htm',{
                'user':f"{usuario}",
                "mensaje": "S I C A SYSTEM ",

                
            })
        else:
            return render(request,  'index.htm',{
                'mensaje':f"Error en la captura, intenta de nuevo"
            })"""

def register(request):
    
    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data['username']   
            register_form.save()

            return redirect('index')
        else:
             messages.error(request,f'No fue posible crear un usuario')

    return render(request,'registro.htm',{
        'logo': 'CERATTI_TEC',
        'titulo': 'Registrate',
        'formulario': register_form
    })




def login_page(request):
    
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'portada.htm',{
                'mensaje': f'Hola bienvenido {user.username}'
            })
        else:

            return render(request,'login.htm',{
                'mensaje': 'No eres bienvenido , verfica tus claves de acceso'
            })


    return render(request,'index.htm',{
        'logo': 'CERATTI_TEC',
        'titulo': 'Accesa ',
    })




#FUNCION PARA SALIR DE LA SESION

def loginOut(request):
    logout(request)

    return redirect('index')



#FUCNION PARA METODOS REDUCE,MAP,FILTER
def opciones(request):
    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
    client=gspread.authorize(creds)
    indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=426780618")    
    fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1857978173")
    hojagestion =("https://docs.google.com/spreadsheets/d/1MpCu_rF7vWjoMHj08DBZhMYk-fi6MeMDeQJ2LZJhoMg/edit#gid=273768678")
    fileName =('BASE CLIENTES PR SAPI')
    #indcadores= paythonglide fileactive=reportes hojagestion=python
    sheet = client.open_by_url(fileActive).sheet1
    
    valores = sheet.get_all_values() 

    data = [
        ["roberto",5000,"2021"],
        ["lorena",10000,"2020"],
         ["pepe",5000,"2021"],
        ["erick",10000,"2020"]

    ]

    print (len(data))
    
    #reduce
    total = reduce(lambda inicial,fila:fila[1]+inicial,data,0)
    

    print(total)
    

    #modo mediabte for 
    for fila in data:
        if fila[1]>5000:
            print(fila)


    #encerrar en un list ya q devuelve un objeto FILTER
    mayores = list(filter(lambda mayor:mayor[1]>5000, data))
    #print(mayores) 

    mayoresCero = list(filter(lambda mayor:int(mayor[5])>0, valores))
    #print(mayoresCero)
    #print(len(mayoresCero))
   
    #FUNCION MAP    
    
    nombres = list(map(lambda fila:fila[0],data))

    #print(nombres)
   
    

    return render(request,'alta_casos.htm',{
        "data": data,
        "datos": valores,
        
    })            



@login_required(login_url='index')
def reportes(request):

    return render(request, 'reportes.htm',{
        "mensaje": "Estados Financieros",
    })



    

# FUNCION PARA SUBIR DATOS EIMAGENES MEDIANTE FORM CREAR ARTICULOS(OBJETOS)
@login_required(login_url='index')
def upload(request):
   
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
       
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')        
        files = request.FILES
        imagen = files.get('imagen')

        articulo= Article(
                titulo= titulo,
                contenido=contenido,
                imagen = imagen,                

            )
        articulo.user = current_user   
        articulo.save()
        return redirect('articulos')

       
    else:
         return render(request, 'articulos.htm',{
                'mensaje': "No se envio el formulario",
                
                
            }) 




@login_required(login_url='index')
def showArticulos(request):
    formulario = FormArticulo
    queryset = request.GET.get('buscar')    
    articulos = Article.objects.all()

    if queryset:
        articulos = Article.objects.filter(
        Q(titulo__contains =queryset)|
        Q(contenido__contains = queryset)
        ).distinct()
    
      
    return render(request, 'articulos.htm',{
        
        'articulos': articulos,
        'formulario': formulario,
    })




def elim_articulo(request,id):
    eliminado =Article.objects.get(pk=id)
    eliminado.delete()

    return redirect('articulos')



def actualizar(request):

    if request.method == "POST":
        titulo     = request.POST['titulo']        
        contenido  = request.POST['contenido']
        id = request.POST['id']
        actualizar = Article.objects.get(id =id)

    actualizar.titulo = titulo
    actualizar.contenido = contenido
    actualizar.save()
       
    return redirect('articulos')
    



#CODIGO PARA LA VISTA DEL ARTICULO 
@login_required(login_url='index')
def detalle(request,id):
    articulo = Article.objects.get(pk=id)
    

    return render(request, 'detalle.htm',{
        'articulo':articulo,

    })







"""
CODIGO PARA TODO LO DEL PERFIL DE USUARIOS ASI COMO SUS POSTS


"""

@login_required(login_url='index')
def perfil(request):
    user = request.user
    current_user = get_object_or_404(User,pk=request.user.id)
    #print(current_user.id)
    perfiles = Profile.objects.all()
    articulos = Article.objects.all()
    posts = user.publicacaciones.all()
    print(len(posts))

    form = Pic_profile()             
    return render(request,'perfil.htm',{
        'form': form,
        'perfiles':perfiles,
        'articulos':articulos,
        'posts':posts,
        'user': user,
       
    })        




#codigo para cambiar la imagen de perfil
@login_required(login_url='index')
def profile(request,id):
    
    instancia = Profile.objects.get(user_id=id)
    print(instancia)
    form = Pic_profile(instance=instancia)
    if request.method == 'POST':
        form = Pic_profile(request.POST,request.FILES,instance=instancia)
        if form.is_valid():
             instancia = form.save(commit=False)
             instancia.save()
             messages.success(request,'Tu imagen se ha modificado con exito !')
             return redirect('perfil')

        else:
            form =Pic_profile()
    form = Pic_profile()             
    return render(request,'perfil.htm',{
        'form': form,
        'usuario': instancia,
    })    



#FUNCION PARA PUBLICAR POST
@login_required(login_url='index')
def post(request):
    current_user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request,'Tu publicacion ya esta disponible!')
            return redirect('blog')
        else:
            messages.error(request,'Hubo un poblema con tu publicacion ::')
    form = postForm()        
    return render(request, 'social/post.html',{
            'form':form,
        })    



#PANTALLA PARA MOSTRAR LOS COLABORADORES TEAM-WORK
@login_required(login_url='index')
def feed(request):

    perfiles = Profile.objects.all()

    return render(request,'feed.htm',{
        'perfiles':perfiles,
    })