#Examen Final, Asignatura:Fundamentos de Programacion.
from tkinter import *
from tkinter import messagebox
Inventario={"Harina":{"Precio":300,"Cantidad":100},"Pan":{"Precio":50,"Cantidad":200},"Leche":{"Precio":150,"Cantidad":100},"Carne":{"Precio":500,"Cantidad":100},"Pollo":{"Precio":700,"Cantidad":100}}
Carrito={}
#Funciones:
def InventarioSuper():
  def Salir():
    Ventana.destroy()
  def VerInventario():
    for i in Inventario:
      etiqueta = Label(Ventana,text=i+":"+" Precio: "+str(Inventario[i]["Precio"])+"$"+" Cantidad: "+str(Inventario[i]["Cantidad"]),bg="orange").pack(anchor=NW)
  Ventana=Tk()
  Ventana.geometry("380x400+100+100")
  Ventana.title("Inventario Supermercado Friuli")
  Ventana.config(bg="orange")
  botonVI=Button(Ventana, text = "Ver Inventario", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2",command = VerInventario)
  botonVI.pack()
  botonVI.place(x=75,y=350)
  botonS=Button(Ventana, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=200,y=350)  
def AgregaralInventario():  
  def Agregar():    
    global Inventario
    TInventario={"Precio":0,"Cantidad":0}
    try:
      Producto=str(nombreEntrada.get())
      Cantidad=int(nombreEntrada2.get())
      Precio=int(nombreEntrada3.get())
      TInventario["Precio"]=Precio
      TInventario["Cantidad"]=Cantidad 
      Inventario.setdefault(Producto,TInventario) 
      Ventana1.destroy()
    except ValueError:
      Aviso.config(text="Debe ingresar algun dato")        
  Ventana1=Tk()
  Ventana1.geometry("380x200+100+100")
  Ventana1.title("Agregar al Inventario")
  Ventana1.config(bg="orange")
  Aviso = Label(Ventana1, text=" ",bg="orange")
  Aviso.pack()
  Aviso.place(x=120,y=150)
  etiqueta = Label(Ventana1, text="Nombre: ")
  etiqueta.pack()
  etiqueta.place(x=20,y=20)
  etiqueta1 = Label(Ventana1, text="Cantidad: ")
  etiqueta1.pack()
  etiqueta1.place(x=20,y=40)
  etiqueta2 = Label(Ventana1, text="Precio: ")
  etiqueta2.pack()
  etiqueta2.place(x=20,y=60)
  nombreEntrada=Entry(Ventana1)
  nombreEntrada.pack()
  nombreEntrada.place(x=120,y=20)
  nombreEntrada2=Entry(Ventana1)
  nombreEntrada2.pack()
  nombreEntrada2.place(x=120,y=40)
  nombreEntrada3=Entry(Ventana1)
  nombreEntrada3.pack()
  nombreEntrada3.place(x=120,y=60)
  botonI=Button(Ventana1, text = "Agregar", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2", command = Agregar)
  botonI.pack()
  botonI.place(x=150,y=100)  
def BuscarProducto():
  def Salir():
    Ventana2.destroy()
  def Buscar():
    Producto=str(nombreEntrada.get())
    if Inventario.get(Producto):      
      Aviso.config(text=Producto+":"+" Cantidad: "+str(Inventario[Producto]["Cantidad"])+" Precio: "+str(Inventario[Producto]["Precio"])+"$")
    else:      
      Aviso.config(text="Producto No Existe")
  Ventana2=Tk()
  Ventana2.geometry("380x150+100+100")
  Ventana2.title("Buscar Producto")
  Ventana2.config(bg="orange")
  Aviso=Label(Ventana2,text=" ",bg="orange")
  Aviso.pack()
  Aviso.place(x=80,y=60)
  etiqueta=Label(Ventana2,text="Nombre: ")
  etiqueta.pack()
  etiqueta.place(x=20,y=20)
  nombreEntrada=Entry(Ventana2)
  nombreEntrada.pack()
  nombreEntrada.place(x=100,y=20)
  botonB=Button(Ventana2, text = "Buscar", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2",command = Buscar)
  botonB.pack()
  botonB.place(x=70,y=100)
  botonS=Button(Ventana2, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=180,y=100)  
def AgregaralCarrito():
  def Salir():
    Ventana3.destroy()
  def Agregar():
    global TCarrito
    TCarrito={"Precio":0,"Cantidad":0}
    try:
      NProducto=str(nombreEntrada.get())
      NCantidad=int(nombreEntrada2.get())
      if (Inventario.get(NProducto) and ((Inventario[NProducto]["Cantidad"])>NCantidad)):
        Aviso.config(text="Hay disponibilidad")
        TCarrito["Cantidad"]=NCantidad
        TCarrito["Precio"]=Inventario[NProducto]["Precio"]
        Carrito.setdefault(NProducto,TCarrito)         
      else:
        Aviso.config(text="No hay disponibilidad o cantidad no disponible")
    except ValueError:
      messagebox.showwarning(message="Debe ingresar algun dato", title="Agregar al Carrito") 
      #Aviso1.config(text="Debe ingresar algun dato")
  Ventana3=Tk()
  Ventana3.geometry("380x150+100+100")
  Ventana3.title("Agregar al Carrito")
  Ventana3.config(bg="orange")
  Aviso = Label(Ventana3, text=" ",bg="orange")
  Aviso.pack()
  Aviso.place(x=20,y=60)
  #Aviso1 = Label(Ventana3, text=" ")
  #Aviso1.pack()
  #Aviso1.place(x=20,y=80)
  etiqueta = Label(Ventana3, text="Nombre: ")
  etiqueta.pack()
  etiqueta.place(x=20,y=20)
  etiqueta1 = Label(Ventana3, text="Cantidad: ")
  etiqueta1.pack()
  etiqueta1.place(x=20,y=40)
  nombreEntrada=Entry(Ventana3)
  nombreEntrada.pack()
  nombreEntrada.place(x=100,y=20)
  nombreEntrada2=Entry(Ventana3)
  nombreEntrada2.pack()
  nombreEntrada2.place(x=100,y=40)
  botonC=Button(Ventana3, text = "Agregar", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2", command = Agregar)
  botonC.pack()
  botonC.place(x=70,y=100)
  botonS=Button(Ventana3, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=180,y=100)
def EliminarProductodelCarrito():
  def Salir():
    Ventana4.destroy()
  def Eliminar():
    global Carrito
    NProducto=str(nombreEntrada.get())
    if Carrito.get(NProducto):
      del Carrito[NProducto]
      Aviso.config(text="Producto Eliminado")
    else:
      Aviso.config(text="El producto no esta en el carrito")
  Ventana4=Tk()
  Ventana4.geometry("380x150+100+100")
  Ventana4.title("Eliminar Productos del Carrito")
  Ventana4.config(bg="orange")
  Aviso=Label(Ventana4,text=" ",bg="orange")
  Aviso.pack()
  Aviso.place(x=80,y=50) 
  etiqueta = Label(Ventana4, text="Nombre: ")
  etiqueta.pack()
  etiqueta.place(x=20,y=20)
  nombreEntrada=Entry(Ventana4)
  nombreEntrada.pack()
  nombreEntrada.place(x=100,y=20)
  botonCL=Button(Ventana4, text = "Eliminar", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2", command = Eliminar)
  botonCL.pack()
  botonCL.place(x=70,y=100)
  botonS=Button(Ventana4, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=180,y=100)  
def VerCarrito():
  def Salir():
    Ventana5.destroy()
  def VerCarrito():    
    for i in Carrito:
      etiqueta = Label(Ventana5, text=i+":"+" Precio: "+str(Carrito[i]["Precio"])+"$"+" Cantidad: "+str(Carrito[i]["Cantidad"]),bg="orange").pack(anchor=NW)    
  Ventana5=Tk()
  Ventana5.geometry("380x300+100+100")
  Ventana5.title("Carrito de Compras")
  Ventana5.config(bg="orange")
  botonVC=Button(Ventana5, text = "Ver Carrito", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2",command = VerCarrito)
  botonVC.pack()
  botonVC.place(x=75,y=250)
  botonS=Button(Ventana5, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=200,y=250)  
def PagarCarrito():
  def VaciarCarrito():
    Carrito.clear()
  def Salir():
    Ventana6.destroy()
  def Pagar():
    Total=0
    global Carrito
    for PC in Carrito:
      for PI in Inventario:
        if PC==PI:
          Total=Total+(Carrito[PC]["Cantidad"]*Carrito[PC]["Precio"])
          Inventario[PI]["Cantidad"]=Inventario[PI]["Cantidad"]-Carrito[PC]["Cantidad"]  
    Carrito.clear()
    Aviso.config(text="Gastaste un total de: "+str(Total)+"$")
    Aviso1.config(text="Gracias por su compra, Vuelva Pronto")        
  Ventana6=Tk()
  Ventana6.geometry("380x150+100+100")
  Ventana6.title("Pagar Compra")
  Ventana6.config(bg="orange")
  Aviso=Label(Ventana6,text=" ",bg="orange")
  Aviso.pack()
  Aviso.place(x=115,y=20)
  Aviso1=Label(Ventana6,text=" ",bg="orange")
  Aviso1.pack()
  Aviso1.place(x=80,y=40)
  botonP=Button(Ventana6, text = "Pagar", fg = "black", width = 10, height = 2, bd = 0, bg = "green", cursor = "hand2", command = Pagar)
  botonP.pack()
  botonP.place(x=20,y=100)
  botonS=Button(Ventana6, text = "Salir", fg = "black", width = 10, height = 2, bd = 0, bg = "red", cursor = "hand2",command = Salir)
  botonS.pack()
  botonS.place(x=250,y=100)
  botonVC=Button(Ventana6, text = "Vaciar Carrito", fg = "black", width = 10, height = 2, bd = 0, bg = "yellow", cursor = "hand2",command = VaciarCarrito)
  botonVC.pack()
  botonVC.place(x=135,y=100) 
def GuardarySalir():
  Inv=open("Inventario.txt","w")
  for i in Inventario:
    Inv.write(str(i))
    Inv.write(" ")
    for j in Inventario[i]:
      Inv.write(str(Inventario[i][j]))
      Inv.write(" ")
    Inv.write("\n")
  Inv.close()
  raiz.destroy()
def LeerInventario():
  global Inventario
  Inventario={}
  Inv=open("Inventario.txt","r")
  Productos = Inv.readlines()
  Inv.close()
  for Prod in Productos:
    Separar=Prod.split()
    Inven=Separar[0]
    Inven1={"Precio":int(Separar[1]),"Cantidad":int(Separar[2])}
    Inventario.setdefault(Inven,Inven1)
  return Inventario
#Inventario:
LeerInventario()
#Ventana Principal:
raiz = Tk()
raiz.title("Supermercado Friuli")
raiz.geometry("420x570")
raiz.config(bg="black")
raiz.resizable(0,0)
#Imagen de Fondo:
imagen = PhotoImage(file="SMFondo.png")
logo_frame = Frame(raiz, width = 500, height = 100, bd = 0, bg="black")
logo_frame.pack(side = TOP)
Label(logo_frame, image=imagen).pack()
#Botones:
boton_frame = Frame(raiz, width = 500, height = 200, bd = 0, bg="black")
boton_frame.pack(side = TOP)
VerInventario=Button(boton_frame, text = "Ver Inventario", fg = "black", width =20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = InventarioSuper).grid(row = 2, column = 0, padx = 10, pady = 10)
AgregaralInventario=Button(boton_frame, text = "Agregar al Inventario", fg = "black", width = 20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = AgregaralInventario).grid(row = 2, column = 1, padx = 10, pady = 10)
BuscarProducto=Button(boton_frame, text = "Buscar Producto", fg = "black", width = 20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = BuscarProducto).grid(row = 3, column = 0, padx = 10, pady = 10)
AgregaralCarrito=Button(boton_frame, text = "Agregar al Carrito", fg = "black", width = 20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = AgregaralCarrito).grid(row = 3, column = 1, padx = 10, pady = 10)
EliminarProductosdelCarrito=Button(boton_frame, text = "Eliminar Productos del Carrito", fg = "black", width = 20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = EliminarProductodelCarrito).grid(row = 4, column = 0, padx = 10, pady = 10)
VerCarrito=Button(boton_frame, text = "Ver Carrito", fg = "black", width = 20, height = 1, bd = 3, bg = "#fff", cursor = "hand2", command = VerCarrito).grid(row = 4, column = 1, padx = 10, pady = 10)
PagarCarrito=Button(boton_frame, text = "Pagar Compra", fg = "black", width = 20, height = 1, bd = 3, bg = "yellow", cursor = "hand2", command = PagarCarrito).grid(row = 5, column = 0, padx = 10, pady = 10)
GuardarySalir=Button(boton_frame, text = "Guardar y Salir", fg = "black", width = 20, height = 1, bd = 3, bg = "red", cursor = "hand2", command = GuardarySalir).grid(row = 5, column =1 , padx = 10, pady = 10)
raiz.mainloop()