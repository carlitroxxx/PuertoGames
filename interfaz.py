import tkinter as tk
from connection import listaJuegos

listado = listaJuegos()

frame = tk.Tk()
frame.title("Videojuegos")
frame.geometry("800x400")

titulo = tk.Label(frame, text="Catálogo", font=("Arial",16,"bold"))
titulo.pack(pady=10)

texto = tk.Text(frame, height=15, width=70, font=("Arial", 10))
texto.pack()

for juego in listado:
    id_videojuego,titulo, precio, stock,id_plataforma = juego
    
    texto.insert(tk.END, f"{titulo} | {id_plataforma} | {precio} | {stock}\n")
    
        
        
cerrar_btn=tk.Button(frame, text="Cerrar", command=frame.destroy)
cerrar_btn.pack(pady=10)
frame.mainloop()
