from tkinter import *
from pasaje.inten_pasajes import pasaje
from subsidio.inten_subsidio import subsidio
from modulo.inten_modulo import modulo
from vivienda.inten_vivienda import vivienda
from tarjeta.inten_tarjeta import tarjeta

def abrir_sub():
    subsidio()
def abrir_pas():
    pasaje()
def abrir_mod():
    modulo()
def abrir_viv():
    vivienda()
def abrir_tarj():
    tarjeta()



#------------ configuracion de la raiz de la ventana---------------------------------
raiz = Tk()
raiz.title("Tinogasta Municipio")
#raiz.resizable(0, 0)
raiz.iconbitmap("final.ico")
raiz.state("zoomed")#mazimizar ventana
raiz.config(bg="white")
raiz.config(cursor="hand2")

#------------------------introducimos una imagen y titulo----------------------------
miImagen = PhotoImage(file="img/logo5.png")
label = Label(raiz, image=miImagen, bg="white").place(x=400, y=200)
labe2=Label(raiz,text="¡Bienvenido Intendente!", bg="white",font=("Bodoni MT Condensed",55)).place(x=460,y=0)
labe4=Label(raiz,text="Elije una opción para conocer los beneficiarios de los servicios otorgados por el Municipio", bg="white",font=("Bodoni MT Condensed",30)).place(x=100,y=100)
labe3=Label(raiz,text="David Sebastian Noblega Intendente", bg="white",font=("Monotype Corsiva",12)).place(x=1100,y=650)
#-------------------------BOTONES DE CONSULTAS---------------------------------------
label5=Label(raiz,text="Subsidios", bg="white",font=(12)).place(x=120,y=170)
imagen1 = PhotoImage(file="img/sub.png")
boton_subsidio = Button(raiz, image=imagen1, command=abrir_sub)
boton_subsidio.place(x=100, y=200)

label6=Label(raiz,text="Pasajes", bg="white",font=(12)).place(x=325,y=170)
imagen2 = PhotoImage(file="img/pasaje.png")
boton_pasaje = Button(raiz, image=imagen2, command=abrir_pas)
boton_pasaje.place(x=300, y=200)

label5=Label(raiz,text="Modulos", bg="white",font=(12)).place(x=525,y=170)
imagen3 = PhotoImage(file="img/modulo.png")
boton_pasaje = Button(raiz, image=imagen3,command=abrir_mod)
boton_pasaje.place(x=500, y=200)

label7=Label(raiz,text="Materiales", bg="white",font=(12)).place(x=725,y=170)
imagen4 = PhotoImage(file="img/vivienda.png")
boton_vivienda = Button(raiz, image=imagen4,command=abrir_viv)
boton_vivienda.place(x=700, y=200)

label8=Label(raiz,text="Tarjeta Social", bg="white",font=(12)).place(x=905,y=170)
imagen5 = PhotoImage(file="img/tarjeta.png")
boton_tarjeta = Button(raiz, image=imagen5,command=abrir_tarj)
boton_tarjeta.place(x=900, y=200)



raiz.mainloop()
