from flask import Flask, jsonify
from config import Config
from modelos import db, Cliente, Contacto, Sitio, Equipo  # Importa los modelos necesarios

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa la base de datos
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

# Rutas adicionales
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

@app.route('/pagina_base')
def pagina_base():
    return render_template('pagina_base.html')

if __name__ == '__main__':
    app.run(debug=True)
