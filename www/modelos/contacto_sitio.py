from . import db

class ContactoSitio(db.Model):
    __tablename__ = 'ContactosSitios'
    sitio_id = db.Column('SitioId', db.Integer, db.ForeignKey('Sitios.Id'), primary_key=True)
    contacto_id = db.Column('ContactoId', db.Integer, db.ForeignKey('Contactos.Id'), primary_key=True)
