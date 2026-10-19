from flask import Flask, render_template, abort, request, redirect, url_for

from database import (
    init_db, obtener_articulos, obtener_articulo,
    crear_articulo, actualizar_articulo, borrar_articulo,
)

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


@app.route("/admin/nuevo", methods=["GET", "POST"])
def nuevo_articulo():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        resumen = request.form["resumen"].strip()
        contenido = request.form["contenido"].strip()

        if titulo and resumen and contenido:
            crear_articulo(titulo, resumen, contenido)
            return redirect(url_for("inicio"))

    return render_template("nuevo.html")


@app.route("/admin/editar/<int:articulo_id>", methods=["GET", "POST"])
def editar_articulo(articulo_id):
    articulo = obtener_articulo(articulo_id)
    if articulo is None:
        abort(404)

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        resumen = request.form["resumen"].strip()
        contenido = request.form["contenido"].strip()

        if titulo and resumen and contenido:
            actualizar_articulo(articulo_id, titulo, resumen, contenido)
            return redirect(url_for("articulo", articulo_id=articulo_id))

    return render_template("editar.html", articulo=articulo)


@app.route("/admin/borrar/<int:articulo_id>", methods=["POST"])
def borrar(articulo_id):
    if obtener_articulo(articulo_id) is None:
        abort(404)
    borrar_articulo(articulo_id)
    return redirect(url_for("inicio"))

@app.route("/acerca")
def acerca():
    return "<h1>Acerca de Pluma</h1>"


if __name__ == "__main__":
    app.run(debug=True)