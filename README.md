# 🪶 Pluma

Blog con panel de administración construido con Flask y SQLite. Permite leer artículos y crear, editar y borrar entradas desde el navegador (CRUD completo).

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white)

![Vista previa de Pluma](docs/preview.png)

## ✨ Características

- CRUD completo: crear, leer, editar y borrar artículos
- Plantillas Jinja2 con herencia (`base.html`) para no repetir menú ni footer
- Base de datos SQLite con consultas parametrizadas (protección contra inyección SQL)
- Rutas con parámetros (`/articulo/<id>`) y páginas 404 personalizadas
- Borrado solo por `POST`, con confirmación en el navegador
- Escape automático de HTML (protección contra XSS)
- Diseño responsivo con Tailwind CSS

## 🛠️ Tecnologías

- **Python 3.10**
- **Flask** (rutas, formularios, plantillas)
- **SQLite** (módulo `sqlite3` incluido en Python)
- **Jinja2** para las plantillas
- **Tailwind CSS** (vía CDN)

## 📁 Estructura

```
pluma-blog/
├── app.py
├── database.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── articulo.html
│   ├── nuevo.html
│   ├── editar.html
│   ├── acerca.html
│   └── 404.html
└── docs/
    └── preview.png
```

## ▶️ Cómo ejecutarlo en local

```bash
git clone https://github.com/EstebanPat98/pluma-blog.git
cd pluma-blog
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abre `http://127.0.0.1:5000` en el navegador. La base de datos se crea sola la primera vez.

## 🔐 Limitaciones conocidas

- El panel de administración **no tiene login**: cualquiera con acceso a la aplicación puede crear, editar o borrar. Está pensado como proyecto de aprendizaje en local.
- La autenticación se implementa en un proyecto posterior de este portafolio.

## 📚 Lo que aprendí

- Crear y usar entornos virtuales y `requirements.txt`
- Definir rutas, métodos GET/POST y redirecciones en Flask
- Diseñar una base de datos y usar SQL (SELECT, INSERT, UPDATE, DELETE)
- Prevenir inyección SQL y XSS

## 👤 Autor

**Esteban A Espinosa Patiño**: [GitHub](https://github.com/EstebanPat98)