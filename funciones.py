import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
#'SERVER=W608-PCX\SQLEXPRESS;'
formulario_frame = None

#Lista de juegos para la tabla
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

#Lista de plataformas para el combobox
def listaPlataformas():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=CARLOS\\SQLEXPRESS;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM Plataformas")
    plataformas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return plataformas

#Funcion para recargar tabla
def cargarTabla(tabla,listado):
    for item in tabla.get_children():
        tabla.delete(item)
    for juego in listado:
        id_videojuego,titulo, precio, stock,nombre = juego
        tabla.insert(parent='', index='end', iid=id_videojuego, text='', values=(id_videojuego,titulo,nombre,stock,precio))
        
#Funcion para eliminar algun juego en la BD
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
            conn.close()

    except ValueError:
        print("Error!")
    except Exception as e:
        print(e)
#Funcion para eliminar en la tabla
def eliminarJuego(tabla):
    eliminar(tabla)
    listado = listaJuegos()
    cargarTabla(tabla,listado)

#Funcion de formulario para guardar un videojuego
def agregarTK(ventana,tabla):
    global formulario_frame, titulo_entry, plataforma_combobox, stock_entry, precio_entry
    
    formulario_frame = tk.LabelFrame(ventana, text="Agregar Videojuego", padx=10, pady=10)
    formulario_frame.place(x=300,y=475,width=375, height=175)
    #titulo
    tk.Label(formulario_frame, text="Titulo").place(x=0, y=0)
    titulo_entry= tk.Entry(formulario_frame, width=45)
    titulo_entry.place(y=0,x=70)
    #plataforma
    tk.Label(formulario_frame, text="Plataforma").place(x=0, y=25)
    plataformas=listaPlataformas()
    plataforma_combobox = ttk.Combobox(formulario_frame, values=plataformas, state="readonly", width=42)
    plataforma_combobox.place(x=70, y=25)
    #stock
    tk.Label(formulario_frame, text="Stock").place(x=0, y=50)
    stock_entry=tk.Entry(formulario_frame, width=10)
    stock_entry.place(y=50, x=70)
    #Precio
    tk.Label(formulario_frame, text="Precio").place(x=0, y=75)
    precio_entry=tk.Entry(formulario_frame, width=10)
    precio_entry.place(y=75,x=70)
    guardar_btn=tk.Button(formulario_frame, text="Guardar", width=10, pady=1, command=lambda: guardarJuego(tabla))
    guardar_btn.place(y=100,x=265)
    
#Funcion para agregar videojuego en la BD
def guardarJuego(tabla):
    global formulario_frame, titulo_entry, plataforma_combobox, stock_entry, precio_entry
    titulo = titulo_entry.get().strip()
    plataforma = plataforma_combobox.get().strip()
    stock = stock_entry.get().strip()
    precio = precio_entry.get().strip()

    if not titulo or not plataforma or not stock or not precio:
        messagebox.showwarning("ALERTA","Debes completar todos los campos")
        return
    if not stock.isdigit():
        messagebox.showwarning("ALERTA","Stock debe ser numérico")
        return
    if not precio.isdigit():
        messagebox.showwarning("ALERTA","Precio debe ser numérico")
        return
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=CARLOS\\SQLEXPRESS;'
            'DATABASE=PuertoGames2025;'
            'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id_plataforma FROM Plataformas WHERE nombre = ?", (plataforma,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", f"La plataforma existente.")
            conn.close()
            return
        id_plataforma = resultado[0]
        #Insertamos el Videojuego
        cursor.execute(
            "INSERT INTO Videojuegos (titulo, id_plataforma, stock, precio) VALUES (?, ?, ?, ?)",
            (titulo, id_plataforma, stock, precio)
        )
        conn.commit()
        messagebox.showinfo("Éxito", f"Videojuego '{titulo}' agregado correctamente.")
        conn.close()

        #Actualizamos la Tabla
        listado = listaJuegos()
        cargarTabla(tabla, listado)

        #Limpiamos el formulario
        titulo_entry.delete(0, tk.END)
        plataforma_combobox.set(plataforma)
        stock_entry.delete(0, tk.END)
        precio_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el videojuego: {e}")



