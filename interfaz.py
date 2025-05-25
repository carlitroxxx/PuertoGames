import tkinter as tk
from tkinter import ttk
from funciones import *


listado = listaJuegos()
#VENTANA
ventana = tk.Tk()
ventana.title("Videojuegos")
ventana.geometry("1000x750")
titulo = tk.Label(ventana, text="Catálogo", font=("Arial",16,"bold"))
titulo.pack(pady=10)
###########################################
#TREEVIEW PARA LISTAR VIDEOJUEGOS
tabla = ttk.Treeview(ventana, height=15,selectmode='browse')
tabla.pack()
tabla['columns'] = ('ID','TITULO','PLATAFORMAS','STOCK','PRECIO')
tabla.column("#0",width=0,stretch=tk.NO)
tabla.column("ID",anchor=tk.CENTER,width=50)
tabla.column("TITULO",width=400)
tabla.column("PLATAFORMAS",width=200)
tabla.column("STOCK",width=85)
tabla.column("PRECIO",width=105)
tabla.heading("ID",text="ID")
tabla.heading("TITULO",text="TITULO")
tabla.heading("PLATAFORMAS",text="PLATAFORMAS")
tabla.heading("STOCK",text="STOCK")
tabla.heading("PRECIO",text="PRECIO")
#FOR PARA INSERTAR DATOS
cargarTabla(tabla,listado)
###########################################
#Menu Botones
#
#Agregar
agregar_btn=tk.Button(ventana, text="Agregar Productos", width=15, pady=4, command=lambda:(agregarTK(ventana)))
agregar_btn.place(x=225,y=400)
#Editar
editar_btn=tk.Button(ventana, text="Editar Productos", width=15, pady=4)
editar_btn.place(x=350,y=400)
#Eliminar
eliminar_btn=tk.Button(ventana, text="Eliminar", width=15, pady=4, command=lambda:(eliminarJuego(tabla)))
eliminar_btn.place(x=475,y=400)
#Cerrar
cerrar_btn=tk.Button(ventana, text="Cerrar",width=15, pady=4, command=ventana.destroy)
cerrar_btn.place(x=600,y=400)
ventana.mainloop()