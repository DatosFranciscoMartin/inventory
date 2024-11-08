from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, Flask!"


# Configuración de la conexión a MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="myadmin",
        password="password",
        database="InventarioEquipos"
    )
    return connection

# Ejemplo de ruta para obtener datos
@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sitios")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

