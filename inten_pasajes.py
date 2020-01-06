from tkinter import *
from tkinter import messagebox
import sqlite3



def pasaje():
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

    # ----------FUNCIONES DE SUBSIDIOS-----------------------------------------
    # funcion borrar
    def borrarcampo():
        borra1.set("")
        borra2.set("")
        borra3.set("")
        borra4.set("")
        borra5.set("")
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


    # ------------------VER GASTOS------------------------------------
    def vergastos():
        miConexion = sqlite3.connect("pasajes.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM pasajes")
        elUsuario = miCursor.fetchall()
        suma = 0
        for pasajes in elUsuario:
            suma += int(pasajes[4])
            gastosentrada.config(text="{}".format("$ "+str(suma)))
            miConexion.commit()

    # ----------------------ver tablas------------------------------------------------------------
    def verexpediente():

        try:
            lista.config(state="normal")
            lista.delete(1.0, END)
            lista.config(state="disable")
            miConexion = sqlite3.connect("pasajes.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM pasajes WHERE dni=" + borra10.get())
            elUsuario = miCursor.fetchall()
            for pasajes in elUsuario:
                lista.config(state="normal")
                lista.insert(1.0, pasajes[1] + "\n" +"Destino:"+ pasajes[7]+ "\n" +"Monto: "+str(pasajes[4])+ "\n" + "Fecha: " + str(
                    pasajes[6])+ "\n" +"Motivo: "+pasajes[5]+ "\n--------------------------------------------------" + "\n")
                lista.config(state="disable")
            miConexion.commit()

        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()
    #------------------------------------------------------------------------------
    def verid():
        miConexion = sqlite3.connect("pasajes.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM pasajes")
        elUsuario = miCursor.fetchall()
        for pasajes in elUsuario:
            entradaid.config(text="{}".format(str(pasajes[0])+"  Pasajes"))
        miConexion.commit()

    # -----------------TITULO--------------------------
    titulo_subsidio = Label(ventana, text="Registro de Pasajes", bg="white", font=("Bodoni MT Condensed", 25)).place(x=260, y=0)
    # -----------------BUSQUEDA POR DNI------------------------
    busqueda = Label(ventana, text="Busqueda por DNI", font=20, bg="white")
    busqueda.place(x=300, y=70)
    ebusqueda = Entry(ventana, justify="center", textvariable=borra10, font=20)
    ebusqueda.place(x=260, y=100, width=200)
    botonbusqueda = Button(ventana, text="BUSCAR", bg='white', command=verexpediente).place(x=270, y=150)
    botonborra = Button(ventana, text="BORRAR", bg='white', command=borrarlista).place(x=400, y=150)
    # -----------CUADRO DE BUSQUEDA--------------------------------------------
    lista = Text(ventana, width=50, height=12)
    lista.place(x=150, y=180)
    scrollvert = Scrollbar(ventana, command=lista.yview)
    scrollvert.place(x=555, y=180, height=200)
    lista.config(yscrollcommand=scrollvert.set, state="disable")

    # -----------------------SUMA DE MONTOS DE SUBSIDIOS---------------------------------
    gastos = Label(ventana, text="Gastos Anuales", font=20,bg="white").place(x=450, y=410)
    gastosentrada = Label(ventana,text="", font=("Arial", 15), justify="center", fg="red",bg="white")
    gastosentrada.place(x=480,y=430)
    gastasB = Button(ventana, text="CALCULAR", bg="red", command=vergastos, fg="white", font="Arial").place(x=460,
                                                                                                            y=460)
     # ------------------------GENERADOR DE ID--------------------
    etiquetaid = Label(ventana, text="Pasajes entregados", font=20, bg="white")
    etiquetaid.place(x=100, y=410, width=200)
    entradaid = Label(ventana,text="",justify="center", font=20,bg="white")
    entradaid.place(x=160, y=440)
    botonID = Button(ventana, text="CONTAR", bg="white",command=verid).place(x=170, y=470)




    ventana.mainloop()
