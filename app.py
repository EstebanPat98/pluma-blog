from flask import Flask, render_template
from database import init_db, obtener_articulos

app = Flask(__name__)

init_db()


@app.route("/")
def inicio():
    articulos = obtener_articulos()
    return render_template("index.html", articulos=articulos)


@app.route("/acerca")
def acerca():
    return "<h1>Acerca de Pluma</h1>"


if __name__ == "__main__":
    app.run(debug=True)