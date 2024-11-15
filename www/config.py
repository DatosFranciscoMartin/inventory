import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://flask_user:Datos!2022@localhost/InventarioEquipos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'd2e7f842f5b86e3f4f83d8e7362392e65028c59c87f87e1f46a3b6183d9e2a8d'