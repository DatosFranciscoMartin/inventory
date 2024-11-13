from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

# Importar los modelos para que SQLAlchemy pueda reconocerlos
from .cliente import Cliente
from .contacto import Contacto
from .sitio import Sitio
from .equipo import Equipo
from .contacto_sitio import ContactoSitio
