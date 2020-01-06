from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
def listaViv():
    #---------------------------------------------------------------------------------------
    ventana = Toplevel()
    #ventana.iconbitmap("final.ico")
    ventana.geometry("900x430+300+70")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    #variables
    consulta=StringVar()
    data1=StringVar()
    data2=StringVar()
    f1 = StringVar()
    f2 = StringVar()
    f3 = StringVar()
    f3.set(2019)
    f4 = StringVar()
    f5 = StringVar()
    f6 = StringVar()
    f6.set(2019)
    #------------------------------------------------------------------
    #funcion actualizar lista
    def actualizarLista():
        x=lista.get_children()
        if x !="()":
            for i in x:
                lista.delete(i)
        miConexion = sqlite3.connect("vivienda.db")
        miCursor = miConexion.cursor()
        miCursor.execute(
            "SELECT ID,nombre_apellido,dni,solicitud, strftime('%d-%m-%Y',fecha),social,alta FROM vivienda")
        elUsuario = miCursor.fetchall()
        for subsidios in elUsuario:
            lista.insert("", 0, text=subsidios[0],
                         values=(
                         str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[3]),
                         imagenLapiz))

    #fucion rellenar datos
    def buscaDatos():
        try:
            miConexion = sqlite3.connect("vivienda.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT ID,nombre_apellido,dni,solicitud, strftime('%d-%m-%Y',fecha),social,alta FROM vivienda WHERE dni=" + consulta.get())
            if len(consulta.get())>8 or len(consulta.get())<8:
                messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida \nDebes ingresar el DNI sin puntos")
                ventana.deiconify()
            elUsuario = miCursor.fetchall()
            x=lista.get_children()
            if x !="()":
                for i in x:
                    lista.delete(i)
            for subsidios in elUsuario:
                lista.insert("",0,text=subsidios[0],values=(str(subsidios[1]),str(subsidios[2]),str(subsidios[4]),str(subsidios[3])))
        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()
    def circuito():
        idSelecionado=lista.item(lista.selection())['text']
        if idSelecionado=="":
            messagebox.showwarning("Atencion", "Debes seleccionar un registro para editarlo")
            ventana.deiconify()
        else:
            root=Toplevel()
            root.geometry("230x275+1100+220")
            borra1=StringVar()
                #llamar datos
            miConexion = sqlite3.connect("vivienda.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM vivienda WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for vivienda in elUsuario:
                    borra1.set(vivienda[6])
            miConexion.commit()
            #actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("vivienda.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE vivienda SET alta='" + borra1.get() +
                                         "' WHERE ID=" + str(idSelecionado))
                miConexion.commit()
                root.destroy()
                opcion = messagebox.askquestion("Felicidades!",
                                            " Registro Modificado\n¿Deseas volver a editar?")
                if opcion == "yes":
                    root.destroy()
                    ventana.deiconify()
                    circuito()
                else:
                    root.destroy()
                    ventana.deiconify()
            etiqueta1 = Label(root, text="Reporte Social").place(x=10, y=40)
            label1 = Label(root, text=vivienda[5], fg="Green", font=25)
            label1.place(x=10, y=70)
            etiqueta2 = Label(root, text="Alta de ayuda").place(x=10, y=120)
            Radiobutton(root, text="SI", variable=borra1, value="SI").place(x=10, y=140)
            Radiobutton(root, text="NO", variable=borra1, value="NO").place(x=10, y=160)
            imagenActaliza = PhotoImage(file="actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)
            root.mainloop()


    def usuario():
        idSelecionado=lista.item(lista.selection())['text']
        if idSelecionado=="":
            messagebox.showwarning("Atencion", "Debes seleccionar un registro para editarlo")
            ventana.deiconify()
        else:
            root=Toplevel()
            root.geometry("250x280+1100+220")
            borra1=StringVar()
            borra2=StringVar()
            borra3=StringVar()
            borra4=StringVar()

            miConexion = sqlite3.connect("vivienda.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT ID,nombre_apellido,dni,solicitud, strftime('%d-%m-%Y',fecha),social,alta FROM vivienda WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for vivienda in elUsuario:
                borra1.set(vivienda[1])
                borra2.set(vivienda[2])
                borra3.set(vivienda[3])
                borra4.set(vivienda[4])

            miConexion.commit()
            etiqueta = Label(root, text="Nombre y Apellido")
            etiqueta.place(x=20, y=30, width=200)
            entrada = Entry(root, justify="center",textvariable=borra1)
            entrada.place(x=20, y=50, width=200)
            entrada.focus()

            # actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("vivienda.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE vivienda SET nombre_apellido='" + borra1.get() +
                                 "', dni='" + borra2.get() +
                                 "', solicitud='" + borra3.get() +
                                 "' WHERE ID=" + str(idSelecionado))
                miConexion.commit()
                root.destroy()
                opcion = messagebox.askquestion("Felicidades!",
                                                " Registro Modificado\n¿Deseas volver a editar?")
                if opcion == "yes":
                    root.destroy()
                    ventana.deiconify()
                    usuario()
                else:
                    root.destroy()
                    ventana.deiconify()
            # ------------------------------------------
            etiqueta2 = Label(root, text="D.N.I. (sin puntos)")
            etiqueta2.place(x=20, y=80, width=200)
            entrada2 = Entry(root, justify="center",textvariable=borra2)
            entrada2.place(x=20, y=100, width=200)
            # -------------------------------------------
            etiqueta5 = Label(root, text="Entrega")
            etiqueta5.place(x=20, y=130, width=200)
            entrada5 = Entry(root, justify="center",textvariable=borra3)
            entrada5.place(x=20, y=150, width=200)
            # --------------------------------------------
            etiqueta6 = Label(root, text="Fecha de entrega (dd/mm/aaaa)")
            etiqueta6.place(x=20, y=180)
            entrada6 = Entry(root, justify="center",textvariable=borra4,state=DISABLED)
            entrada6.place(x=20, y=200, width=200)
            # ---------------------------------------------
            imagenActaliza = PhotoImage(file="actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)

            root.mainloop()
    #buscar por rango de fechas
    def calcularMaterial():
        x = lista.get_children()
        if x != "()":
            for i in x:
                lista.delete(i)
        miConexion = sqlite3.connect("vivienda.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT ID,nombre_apellido,dni,solicitud, strftime('%d-%m-%Y',fecha),social,alta FROM vivienda WHERE fecha BETWEEN "+"'"+f3.get()+"-"+
                             f2.get()+"-"+
                             f1.get()+
                             "'"+
                             " AND " +
                             "'"+
                             f6.get()+"-"+
                             f5.get()+"-"+
                             f4.get()+
                             "'")
        elUsuario = miCursor.fetchall()
        for subsidios in elUsuario:
            lista.insert("", 0, text=subsidios[0],values=(str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[3])))
            miConexion.commit()
    buscarFecha = Label(ventana, text="Buscar entregas por rango de fechas").place(x=30, y=15)
    desde=Label(ventana,text="Desde").place(x=10,y=40)
    fecha1 = Entry(ventana, width=3, textvariable=f1)
    fecha1.place(x=50, y=40)
    barra1=Label(ventana,text="-").place(x=70,y=40)
    fecha2 = Entry(ventana, width=3, textvariable=f2)
    fecha2.place(x=80, y=40)
    barra2 = Label(ventana, text="-").place(x=100, y=40)
    fecha3 = Entry(ventana, width=5, textvariable=f3)
    fecha3.place(x=110, y=40)
        #------hasta
    hasta=Label(ventana,text="Hasta").place(x=10,y=60)
    fecha4 = Entry(ventana, width=3, textvariable=f4)
    fecha4.place(x=50, y=60)
    barra3=Label(ventana,text="-").place(x=70,y=60)
    fecha5 = Entry(ventana, width=3, textvariable=f5)
    fecha5.place(x=80, y=60)
    barra4 = Label(ventana, text="-").place(x=100, y=60)
    fecha6 = Entry(ventana, width=5, textvariable=f6)
    fecha6.place(x=110, y=60)
        #----
    imagenM = PhotoImage(file="buscar.png")
    botonMaterial = Button(ventana,image=imagenM, command=calcularMaterial)
    botonMaterial.place(x=160, y=40)

    #-------------------------------------------------------------------------------
    buscar=Label(ventana,text="Busqueda por DNI").place(x=480,y=20)
    Ebuscar=Entry(ventana,width=20,justify="center",textvariable=consulta)
    Ebuscar.place(x=590,y=20)
    Ebuscar.focus()
    imagenBuscar=PhotoImage(file="buscar.png")
    Botonbuscar=Button(ventana,image=imagenBuscar,command=buscaDatos)
    Botonbuscar.place(x=720,y=15)
    #------------------------------------------------------------------
    imagenActaliza=PhotoImage(file="actualiza.png")
    botonActualiza=Button(ventana,image=imagenActaliza,command=actualizarLista)
    botonActualiza.place(x=760,y=15)
    imagenLapiz=PhotoImage(file="editar.gif")
    botonEditar=Button(ventana,image=imagenLapiz,command=circuito)
    botonEditar.place(x=800,y=80)
    imagenUser=PhotoImage(file="usuario.png")
    botonUser=Button(ventana,image=imagenUser,bg="white",command=usuario)
    botonUser.place(x=840,y=80)
    lista=ttk.Treeview(ventana,columns=("A","B","C","D"),height=15)
    lista.place(x=10,y=80)
    lista.heading("#0",text="#")
    lista.column("#0",minwidth=0,width=50)
    lista.heading("A",text="User")
    lista.heading("B",text="DNI")
    lista.column("B",minwidth=0,width=130)
    lista.heading("C",text="Fecha")
    lista.column("C",minwidth=0,width=100)
    lista.heading("D",text="Entrega/Descripción")
    lista.column("D",width=300)

    miConexion = sqlite3.connect("vivienda.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT ID,nombre_apellido,dni,solicitud, strftime('%d-%m-%Y',fecha),social,alta FROM vivienda")
    elUsuario = miCursor.fetchall()
    for subsidios in elUsuario:
        lista.insert("", 0, text=subsidios[0],
                     values=(str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[3]),imagenLapiz))


    #lista.insert("","0","#",text="#")
    ventana.mainloop()
