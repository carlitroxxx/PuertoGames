import pyodbc
import tkinter as tk
from tkinter import messagebox
#'SERVER=W608-PCX\SQLEXPRESS;'
def listaJuegos():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=CARLOS\\SQLEXPRESS;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT v.id_videojuego, v.titulo, v.precio, v.stock, p.nombre
        FROM Videojuegos v
        inner join Plataformas p on (v.id_plataforma = p.id_plataforma)
        """)
    lista = cursor.fetchall()
    conn.close()
    return lista

def cargarTabla(tabla,listado):
    for item in tabla.get_children():
        tabla.delete(item)
    for juego in listado:
        id_videojuego,titulo, precio, stock,nombre = juego
        tabla.insert(parent='', index='end', iid=id_videojuego, text='', values=(id_videojuego,titulo,nombre,stock,precio))

def eliminar(tabla):
    try:
        id = tabla.focus()
        if not id:
            messagebox.showwarning("Atención","No se ha seleccionado ningun videojuego.")
            return
        conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=CARLOS\\SQLEXPRESS;'
                'DATABASE=PuertoGames2025;'
                'Trusted_Connection=yes;'
            )
        confirmacion = messagebox.askyesno("CUIDADO",f"¿Desea ELIMINAR el videojuego ID: {id}?")
        if confirmacion:    
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Videojuegos WHERE id_videojuego = ?", (int(id,)))
            conn.commit()
            print(f"ID eliminado:{id}")
    except ValueError:
        print("Error!")
    except Exception as e:
        print(e)
    finally:
        conn.close()
        
def eliminarJuego(tabla):
    eliminar(tabla)
    listado = listaJuegos()
    cargarTabla(tabla,listado)
    
def agregarTK(ventana):
    formulario_frame = tk.LabelFrame(ventana, text="Agregar Videojuego", padx=10, pady=10)
    formulario_frame.place(x=300,y=475,width=375, height=175)
    #titulo
    tk.Label(formulario_frame, text="Titulo").place(x=0, y=0)
    titulo_entry= tk.Entry(formulario_frame, width=45)
    titulo_entry.place(y=0,x=70)
    #plataforma
    tk.Label(formulario_frame, text="Plataforma").place(x=0,y=25)
    plataforma_entry=tk.Entry(formulario_frame, width=45)
    plataforma_entry.place(y=25, x=70)
    #stock
    tk.Label(formulario_frame, text="Stock").place(x=0, y=50)
    stock_entry=tk.Entry(formulario_frame, width=10)
    stock_entry.place(y=50, x=70)
    #Precio
    tk.Label(formulario_frame, text="Precio").place(x=0, y=75)
    precio_entry=tk.Entry(formulario_frame, width=10)
    precio_entry.place(y=75,x=70)
    guardar_btn=tk.Button(formulario_frame, text="Guardar", width=10, pady=1)
    guardar_btn.place(y=100,x=265)



