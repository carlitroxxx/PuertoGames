import pyodbc


def listaJuegos():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=W608-PCX\SQLEXPRESS;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    
    cursor.execute(
        """
        SELECT id_videojuego, titulo, precio, stock, id_plataforma
        FROM Videojuegos
        """)
    lista = cursor.fetchall()
    conn.close()
    return lista