import sys
import os

# Agrega la ruta del proyecto al sys.path
sys.path.insert(0, '/opt/flask-app/inventory/www')

# Importa la aplicación desde app.py
from app import app as application
