from . import db

class Sitio(db.Model):
    __tablename__ = 'Sitios'
    id = db.Column('Id', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    cliente_id = db.Column('ClienteId', db.Integer, db.ForeignKey('Clientes.Id'))
    ubicacion = db.Column('Ubicacion', db.String(200))
    equipos = db.relationship('Equipo', backref='sitio', lazy=True)
