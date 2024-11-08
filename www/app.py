from flask import Flask, render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



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
    tabla = request.args.get('tabla')  # Obtener la tabla seleccionada del formulario
    
    if not tabla:
        return "No se ha seleccionado ninguna tabla", 400
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Ejecutar consulta SQL dinámica
    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Retornar los resultados en formato JSON
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

