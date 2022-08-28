import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import pandas as pd
from tkinter import *
import os.path
from tkinter import messagebox as alert


ventana = Tk()
ventana.geometry("950x500")
ventana.title("DAJER SAPI")
ventana.config(bg = "white")

ruta_logo = os.path.abspath("./imagenes/R_verde.ico")
if not os.path.isfile(ruta_logo):
    ruta_logo =os.path.abspath("Desktop/python/TKINTER/imagenes/R_verde.ico")
#insertar icno oimagne logo en formato ico
ventana.iconbitmap(ruta_logo)

ruta = os.path.abspath('client.json')
if not os.path.isfile(ruta):
   ruta =os.path.abspath('Desktop\python\Tkinter/client.json')
print(ruta)
  



listado = StringVar()
dato = StringVar()
resultado = StringVar()  

#FUNCIONES 

def google_data():
     scope = ["https://spreadsheets.google.com/feeds"]
     creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
     client=gspread.authorize(creds)
     indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=2100685177")    
     fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1857978173")
     fileName =('BASE CLIENTES PR SAPI')
     sheet = client.open_by_url(indicadores).sheet1
     pp = pprint.PrettyPrinter()
     valores = sheet.get_all_values()     
          
     
     sheet.update_acell('A1',"CERATTI")
     dato =sheet.acell('A1').value
     status = "CONECTT whit GOOGLE SHEETS INDICADORES DAJER"
     print(status)
     #print(dato)
     #print("\n")
     #alert.showinfo("Alerta de coneccion","Acceso google") 
     df =pd.DataFrame(valores)
     #print(df)
     #print("\n")
     return df

#google_data("")


#FUNCION PARA LISTA COMPLEA DE CASOS VIGENTES
def google_lista ():
     scope = ["https://spreadsheets.google.com/feeds"]
     creds = ServiceAccountCredentials.from_json_keyfile_name(ruta, scope)
     client=gspread.authorize(creds)
     indicadores = ("https://docs.google.com/spreadsheets/d/1avUWBLkeKrc37wi24kiAzuXfRO9RCYEPO_m7MwMXT0E/edit#gid=2100685177")    
     fileActive = ("https://docs.google.com/spreadsheets/d/1qAsB6Dd2uyky2r2uMryxLasA6NHNyVoa5Z7_9XIlLYE/edit#gid=1857978173")
     fileName =('BASE CLIENTES PR SAPI')
     sheet = client.open_by_url(fileActive).sheet1
     pp = pprint.PrettyPrinter()
     valores = sheet.get_all_values()     
     #for valor in valores:
         #print(valor)     
     
     
     dato =sheet.acell('A1').value
     status = "CONECTT whit GOOGLE SHEETS LISTADO DAJER"
     print(status)
     #print(dato)
     #print("\n") 
     #alert.showinfo("Alerta de coneccion","Acceso google")
     df =pd.DataFrame(valores)
     print(df)
     #print("\n")
     return df

gr = google_data()  
lista = google_lista()

def get_dato():
     #r = gr
     #resultado.set(r)
     reporte.insert("insert" ,gr)
     

def actualizar():
   reporte.delete("1.0", END)
   google_data()  
   get_dato()   
     

def limpiar():
    reporte.delete('1.0',END)  
    reporte.insert("insert","CERATTI _TEC_SERVICES")  

def listar():
    
    reporte.insert("insert",lista)    



#VENTANA PARA MOSTAR DATOS 
#recibir = Entry(ventana,text = gr).grid()

#VARIBALES DE COLOR DE FONSO , FUENTE , TIPOGRAFIA
fondo = "#0000FF"
colorf = "white"
tipogrfia = "opensans"
titulo = Label(ventana,text = "CERATTI_TEC" ).grid(row = 0, column = 0,columnspan =3)

reporte = Text(ventana)
reporte.config( bg = fondo, state = "normal",fg= colorf, font= (tipogrfia,10), height= 25,width = 90)
reporte.grid(row = 1, column = 0 , columnspan = 4, padx = 30, pady = 10)

#BOTON PARA LLAMAR LA DATA A PANTALLA
Enviar_btn = Button(ventana,text = "Indicadores", command = get_dato)
Enviar_btn.grid(row =2, column = 1, pady=10 )
Enviar_btn.config(bg =fondo ,bd = 2, relief = "solid", fg = colorf , pady = 10 , width = 12)

#BOTON PARA ACTUALIZAR
Enviar_btn = Button(ventana,text = "Actualizar", command = actualizar)
Enviar_btn.grid(row =2, column = 0, pady=10 )
Enviar_btn.config(bg =fondo ,bd = 2, relief = "solid", fg = colorf, pady = 10 , width = 8)

#BOTON LISTADO DE CLIENTES
Enviar_btn = Button(ventana,text = "Listar", command = listar)
Enviar_btn.grid(row =2, column = 2, pady=10 )
Enviar_btn.config(bg =fondo ,bd = 2, relief = "solid", fg = colorf, pady = 10 , width = 8)


#BOTON PARA LIMPIAR LA PANTALLA
Limpiar_btn = Button(ventana,text = "Limpiar", command = limpiar)
Limpiar_btn.grid(row =2, column = 3, pady=10 )
Limpiar_btn.config(bg =fondo ,bd = 2, relief = "solid", fg = colorf, pady = 10, width = 8)





ventana.mainloop()