#Funcion para algun juego seleccionado
def formularioEditar(ventana, tabla):
    global formulario_frame, titulo_entry,plataforma_combobox, stock_entry, precio_entry
    
    id= tabla.focus()
    if not id:
        messagebox.showwarning("Atención","No se ha seleccionado ningun videojuego.")
        return
    #Formulario
    formulario_frame = tk.LabelFrame(ventana, text="Editar Videojuego", padx=10, pady=10)
    formulario_frame.place(x=300, y=475, width=375, height=175)
    #Titulo
    tk.Label(formulario_frame, text="Titulo").place(x=0, y=0)
    titulo_entry = tk.Entry(formulario_frame, width=45)
    titulo_entry.place(x=70, y=0)
    #Plataforma
    tk.Label(formulario_frame, text="Plataforma").place(x=0, y=25)
    plataformas=listaPlataformas()
    plataforma_combobox = ttk.Combobox(formulario_frame, values=plataformas, state="readonly", width=42)
    plataforma_combobox.place(x=70, y=25)
    #Stock
    tk.Label(formulario_frame, text="Stock").place(x=0, y=50)
    stock_entry = tk.Entry(formulario_frame, width=10)
    stock_entry.place(x=70, y=50)
    #Precio
    tk.Label(formulario_frame, text="Precio").place(x=0, y=75)
    precio_entry = tk.Entry(formulario_frame, width=10)
    precio_entry.place(x=70, y=75)
    #Boton Guardar
    guardar_btn = tk.Button(formulario_frame, text="Guardar", width=10, pady=1, command=lambda:(editarDatos(id_videojuego,tabla)))
    guardar_btn.place(x=265, y=100)
    
    id = tabla.focus()
    if id:
        juego = tabla.item(id, 'values')
        if juego:
            id_videojuego, titulo, plataforma, stock, precio = juego
            titulo_entry.insert(0, titulo)
            plataforma = plataforma_combobox.set(plataforma)
            stock_entry.insert(0, stock)
            precio_entry.insert(0, precio)
    tabla.bind("<<TreeviewSelect>>", seleccionTabla)
    
#Funcion para autocompletar campos cada vez que se seleccione una fila en la tabla 
def seleccionTabla(event):
    global titulo_entry, plataforma_combobox, stock_entry, precio_entry

    tabla = event.widget
    id = tabla.focus()
    if not id:
        return

    juego = tabla.item(id, 'values')
    if not juego:
        return

    id_videojuego, titulo, plataforma, stock, precio = juego

    #Autocompletar entry
    titulo_entry.delete(0, tk.END)
    titulo_entry.insert(0, titulo)

    plataforma_combobox.set(plataforma)


    stock_entry.delete(0, tk.END)
    stock_entry.insert(0, stock)

    precio_entry.delete(0, tk.END)
    precio_entry.insert(0, precio)
    #Boton Guardar
    guardar_btn = tk.Button(formulario_frame, text="Guardar", width=10, pady=1, command=lambda:(editarDatos(id_videojuego,tabla)))
    guardar_btn.place(x=265, y=100)

#Funcion para editar algun juego en la BD
def editarDatos(id,tabla):
    global titulo_entry, plataforma_combobox, stock_entry, precio_entry
    
    titulo=titulo_entry.get().strip()
    plataforma = plataforma_combobox.get().strip()
    precio=precio_entry.get().strip()
    stock=stock_entry.get().strip()
    
    #VALIDACIONES
    if not titulo or not plataforma or not precio or not stock:
        messagebox.showwarning("ALERTA","Debes completar todos los campos")
        return
    if not stock.isdigit():
        messagebox.showwarning("ALERTA","Stock debe ser numérico")
        return
    if not precio.isdigit():
        messagebox.showwarning("ALERTA","Precio debe ser numérico")
        return
    
    #Conexión a la base de datos
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=CARLOS\\SQLEXPRESS;'
            'DATABASE=PuertoGames2025;'
            'Trusted_Connection=yes;'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT id_plataforma FROM Plataformas WHERE nombre = ?", (plataforma,))
        resultado = cursor.fetchone()
        if not resultado:
            messagebox.showerror("Error", f"La plataforma existente.")
            conn.close()
            return
        id_plataforma = resultado[0]

        cursor.execute("""
            UPDATE Videojuegos
            SET titulo = ?, id_plataforma = ?, stock = ?, precio = ?
            WHERE id_videojuego = ?
        """, (titulo, id_plataforma, int(stock), precio, int(id)))
        conn.commit()
        conn.close()

        messagebox.showinfo("Info", "Videojuego actualizado correctamente.")

        listado = listaJuegos()
        cargarTabla(tabla, listado)

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

#Funcion para mostrar grafico de barras con la cantidad de juegos que pertenecen a una plataformas
def estadisticas():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=CARLOS\\SQLEXPRESS;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.nombre, COUNT(*) AS cantidad
        FROM Videojuegos v
        INNER JOIN Plataformas p ON v.id_plataforma = p.id_plataforma
        GROUP BY p.nombre
    """)
    
    datos = cursor.fetchall()
    conn.close()
    plataformas = [row[0] for row in datos]
    cantidades = [row[1] for row in datos]
    
    plt.figure(figsize=(8,6))
    plt.bar(plataformas, cantidades)
    plt.title('Cantidad de Videojuegos por Plataforma')
    plt.xlabel('Plataforma')
    plt.ylabel('Cantidad')
    plt.yticks(range(0, max(cantidades) + 5, 5))
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()
    plt.show()
    