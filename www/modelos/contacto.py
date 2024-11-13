from . import db

class Contacto(db.Model):
    __tablename__ = 'Contactos'
    id = db.Column('Id', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(50), nullable=False)
    apellidos = db.Column('Apellidos', db.String(50))
    correo_electronico = db.Column('CorreoElectronico', db.String(100))
    telefono = db.Column('Telefono', db.String(15))
    sitios = db.relationship('Sitio', secondary='ContactosSitios', backref='contactos', lazy=True)
