from tkinter import *
from tkinter import messagebox
import sqlite3



def modulo():
    #----------CONFIGURACION VENTANA-------------------------------
    ventana = Toplevel()
    ventana.iconbitmap("final.ico")
    ventana.geometry("750x530+300+110")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    #--------------------------------------------------
    # -----------------variables
    borra1 = StringVar()
    borra2 = StringVar()
    borra3 = StringVar()
    borra4 = StringVar()
    borra5 = StringVar()
    borra6 = StringVar()
    borra7 = StringVar()
    borra8 = StringVar()
    borra9 = StringVar()
    borra10 = StringVar()
    borra11 = StringVar()
    borra12 = StringVar()
    borra20 = StringVar()
    borra21 = StringVar()

    # ----------FUNCIONES DE SUBSIDIOS-----------------------------------------
    # funcion borrar
    def borrarcampo():
        borra1.set("")
        borra2.set("")
        borra3.set("")
        borra4.set("")
        borra6.set("")
        borra7.set("")
        borra8.set("")
        borra9.set("")
        borra12.set("")

    # --------borrar lista------------------------
    def borrarlista():
        borra10.set("")
        lista.config(state="normal")
        lista.delete(1.0, END)
        lista.config(state="disable")
    #----------borrar busqueda---------------------
    def borrarbusqueda():
        entrada9.config(text="")
        lista2.config(state="normal")
        lista2.delete(1.0, END)
        lista2.config(state="disable")

    # --------------------------------------------

    # ------------------VER GASTOS------------------------------------
    def vergastos():
        miConexion = sqlite3.connect("modulos.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM modulos")
        elUsuario = miCursor.fetchall()
        suma = 0
        for modulos in elUsuario:
            suma += int(modulos[3])
            gastosentrada.config(text="{}".format(str(suma)+" Modulos"))
            miConexion.commit()
    #--------------------POR LOCALIDAD---------------------------------
    def verlocalidad():
        entrada9.config(text="No se entregaron modulos")
        lista2.config(state="normal")
        lista2.delete(1.0, END)
        lista2.config(state="disable")
        miConexion = sqlite3.connect("modulos.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM modulos WHERE localidad="+ "'"+ borra20.get()+"'")
        elUsuario = miCursor.fetchall()
        suma = 0
        for modulos in elUsuario:
            suma += int(modulos[3])
            entrada9.config(text="{}".format("Se entregaron: "+str(suma)))
            lista2.config(state="normal")
            lista2.insert(1.0, modulos[1] + "\n" +"Cantidad:"+ str(modulos[3]) + "\n" + str(modulos[5])+ "\n" + "Fecha: " + str(
                    modulos[6])+ "\n----------------------")
            lista2.config(state="disable")

            miConexion.commit()

    # ----------------------ver tablas------------------------------------------------------------
    def verexpediente():

        try:
            lista.config(state="normal")
            lista.delete(1.0, END)
            lista.config(state="disable")
            miConexion = sqlite3.connect("modulos.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM modulos WHERE dni=" + borra10.get())
            elUsuario = miCursor.fetchall()
            for modulos in elUsuario:
                lista.config(state="normal")
                lista.insert(1.0, modulos[1] + "\n" +"Cantidad de modulos:"+ str(modulos[3])+"\nLocalidad: "+modulos[4] + "\n" +"Dirección: "+str(modulos[5])+ "\n" + "Fecha de entrega: " + str(
                    modulos[6])+ "\n------------------------------")
                lista.config(state="disable")
            miConexion.commit()

        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()
    #------------------------------------------------------------------------------

    # -----------------TITULO--------------------------
    titulo_subsidio = Label(ventana, text="Modulos Alimentarios", bg="white", font=("Bodoni MT Condensed", 25)).place(x=260, y=0)

    # -----------------BUSQUEDA POR DNI------------------------
    busqueda = Label(ventana, text="Busqueda por DNI", bg="white",font=20)
    busqueda.place(x=400, y=80, width=200)
    ebusqueda = Entry(ventana, justify="center", textvariable=borra10, font=20)
    ebusqueda.place(x=400, y=110, width=200)
    botonbusqueda = Button(ventana, text="BUSCAR", bg='white', command=verexpediente).place(x=430, y=150)
    botonborra = Button(ventana, text="BORRAR", bg='white', command=borrarlista).place(x=510, y=150)
    # -----------CUADRO DE BUSQUEDA--------------------------------------------
    lista = Text(ventana, width=30, height=20)
    lista.place(x=380, y=180)
    scrollvert = Scrollbar(ventana, command=lista.yview)
    scrollvert.place(x=620, y=180, height=320)
    lista.config(yscrollcommand=scrollvert.set, state="disable")
    #------------CONTAR POR LOCALIDAD--------------------------------------------
    etiqueta9=Label(ventana, text="Contar por localidad", font=20, bg="white")
    etiqueta9.place(x=100,y=80, width=200)
    combo2=Spinbox(ventana,textvariable=borra20,justify="center", font=15, values=(
    "Tinogasta","Anillaco","El Puesto","Villa San Roque","Santa Rosa","Costa de Reyes","Villa Lujan","La Puntilla",
    "Copacabana","Banda de Lucero","El Salado","El Pueblito"))
    combo2.place(x=100,y=120,width=200)
    entrada9=Label(ventana, justify="center", text="", font=15, fg="red", bg="white")
    entrada9.place(x=100,y=150)
     # -----------LISTA DEBAJO --------------------------------------------
    lista2 = Text(ventana, width=22, height=10)
    lista2.place(x=100, y=180)
    scrollvert2 = Scrollbar(ventana, command=lista2.yview)
    scrollvert2.place(x=285, y=180, height=170)
    lista2.config(yscrollcommand=scrollvert2.set, state="disable")
    botoncontar=Button(ventana, text="CONTAR", command=verlocalidad).place(x=130,y=360)
    botonborra2=Button(ventana, text="BORRAR", command=borrarbusqueda).place(x=200,y=360)
    # -----------------BOTONES------------------------

    # -----------------------SUMA DE MONTOS DE SUBSIDIOS---------------------------------
    gastos = Label(ventana, text="Modulos Entregados", font=20).place(x=120, y=420)
    gastosentrada = Label(ventana, font=("Arial", 15), justify="center", fg="red",bg="white")
    gastosentrada.place(x=135,y=450)
    gastasB = Button(ventana, text="CALCULAR", bg="red", command=vergastos, fg="white", font="Arial").place(x=140,y=490)




    ventana.mainloop()
