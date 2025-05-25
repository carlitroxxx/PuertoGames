import pyodbc

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