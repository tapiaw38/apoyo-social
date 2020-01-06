from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def listaFarm():
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
        miConexion = sqlite3.connect("farmacia.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT ID, nombre_apellido, dni, monto, strftime('%d-%m-%Y',fecha_solicitud) FROM farmacia")
        elUsuario = miCursor.fetchall()
        for farmacia in elUsuario:
            lista.insert("", 0, text=farmacia[0],
                         values=(
                             str(farmacia[1]), str(farmacia[2]), str(farmacia[3]), str(farmacia[4])))

    #fucion rellenar datos
    def buscaDatos():
        try:
            miConexion = sqlite3.connect("farmacia.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT ID, nombre_apellido, dni, monto, strftime('%d-%m-%Y',fecha_solicitud) FROM farmacia WHERE dni=" + consulta.get())
            if len(consulta.get())>8 or len(consulta.get())<8:
                messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida \nDebes ingresar el DNI sin puntos")
                ventana.deiconify()
            elUsuario = miCursor.fetchall()
            x=lista.get_children()
            if x !="()":
                for i in x:
                    lista.delete(i)
            for farmacia in elUsuario:
                lista.insert("", 0, text=farmacia[0], values=(str(farmacia[1]), str(farmacia[2]), str(farmacia[3]), str(farmacia[5]), str(farmacia[8])))
        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()

    def usuario():
        idSelecionado=lista.item(lista.selection())['text']
        if idSelecionado=="":
            messagebox.showwarning("Atencion", "Debes seleccionar un registro para editarlo")
            ventana.deiconify()
        else:
            root=Toplevel()
            root.geometry("250x330+1100+220")
            borra1=StringVar()
            borra2=StringVar()
            borra3=StringVar()
            borra4=StringVar()

            miConexion = sqlite3.connect("farmacia.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT ID, nombre_apellido, dni, monto, strftime('%d-%m-%Y',fecha_solicitud) FROM farmacia WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for subsidios in elUsuario:
                borra1.set(subsidios[1])
                borra2.set(subsidios[2])
                borra3.set(subsidios[3])
                borra4.set(subsidios[4])
            miConexion.commit()


            # actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("farmacia.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE farmacia SET nombre_apellido='" + borra1.get() +
                                 "', dni='" + borra2.get() +
                                 "', monto='" + borra3.get() +
                                 "', fecha_solicitud ='" + borra4.get() +
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
            etiqueta = Label(root, text="Nombre y Apellido")
            etiqueta.place(x=20, y=30, width=200)
            entrada = Entry(root, justify="center",textvariable=borra1)
            entrada.place(x=20, y=50, width=200)
            entrada.focus()
            # --------------------------------------------
            etiqueta2 = Label(root, text="D.N.I. (sin puntos)")
            etiqueta2.place(x=20, y=80, width=200)
            entrada2 = Entry(root, justify="center",textvariable=borra2)
            entrada2.place(x=20, y=100, width=200)
            # --------------------------------------------
            etiqueta4 = Label(root, text="Monto (sin puntos)")
            etiqueta4.place(x=20, y=130, width=200)
            entrada4 = Entry(root, justify="center",textvariable=borra3)
            entrada4.place(x=20, y=150, width=200)
            # --------------------------------------------
            etiqueta6 = Label(root, text="Fecha")
            etiqueta6.place(x=20, y=230,width=200)
            entrada6 = Entry(root, justify="center",textvariable=borra4,state=DISABLED)
            entrada6.place(x=20, y=250, width=200)
            # ---------------------------------------------
            imagenActaliza = PhotoImage(file="actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)
            #----------------------------------------------

            root.mainloop()
    #------------------------------------------------------------------------------

    def vergastos():
        root = Toplevel()
        root.geometry("230x275+1100+220")
        data1 = StringVar()
        data2 = StringVar()
        data3 = StringVar()
        data3.set(2019)
        data4 = StringVar()
        data5 =  StringVar()
        data6 = StringVar()
        data6.set(2019)
        miConexion = sqlite3.connect("farmacia.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM farmacia ORDER BY fecha_solicitud ASC")

        def contardatos():
            miConexion = sqlite3.connect("farmacia.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM farmacia WHERE fecha_solicitud BETWEEN "+"'"+data3.get()+"-"+
                             data2.get()+"-"+
                             data1.get()+
                             "'"+
                             " AND " +
                             "'"+
                             data6.get()+"-"+
                             data5.get()+"-"+
                             data4.get()+
                             "'")

            elUsuario = miCursor.fetchall()
            suma=0
            for farmacia in elUsuario :
                suma+=int(farmacia[3])
                suma1.config(text="{}".format("Los gastos son de $"+str(suma)))

            miConexion.commit()
        buscarFecha = Label(root, text="Calcular gastos por rango de fechas").place(x=5, y=0)
        suma1 = Label(root, text="0",bg="white", font=25)
        suma1.place(x=20, y=85)
        desde=Label(root,text="Desde").place(x=10,y=40)
        fecha1 = Entry(root, width=3, textvariable=data1)
        fecha1.place(x=50, y=40)
        barra1=Label(root,text="-").place(x=70,y=40)
        fecha2 = Entry(root, width=3, textvariable=data2)
        fecha2.place(x=80, y=40)
        barra2 = Label(root, text="-").place(x=100, y=40)
        fecha3 = Entry(root, width=5, textvariable=data3)
        fecha3.place(x=110, y=40)
        #------hasta
        hasta=Label(root,text="Hasta").place(x=10,y=60)
        fecha4 = Entry(root, width=3, textvariable=data4)
        fecha4.place(x=50, y=60)
        barra3=Label(root,text="-").place(x=70,y=60)
        fecha5 = Entry(root, width=3, textvariable=data5)
        fecha5.place(x=80, y=60)
        barra4 = Label(root, text="-").place(x=100, y=60)
        fecha6 = Entry(root, width=5, textvariable=data6)
        fecha6.place(x=110, y=60)
        #----
        imagenBuscarf = PhotoImage(file="buscar.png")
        botoncontar = Button(root,image=imagenBuscar, command=contardatos)
        botoncontar.place(x=160, y=40)

        root.mainloop()
    #-------------------------------------------------------------------------------
    buscar=Label(ventana,text="Busqueda por DNI").place(x=100,y=20)
    Ebuscar=Entry(ventana,width=20,justify="center",textvariable=consulta)
    Ebuscar.place(x=210,y=20)
    Ebuscar.focus()
    imagenBuscar=PhotoImage(file="buscar.png")
    Botonbuscar=Button(ventana,image=imagenBuscar,command=buscaDatos)
    Botonbuscar.place(x=340,y=15)
    #------------------------------------------------------------------
    calculador=PhotoImage(file="calculadora.png")
    botonCalc=Button(ventana,image=calculador,bg="white",command=vergastos)
    botonCalc.place(x=420,y=15)
    #------------------------------------------------------------------
    imagenActaliza=PhotoImage(file="actualiza.png")
    botonActualiza=Button(ventana,image=imagenActaliza,command=actualizarLista)
    botonActualiza.place(x=380,y=15)
    #------------------------------------------------------------------
    imagenUser=PhotoImage(file="usuario.png")
    botonUser=Button(ventana,image=imagenUser,bg="white",command=usuario)
    botonUser.place(x=670,y=80)
    #------------------------------------------------------------------
    lista=ttk.Treeview(ventana,columns=("A","B","C","D"),height=15)
    lista.place(x=10,y=80)
    lista.heading("#0",text="#")
    lista.column("#0",minwidth=0,width=50)
    lista.heading("A",text="User")
    lista.heading("B",text="DNI")
    lista.column("B",minwidth=0,width=130)
    lista.heading("C",text="Monto en $")
    lista.column("C",minwidth=0,width=130)
    lista.heading("D",text="Fecha")
    lista.column("D",minwidth=0,width=130)

    miConexion = sqlite3.connect("farmacia.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT ID, nombre_apellido, dni, monto, strftime('%d-%m-%Y',fecha_solicitud) FROM farmacia")
    elUsuario = miCursor.fetchall()
    for farmacia in elUsuario:
        lista.insert("", 0, text=farmacia[0],
                     values=(str(farmacia[1]), str(farmacia[2]), str(farmacia[3]), str(farmacia[4])))


    #lista.insert("","0","#",text="#")
    ventana.mainloop()
