from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import os




def listaTarj():
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
    #funcion convertir txt
    def conver_txt():
        miConexion = sqlite3.connect("tarjeta.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM tarjeta")
        elUsuario = miCursor.fetchall()
        file = open("tarjeta_tinogasta.txt", "w", encoding="utf-8")
        file.write("MUNICIPALIDAD DE TINOGASTA \nREEMPADRONAMIENTO DE TARJETA SOCIAL\n")
        for tarjeta in elUsuario:
            file.write(str(tarjeta[0])+"  "+str(tarjeta[1])+"  "+str(tarjeta[2])+"  "+str(tarjeta[3])+"  "+str(tarjeta[4])+"  "+str(tarjeta[5])+"  "+str(tarjeta[6])+"  "+str(tarjeta[7])+"  "+str(tarjeta[8])+"  "+str(tarjeta[9])+"  "+str(tarjeta[10])+"\n")
        file.close()
        os.system("tarjeta_tinogasta.txt")
    
    #------------------------------------------------------------------
    #funcion actualizar lista
    def actualizarLista():
        x=lista.get_children()
        if x !="()":
            for i in x:
                lista.delete(i)
        miConexion = sqlite3.connect("tarjeta.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM tarjeta")
        elUsuario = miCursor.fetchall()
        for subsidios in elUsuario:
            lista.insert("", 0, text=subsidios[0],
                         values=(
                         str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[7]), str(subsidios[10])))


    #fucion rellenar datos
    def buscaDatos():
        try:
            miConexion = sqlite3.connect("tarjeta.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM tarjeta WHERE documento=" +"'"+consulta.get()+"'")
            if len(consulta.get())>10 or len(consulta.get())<10:
                messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida \nDebes ingresar el DNI con puntos")
                ventana.deiconify()
            elUsuario = miCursor.fetchall()
            x=lista.get_children()
            if x !="()":
                for i in x:
                    lista.delete(i)
            for subsidios in elUsuario:
                lista.insert("", 0, text=subsidios[0],
                             values=(str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[7]),
                                     str(subsidios[10])))
        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()

    def usuario():
        idSelecionado=lista.item(lista.selection())['text']
        if idSelecionado=="":
            messagebox.showwarning("Atencion", "Debes seleccionar un usuario para editarlo")
            ventana.deiconify()
        else:
            root=Toplevel()
            root.geometry("250x330+1100+220")
            borra1=StringVar()
            borra2=StringVar()
            borra3=StringVar()
            borra4=StringVar()
            borra5=StringVar()

            miConexion = sqlite3.connect("tarjeta.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM tarjeta WHERE ID=" + str(idSelecionado))
            elUsuario = miCursor.fetchall()
            for subsidios in elUsuario:
                borra1.set(subsidios[1])
                borra2.set(subsidios[2])
                borra3.set(subsidios[4])
                borra4.set(subsidios[10])
                borra5.set(subsidios[7])
            miConexion.commit()
            etiqueta = Label(root, text="Apellido")
            etiqueta.place(x=20, y=30, width=200)
            entrada = Entry(root, justify="center",textvariable=borra1)
            entrada.place(x=20, y=50, width=200)

            # actualizar datos
            def actualiza():
                miConexion = sqlite3.connect("tarjeta.db")
                miCursor = miConexion.cursor()
                miCursor.execute("UPDATE tarjeta SET documentacion='" + borra4.get() +
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
            etiqueta2 = Label(root, text="Nombre")
            etiqueta2.place(x=20, y=80, width=200)
            entrada2 = Entry(root, justify="center",textvariable=borra2)
            entrada2.place(x=20, y=100, width=200)
            # --------------------------------------------
            etiqueta4 = Label(root, text="D.N.I.")
            etiqueta4.place(x=20, y=130, width=200)
            entrada4 = Entry(root, justify="center",textvariable=borra3)
            entrada4.place(x=20, y=150, width=200)
            # --------------------------------------------
            etiqueta5 = Label(root, text="Documentación")
            etiqueta5.place(x=20, y=180, width=200)
            entrada5 = Entry(root, justify="center",textvariable=borra4)
            entrada5.place(x=20, y=200, width=200)
            entrada5.focus()
            entrada5.icursor(END)
            entrada5.select_range(0,END)
            # --------------------------------------------
            etiqueta6 = Label(root, text="Fecha de creación")
            etiqueta6.place(x=20, y=230,width=200)
            entrada6 = Entry(root, justify="center",textvariable=borra5,state=DISABLED)
            entrada6.place(x=20, y=250, width=200)
            # ---------------------------------------------
            imagenActaliza = PhotoImage(file="img/actualiza.png")
            botonActualiza = Button(root,image=imagenActaliza, command=actualiza)
            botonActualiza.place(x=0, y=0)

            root.mainloop()
    #------------------------------------------------------------------------------


    #-------------------------------------------------------------------------------
    buscar=Label(ventana,text="Busqueda por DNI").place(x=100,y=20)
    Ebuscar=Entry(ventana,width=20,justify="center",textvariable=consulta)
    Ebuscar.place(x=210,y=20)
    Ebuscar.focus()
    imagenBuscar=PhotoImage(file="img/buscar.png")
    Botonbuscar=Button(ventana,image=imagenBuscar,command=buscaDatos)
    Botonbuscar.place(x=340,y=15)
    #------------------------------------------------------------------
    imagenActaliza=PhotoImage(file="img/actualiza.png")
    botonActualiza=Button(ventana,image=imagenActaliza,command=actualizarLista)
    botonActualiza.place(x=380,y=15)
    imagenLapiz=PhotoImage(file="img/editar.gif")
    imagenUser=PhotoImage(file="img/usuario.png")
    botonUser=Button(ventana,image=imagenUser,bg="white",command=usuario)
    botonUser.place(x=420,y=15)
    imagenimpri=PhotoImage(file="img/imprimir.gif")
    botonImprim = Button(ventana, image=imagenimpri, bg="white", command=conver_txt)
    botonImprim.place(x=770, y=80)
    lista=ttk.Treeview(ventana,columns=("A","B","C","D","E"),height=15)
    lista.place(x=10,y=80)
    lista.heading("#0",text="ID")
    lista.column("#0",minwidth=0,width=80)
    lista.heading("A",text="Apellido")
    lista.column("A", minwidth=0, width=100)
    lista.heading("B",text="Nombre")
    lista.column("B",minwidth=0,width=180)
    lista.heading("C",text="DNI")
    lista.column("C",minwidth=0,width=100)
    lista.heading("D",text="Fecha")
    lista.column("D",minwidth=0,width=100)
    lista.heading("E",text="Documentación")
    lista.column("E",minwidth=0, width=180)

    miConexion = sqlite3.connect("tarjeta.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM tarjeta")
    elUsuario = miCursor.fetchall()
    for subsidios in elUsuario:
        lista.insert("", 0, text=subsidios[0],
                     values=(str(subsidios[1]), str(subsidios[2]), str(subsidios[4]), str(subsidios[7]), str(subsidios[10])))


    #lista.insert("","0","#",text="#")
    ventana.mainloop()
