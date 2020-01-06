from tkinter import *


def alerta():
    ventana = Toplevel()
    ventana.iconbitmap("final.ico")
    ventana.geometry("750x650+300+30")
    ventana.config(bg="white")
    ventana.resizable(0, 0)


    alerta = Label(ventana, text="Se dejo de dar mantenimiento a esta aplicación \nPor favor póngase en contacto con el administrador", bg="red", fg="white", font=("Bodoni MT Condensed", 33))
    alerta.place(x=50, y=50)


    imagen = PhotoImage(file="alert.png")
    img = Label(ventana, image=imagen, bg="white")
    img.place(x=150,y=200)



    ventana.mainloop()
