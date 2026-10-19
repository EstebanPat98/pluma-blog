import sqlite3

DB_NAME = "pluma.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            resumen TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
        """
    )

    cantidad = conn.execute("SELECT COUNT(*) FROM articulos").fetchone()[0]
    if cantidad == 0:
        conn.executemany(
            "INSERT INTO articulos (titulo, resumen, contenido, fecha) VALUES (?, ?, ?, ?)",
            [
                (
                    "Mi primer día con Flask",
                    "Cómo pasé de páginas estáticas a una aplicación que genera HTML con Python.",
                    "Hoy descubrí que una página puede construirse en el momento, según los datos que haya.",
                    "2026-10-12",
                ),
                (
                    "Por qué uso entornos virtuales",
                    "Una caja aislada para las librerías de cada proyecto evita muchos dolores de cabeza.",
                    "Cada proyecto tiene sus propias versiones de las librerías, sin mezclarse con los demás.",
                    "2026-10-14",
                ),
                (
                    "Tailwind sin instalar nada",
                    "El CDN es perfecto para prototipar, aunque en producción se instala bien.",
                    "Con una sola línea en el HTML puedes usar todas las clases de Tailwind.",
                    "2026-10-16",
                ),
            ],
        )

    conn.commit()
    conn.close()


def obtener_articulos():
    conn = get_connection()
    articulos = conn.execute("SELECT * FROM articulos ORDER BY id DESC").fetchall()
    conn.close()
    return articulos