from . import db

class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column('Id', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    persona_contacto_id = db.Column('PersonaContactoId', db.Integer, db.ForeignKey('Contactos.Id'))
    sitios = db.relationship('Sitio', backref='cliente', lazy=True)
