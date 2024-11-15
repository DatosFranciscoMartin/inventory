from . import db

class Equipo(db.Model):
    __tablename__ = 'Equipos'
    id = db.Column('Id', db.Integer, primary_key=True)
    proveedor = db.Column('Proveedor', db.String(100))
    marca = db.Column('Marca', db.String(50))
    nserie = db.Column('Nserie', db.String(50), unique=True)
    licencia = db.Column('Licencia', db.String(100))
    fecha_compra = db.Column('FechaCompra', db.Date)
    esta_en_soporte = db.Column('EstaEnSoporte', db.Boolean, default=True)
    sitio_id = db.Column('SitioId', db.Integer, db.ForeignKey('Sitios.Id'))
    fecha_fin = db.Column('FechaFin', db.Date)
    renovacion = db.Column('Renovacion', db.Date)
    contacto_id = db.Column('ContactoId', db.Integer, db.ForeignKey('Contactos.Id'))
    sitio = db.relationship('Sitio', backref='equipos')
    contacto = db.relationship('Contacto', backref='equipos')
