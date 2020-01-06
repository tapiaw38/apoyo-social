from tkinter import *
from tkinter import messagebox
import sqlite3



# --------------VENTANA SUBSIDIOS----------------------------------------
def tarjeta():
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
            miConexion = sqlite3.connect("tarjeta.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM tarjeta WHERE documento=" +"'"+ borra10.get()+"'")
            elUsuario = miCursor.fetchall()
            for tarjeta in elUsuario:
                estado1=str(tarjeta[10])
                if estado1==" ":
                    estado.config(text="{}".format("NO REALIZO EL REEMPADRONAMIENTO"))
                else:
                    estado.config(fg="green",text="{}".format("SI REALIZO EL REEMPADRONAMIENTO"))
                lista.config(state="normal")
                lista.insert(1.0, str(tarjeta[2]) + "\nFecha creación: " + tarjeta[
                    7] +
                    "\nDocumentación: "+(tarjeta[10])+"\n--------------------------------------------------" + "\n")
                lista.config(state="disable")
            miConexion.commit()

        except:
            messagebox.showwarning("ERROR", "Ingresaste una busqueda invalida")
            ventana.deiconify()





    #-----------------TITULO--------------------------
    titulo_subsidio=Label(ventana, text="Registro de Tarjetas", bg="white",font=("Bodoni MT Condensed",25)).place(x=260,y=0)

    #-----------------BUSQUEDA POR DNI------------------------
    busqueda = Label(ventana, text="Busqueda por DNI (con puntos)", font=12, bg="white")
    busqueda.place(x=250, y=70)
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
    #------------ESTADO-----------------------------------------
    estado = Label(ventana,text="",font=("Arial",15),justify="center",fg="red",bg="white")
    estado.place(x=170, y=430)



    ventana.mainloop()




#--------------------------------------------------------

