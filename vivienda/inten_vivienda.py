from tkinter import *
from tkinter import messagebox
import sqlite3



# --------------VENTANA SUBSIDIOS----------------------------------------
def vivienda():
    ventana = Toplevel()
    ventana.iconbitmap("final.ico")
    ventana.geometry("750x530+300+110")
    ventana.config(bg="white")
    ventana.resizable(0, 0)


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
    borra20= StringVar()
    borra21= StringVar()
    borra20.set(None)
    borra21.set(None)


    #--------borrar lista------------------------
    def borrarlista():
        borra10.set("")
        lista.config(state="normal")
        lista.delete(1.0, END)
        lista.config(state="disable")



    # ----------------------ver tablas------------------------------------------------------------
    def verexpediente():
        try:
            lista.config(state="normal")
            lista.delete(1.0, END)
            lista.config(state="disable")
            miConexion = sqlite3.connect("vivienda.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM vivienda WHERE dni=" + borra10.get())
            elUsuario = miCursor.fetchall()
            for vivienda in elUsuario:
                lista.config(state="normal")
                lista.insert(1.0,"Fecha: " + str(vivienda[4]) + "\n" + vivienda[
                    1] + "\n" + "Entrega: " + str(vivienda[3])+ "\nInforme Social: " + str(vivienda[5])+"\n--------------------------------------------------" + "\n")
                lista.config(state="disable")
            miConexion.commit()

        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()

    def verid():
        miConexion = sqlite3.connect("vivienda.db")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT * FROM vivienda")
        elUsuario = miCursor.fetchall()
        for subsidios in elUsuario:
            identrada.config(text="{}".format(str(subsidios[0])+"  Pedidos Entregados"))
        miConexion.commit()



    #-----------------TITULO--------------------------
    titulo_subsidio=Label(ventana, text="Registro de Materiales", bg="white",font=("Bodoni MT Condensed",25)).place(x=260,y=0)

    #-----------------BUSQUEDA POR DNI------------------------
    busqueda = Label(ventana, text="Busqueda por DNI", font=12, bg="white")
    busqueda.place(x=300, y=70)
    ebusqueda = Entry(ventana,justify="center",textvariable=borra10, font=12)
    ebusqueda.place(x=260, y=100, width=200)
    botonbusqueda= Button(ventana, text="BUSCAR", bg='white',command=verexpediente).place(x=270,y=150)
    botonborra = Button(ventana, text="BORRAR", bg='white',command=borrarlista).place(x=400, y=150)
    #-----------CUADRO DE BUSQUEDA--------------------------------------------
    lista = Text(ventana, width=50, height=12)
    lista.place(x=150, y=180)
    scrollvert = Scrollbar(ventana, command=lista.yview)
    scrollvert.place(x=555, y=180, height=200)
    lista.config(yscrollcommand=scrollvert.set, state="disable")


    #--------------------------CANTIDAD DE SUBSIDIOS-------------------------------------
    id=Label(ventana,text="Cantidad de Materiales entregados",font=20).place(x=230,y=400)
    identrada = Label(ventana,text="",font=("Arial",15),justify="center",fg="red",bg="white")
    identrada.place(x=250, y=430)
    idB=Button(ventana,text="CALCULAR",bg="red",fg="white",font="Arial",command=verid).place(x=310,y=470)



    ventana.mainloop()




#--------------------------------------------------------

