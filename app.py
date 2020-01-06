from tkinter import *
from tkinter import messagebox
from subsidio.ventana_sub import ven_sub
from subsidio.lista_sub import listaSub
from vivienda.ventana_viv import ven_viv
from vivienda.lista_viv import listaViv
from modulo.ventana_mod import ven_mod
from modulo.lista_mod import listaMod
from pasaje.ventana_pas import ven_pas
from pasaje.lista_pas import listaPas
from tarjeta.lista_tarj import listaTarj
from farmacia.ventana_farm import ven_farm
from farmacia.lista_farm import listaFarm

#------------ configuracion de la raiz de la ventana---------------------------------
ventana_menu = Tk()
ventana_menu.title("Registro Social")
#raiz.resizable(0, 0)
ventana_menu.iconbitmap("img/final.ico")
ventana_menu.state("zoomed")#mazimizar ventana
ventana_menu.config(bg="white")
ventana_menu.config(cursor="hand2")

#------------------------introducimos una imagen y titulo----------------------------
miImagen = PhotoImage(file="img/muni.png")
label7 = Label(ventana_menu, image=miImagen, bg="white").place(x=30, y=540)
label8=Label(ventana_menu, text="MUNICIPALIDAD DE TINOGASTA", bg="white", font=("Bodoni MT Condensed", 55)).place(x=170, y=570)
label9=Label(ventana_menu, text="Sebastian Noblega Intendente", bg="white", font=("Monotype Corsiva", 12)).place(x=170, y=640)
imageEscritorio=PhotoImage(file="img/escritorio.png")
escritorio=Label(ventana_menu, image=imageEscritorio, bg="white").place(x=250, y=100)
# ---------------------------------funciones-----------------------------------------
def licencia():
    messagebox.showinfo("Registro Social", "Version 1.3 \n2018 all rights reserved. \nTapia W.")


def salir():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        ventana_menu.destroy()
#---------------VENTANA PASAJES-----------------------------------------
def nuevo_sub():
    ven_sub()
#---------------ABRIR DUBSIDIOS----------------------------------------
def lista_sub():
    listaSub()
#---------------ABRIR MODULO-------------------------------------------
def nuevo_viv():
    ven_viv()

#---------------ABRIR VIVINDA------------------------------------------
def lista_viv():
    listaViv()
#---------------ABRIR TARJETA SOCIAL-----------------------------------
def nuevo_mod():
    ven_mod()

def lista_mod():
    listaMod()

def nuevo_pas():
    ven_pas()

def lista_pas():
    listaPas()

def lista_tarj():
    listaTarj()

def nuevo_farm():
    ven_farm()

def lista_farm():
    listaFarm()


# configura el menu y submenu
barramenu = Menu(ventana_menu)
ventana_menu.config(menu=barramenu)
archivo = Menu(barramenu, tearoff=0,font=20,bg="#33D7FF")
archivo.add_command(label="Salir", command=salir)



subsidios = Menu(barramenu, tearoff=0, font=20)
subsidios.add_command(label="Ingresar Subsidio", command=nuevo_sub)
subsidios.add_separator()#separador de menu
subsidios.add_command(label="Listar y buscar", command=lista_sub)


materiales = Menu(barramenu, tearoff=0,  font=20)
materiales.add_command(label="Ingresar Pedido de Material", command=nuevo_viv)
materiales.add_separator()
materiales.add_command(labe="Listar y buscar",command=lista_viv)

tarjetaSocial = Menu(barramenu, tearoff=0, font=20)
tarjetaSocial.add_command(label="Listar y buscar", command=lista_tarj)

modulos = Menu(barramenu, tearoff=0, font=20)
modulos.add_command(label="Ingresar Modulos",command=nuevo_mod)
modulos.add_separator()
modulos.add_command(label="Listar y buscar",command=lista_mod)

pasajes = Menu(barramenu, tearoff=0, font=20)
pasajes.add_command(label="Ingresar Pasaje",command=nuevo_pas)
pasajes.add_separator()
pasajes.add_command(label="Listar y buscar", command=lista_pas)

farmacia = Menu(barramenu, tearoff=0, font=20)
farmacia.add_command(label="Ingresar Farmacia",command=nuevo_farm)
farmacia.add_separator()
farmacia.add_command(label="Listar y buscar", command=lista_farm)


ayuda = Menu(barramenu, tearoff=0, font=20,bg="#33D7FF")
ayuda.add_command(label="Acerca de...", command=licencia)
#-------------------------ingresar en menu-------------------------------
barramenu.add_cascade(label="Archivo", menu=archivo)

barramenu.add_cascade(label="Subsidios", menu=subsidios)

barramenu.add_cascade(label="Materiales", menu=materiales)

barramenu.add_cascade(label="Modulos", menu=modulos)

barramenu.add_cascade(label="Tarjeta Social", menu=tarjetaSocial)

barramenu.add_cascade(label="Pasajes", menu=pasajes)

barramenu.add_cascade(label="Farmacia", menu=farmacia)

barramenu.add_cascade(label="Ayuda", menu=ayuda)

ventana_menu.mainloop()


