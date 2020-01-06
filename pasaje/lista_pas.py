from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def listaPas():
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
    #------------------------------------------------------------------
    #funcion actualizar lista
    def actualizarLista():
        x=lista.get_children()
        if x !="()":
            for i in x:
                lista.delete(i)
        miConexion = sqlite3.connect("pasajes.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM pasajes")
        elUsuario = miCursor.fetchall()
        for subsidios in elUsuario:
            lista.insert("", 0, text=subsidios[0],
                         values=(
                         str(subsidios[1]), str(subsidios[2]), str(subsidios[3]), str(subsidios[5]), str(subsidios[6]),
                         imagenLapiz))

    #fucion rellenar datos
    def buscaDatos():
        try:
            miConexion = sqlite3.connect("pasajes.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM pasajes WHERE dni=" + consulta.get())
            if len(consulta.get())>8 or len(consulta.get())<8:
                messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida \nDebes ingresar el DNI sin puntos")
                ventana.deiconify()
            elUsuario = miCursor.fetchall()
            x=lista.get_children()
            if x !="()":
                for i in x:
                    lista.delete(i)
            for subsidios in elUsuario:
                lista.insert("",0,text=subsidios[0],values=(str(subsidios[1]),str(subsidios[2]),str(subsidios[3]),str(subsidios[5]),str(subsidios[6])))
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
            root.geometry("230x230+1100+220")
            borra1=StringVar()
            borra2=StringVar()
            borra3=StringVar()
            #llamar datos
            miConexion = sqlite3.connect("pasajes.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM pasajes WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for subsidios in elUsuario:
                borra1.set(subsidios[3])
                borra2.set(subsidios[5])
                borra3.set(subsidios[6])
            miConexion.commit()
            #actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("pasajes.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE pasajes SET monto='" + borra1.get() +
                             "', destino='" + borra3.get() +
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

            etiqueta1 = Label(root, text="Monto en $")
            etiqueta1.place(x=10, y=40, width=200)
            entrada1 = Entry(root, justify="center", textvariable=borra1)
            entrada1.place(x=10, y=60, width=200)
            # -----------------------------------------------
            etiqueta3 = Label(root, text="Fecha")
            etiqueta3.place(x=10, y=80, width=200)
            entrada3 = Entry(root, justify="center",state=DISABLED ,textvariable=borra2)
            entrada3.place(x=10, y=100, width=200)
            # --------------------------------------------
            etiqueta4 = Label(root, text="Destino")
            etiqueta4.place(x=10, y=130, width=200)
            entrada4 = Entry(root, justify="center",textvariable=borra3)
            entrada4.place(x=10, y=150, width=200)
            # ---------------------------------------------
            imagenActaliza = PhotoImage(file="../img/actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)
            root.mainloop()


    def usuario():
        idSelecionado=lista.item(lista.selection())['text']
        if idSelecionado=="":
            messagebox.showwarning("Atencion", "Debes seleccionar un subsidio para editarlo")
            ventana.deiconify()
        else:
            root=Toplevel()
            root.geometry("250x170+1100+220")
            borra1=StringVar()
            borra2=StringVar()

            miConexion = sqlite3.connect("pasajes.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM pasajes WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for subsidios in elUsuario:
                borra1.set(subsidios[1])
                borra2.set(subsidios[2])

            miConexion.commit()
            etiqueta = Label(root, text="Nombre y Apellido")
            etiqueta.place(x=20, y=30, width=200)
            entrada = Entry(root, justify="center",textvariable=borra1)
            entrada.place(x=20, y=50, width=200)
            entrada.focus()

            # actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("pasajes.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE pasajes SET nombre_apellido='" + borra1.get() +
                                 "', dni='" + borra2.get() +
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

            imagenActaliza = PhotoImage(file="img/actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)

            root.mainloop()
    #------------------------------------------------------------------------------

    def vergastos():
        root = Toplevel()
        root.geometry("230x145+1100+220")
        data1 = StringVar()

        def contardatos():
            miConexion = sqlite3.connect("pasajes.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM pasajes")
            elUsuario = miCursor.fetchall()
            suma = 0
            for modulos in elUsuario:
                suma += int(modulos[3])
            suma1.config(text="{}".format("Gastos en pasajes: $" + str(suma)))
            miConexion.commit()

        #----
        etiqueta1=Label(root,text="Calcular gastos en pasajes").place(x=0,y=10)
        imagenBuscarf = PhotoImage(file="img/buscar.png")
        botoncontar = Button(root,image=imagenBuscar, command=contardatos)
        botoncontar.place(x=160, y=3)
        suma1 = Label(root, text="0", bg="white", font=25)
        suma1.place(x=20, y=45)

        root.mainloop()
    #-------------------------------------------------------------------------------
    buscar=Label(ventana,text="Busqueda por DNI").place(x=100,y=20)
    Ebuscar=Entry(ventana,width=20,justify="center",textvariable=consulta)
    Ebuscar.place(x=210,y=20)
    Ebuscar.focus()
    imagenBuscar=PhotoImage(file="img/buscar.png")
    Botonbuscar=Button(ventana,image=imagenBuscar,command=buscaDatos)
    Botonbuscar.place(x=340,y=15)
    #------------------------------------------------------------------
    calculador=PhotoImage(file="img/calculadora.png")
    botonCalc=Button(ventana,image=calculador,bg="white",command=vergastos)
    botonCalc.place(x=420,y=15)
    #------------------------------------------------------------------
    imagenActaliza=PhotoImage(file="img/actualiza.png")
    botonActualiza=Button(ventana,image=imagenActaliza,command=actualizarLista)
    botonActualiza.place(x=380,y=15)
    imagenLapiz=PhotoImage(file="img/editar.gif")
    botonEditar=Button(ventana,image=imagenLapiz,command=circuito)
    botonEditar.place(x=800,y=80)
    imagenUser=PhotoImage(file="img/usuario.png")
    botonUser=Button(ventana,image=imagenUser,bg="white",command=usuario)
    botonUser.place(x=840,y=80)
    lista=ttk.Treeview(ventana,columns=("A","B","C","D","E"),height=15)
    lista.place(x=10,y=80)
    lista.heading("#0",text="#")
    lista.column("#0",minwidth=0,width=50)
    lista.heading("A",text="User")
    lista.heading("B",text="DNI")
    lista.column("B",minwidth=0,width=130)
    lista.heading("C",text="Monto en $")
    lista.column("C",minwidth=0,width=100)
    lista.heading("D",text="Fecha")
    lista.column("D",minwidth=0,width=100)
    lista.heading("E",text="Destino")
    lista.column("E",minwidth=80)

    miConexion = sqlite3.connect("pasajes.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM pasajes")
    elUsuario = miCursor.fetchall()
    for subsidios in elUsuario:
        lista.insert("", 0, text=subsidios[0],
                     values=(str(subsidios[1]), str(subsidios[2]), str(subsidios[3]), str(subsidios[5]), str(subsidios[6]),imagenLapiz))


    #lista.insert("","0","#",text="#")
    ventana.mainloop()
