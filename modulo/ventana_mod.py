from tkinter import *
from tkinter import messagebox
import sqlite3

def ven_mod():
    ventana=Toplevel()
    ventana.geometry("250x500+50+70")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    #variables
    borra1=StringVar()
    borra2=StringVar()
    borra3=StringVar()
    borra4=StringVar()
    borra5=StringVar()
    data1 = StringVar()
    data2 = StringVar()
    data3 = StringVar()
    #funcion actualiza
    def guardaDatos():
        miConexion = sqlite3.connect("modulos.db")
        miCursor = miConexion.cursor()
        if borra1.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
            ventana.deiconify()
        elif borra2.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
            ventana.deiconify()
        elif len(borra2.get())>8 or len(borra2.get())<8:
            messagebox.showerror("ERROR", "Debes ingresar un DNI sin puntos \nDebe tener 8 caracteres")
            ventana.deiconify()
        elif borra3.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
            ventana.deiconify()
        elif borra4.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
            ventana.deiconify()
        elif borra5.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
            ventana.deiconify()
        else:
            miCursor.execute("INSERT INTO modulos VALUES(NULL, '" + borra1.get() +
                             "','" + borra2.get() +
                             "','" + borra3.get() +
                             "','" + borra4.get() +
                             "','" + borra5.get() +
                             "','" + data3.get() + "-" + data2.get() + "-" + data1.get() +
                             "')")
            miConexion.commit()
            opcion = messagebox.askquestion("Felicidades!", " Registro Guardado\n¿Deseas ingresar uno nuevo?")
            if opcion == "yes":
                ventana.destroy()
                ven_mod()
            else:
                ventana.destroy()
    # ------------------------------------------
    #Borrar datos
    def borraD():
        borra1.set("")
        borra2.set("")
        borra3.set("")
        borra4.set("")
        borra5.set("")
        data1.set("")
        data2.set("")
        data3.set("")
    #-------------------------------------------------

    # -----------------TITULO--------------------------
    titulo_etiquetas = Label(ventana, text="Ingresá nuevo registro", bg="white", font=("Bodoni MT Condensed", 15)).place(
        x=50, y=0)
    #-----------------------------------------
    etiqueta8 = Label(ventana, text="Trámite N°:", bg="green", fg="white")
    etiqueta8.place(x=20, y=40, width=200)
    idLabel = Label(ventana,justify="center",text="0",font=15)
    idLabel.place(x=90, y=70, width=50)
    #-----------------------------------------
    #leer ID
    miConexion = sqlite3.connect("modulos.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM modulos")
    elUsuario = miCursor.fetchall()
    for subsidios in elUsuario:
        idLabel.config(text="{}".format(str(subsidios[0] + 1)))
    miConexion.commit()
    #-----------------------------------------
    etiqueta = Label(ventana, text="Nombre y Apellido")
    etiqueta.place(x=20, y=110, width=200)
    entrada = Entry(ventana, justify="center",textvariable=borra1)
    entrada.place(x=20, y=130, width=200)
    entrada.focus()
    # ------------------------------------------
    etiqueta2 = Label(ventana, text="D.N.I. (sin puntos)")
    etiqueta2.place(x=20, y=160, width=200)
    entrada2 = Entry(ventana, justify="center",textvariable=borra2)
    entrada2.place(x=20, y=180, width=200)
    # -------------------------------------------
    etiqueta3 = Label(ventana, text="Cantidad de modulos")
    etiqueta3.place(x=20, y=210, width=200)
    entrada3 = Entry(ventana, justify="center",textvariable=borra3)
    entrada3.place(x=20, y=230, width=200)
    # --------------------------------------------
    etiqueta6 = Label(ventana, text="Localidad")
    etiqueta6.place(x=20, y=260, width=200)
    combo = Spinbox(ventana, justify="center",textvariable=borra4 ,values=(
        "Tinogasta", "Anillaco", "El Puesto", "Villa San Roque", "Santa Rosa", "Costa de Reyes", "Villa Lujan",
        "La Puntilla",
        "Copacabana", "Banda de Lucero", "El Salado", "El Pueblito"))
    combo.place(x=20, y=280, width=200)
    # --------------------------------------------
    etiqueta5 = Label(ventana, text="Dirección")
    etiqueta5.place(x=20, y=310, width=200)
    entrada5 = Entry(ventana, justify="center",textvariable=borra5)
    entrada5.place(x=20, y=330, width=200)
    # --------------------------------------------
    etiqueta6 = Label(ventana, text="Fecha de entrega (dd/mm/aaaa)")
    etiqueta6.place(x=20, y=360, width=200)
    fecha1 = Entry(ventana, width=3, textvariable=data1)
    fecha1.place(x=70, y=390)
    barra1 = Label(ventana, text="-").place(x=90, y=390)
    fecha2 = Entry(ventana, width=3, textvariable=data2)
    fecha2.place(x=100, y=390)
    barra2 = Label(ventana, text="-").place(x=120, y=390)
    fecha3 = Entry(ventana, width=5, textvariable=data3)
    fecha3.place(x=130, y=390)
    # --------------------------------------------
    imagen1=PhotoImage(file="img/guardar.png")
    botonguarda = Button(ventana, image=imagen1,command=guardaDatos)
    botonguarda.place(x=40, y=430)
    imagen2=PhotoImage(file="img/borrar.png")
    botonborrar = Button(ventana, image=imagen2, bg='white',command=borraD)
    botonborrar.place(x=140, y=430)


    ventana.mainloop()
