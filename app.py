from flask import Flask, render_template, abort
from database import init_db, obtener_articulos, obtener_articulo

app = Flask(__name__)

init_db()


@app.route("/")
def inicio():
    articulos = obtener_articulos()
    return render_template("index.html", articulos=articulos)


@app.route("/articulo/<int:articulo_id>")
def articulo(articulo_id):
    articulo = obtener_articulo(articulo_id)
    if articulo is None:
        abort(404)
    return render_template("articulo.html", articulo=articulo)


@app.route("/acerca")
def acerca():
    return "<h1>Acerca de Pluma</h1>"


if __name__ == "__main__":
    app.run(debug=True)