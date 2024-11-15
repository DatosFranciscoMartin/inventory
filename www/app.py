from flask import Flask, render_template, redirect, url_for, request
from config import Config
from modelos import db, Cliente, Contacto, Sitio, Equipo  # Importa los modelos necesarios
from forms import EquipoForm

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

@app.route('/consultas', methods=['GET'])
def consultas():
    return render_template('consultas.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    consulta = request.form.get('consulta')
    resultados = []

    if consulta == 'clientes':
        resultados = [
            {
                'id': cliente.id, 
                'nombre': cliente.nombre
            }
            for cliente in Cliente.query.all()]
    elif consulta == 'sitios':
        resultados = [
            {
                'id': sitio.id, 
                'nombre': sitio.nombre, 
                'ubicacion': sitio.ubicacion
            } 
            for sitio in Sitio.query.all()]
    elif consulta == 'equipos':
        resultados = [
            {
                'id': equipo.id,
                'proveedor': equipo.proveedor,
                'marca': equipo.marca,
                'nserie': equipo.nserie,
                'fecha_compra': equipo.fecha_compra,
                'esta_en_soporte': equipo.esta_en_soporte
            }
            for equipo in Equipo.query.all()
        ]
    elif consulta == 'contactos':
        resultados = [
            {
                'id': contacto.id,
                'nombre': contacto.nombre,
                'apellidos': contacto.apellidos,
                'correo_electronico': contacto.correo_electronico,
                'telefono': contacto.telefono
            }
            for contacto in Contacto.query.all()
        ]

    return render_template('consultas.html', resultados=resultados)

@app.route('/equipos', methods=['GET', 'POST'])
def manage_equipos():
    form = EquipoForm()
    # Cargar opciones para Sitio y Contacto
    form.sitio_id.choices = [(s.id, s.nombre) for s in Sitio.query.all()]
    form.contacto_id.choices = [(c.id, c.nombre) for c in Contacto.query.all()]

    if form.validate_on_submit():
        equipo = Equipo(
            proveedor=form.proveedor.data,
            marca=form.marca.data,
            nserie=form.nserie.data,
            licencia=form.licencia.data,
            fecha_compra=form.fecha_compra.data,
            esta_en_soporte=form.esta_en_soporte.data,
            sitio_id=form.sitio_id.data,
            fecha_fin=form.fecha_fin.data,
            renovacion=form.renovacion.data,
            contacto_id=form.contacto_id.data
        )
        db.session.add(equipo)
        db.session.commit()
        return redirect(url_for('manage_equipos'))

    equipos = Equipo.query.all()
    return render_template('equipos.html', form=form, equipos=equipos)

if __name__ == '__main__':
    app.run(debug=True)
