from flask import Flask, render_template

app = Flask(__name__)

ARTICULOS = [
    {
        "titulo": "Mi primer día con Flask",
        "resumen": "Cómo pasé de páginas estáticas a una aplicación que genera HTML con Python.",
        "fecha": "12 oct 2026",
    },
    {
        "titulo": "Por qué uso entornos virtuales",
        "resumen": "Una caja aislada para las librerías de cada proyecto evita muchos dolores de cabeza.",
        "fecha": "14 oct 2026",
    },
    {
        "titulo": "Tailwind sin instalar nada",
        "resumen": "El CDN es perfecto para prototipar, aunque en producción se instala bien.",
        "fecha": "16 oct 2026",
    },
    {
        "titulo": "Tailwind sin instalar nada",
        "resumen": "El CDN es perfecto para prototipar, aunque en producción se instala bien.",
        "fecha": "16 oct 2026",
    },
]


@app.route("/")
def inicio():
    return render_template("index.html", articulos=ARTICULOS)


@app.route("/acerca")
def acerca():
    return "<h1>Acerca de Pluma</h1>"


if __name__ == "__main__":
    app.run(debug=True)