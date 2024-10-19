from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Configuración de conexión para PostgreSQL
conn_str = {
    "host": "dpg-crnlv5l6l47c73ai705g-a.oregon-postgres.render.com",
    "database": "fisi_tweet",
    "user": "root",
    "password": "ROCR5iWHfufiDIHTQPNohyXiWFlooPhX"
}

# Conexión a la base de datos PostgreSQL
try:
    mydb = psycopg2.connect(**conn_str)
    print("Conexión exitosa a la base de datos PostgreSQL")
except Exception as e:
    print(f"No se pudo conectar a la base de datos PostgreSQL: {e}")

@app.route('/')
def Index():
    publicaciones = consultarTodasPublicaciones()
    return render_template('index.html', publicaciones=publicaciones)

def consultarTodasPublicaciones():
    try:
        cursor = mydb.cursor()
        query = '''
            SELECT alumnos.nombre, alumnos.correo, publicaciones.contenido, publicaciones.fecha
            FROM alumnos
            JOIN publicaciones ON alumnos.idAlumno = publicaciones.idAlumno
            ORDER BY publicaciones.fecha DESC
        '''
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except Exception as e:
        print(f"Error al consultar publicaciones: {e}")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Configuración de conexión para PostgreSQL
conn_str = {
    "host": "dpg-crnlv5l6l47c73ai705g-a.oregon-postgres.render.com",
    "database": "fisi_tweet",
    "user": "root",
    "password": "ROCR5iWHfufiDIHTQPNohyXiWFlooPhX"
}

# Conexión a la base de datos PostgreSQL
try:
    mydb = psycopg2.connect(**conn_str)
    print("Conexión exitosa a la base de datos PostgreSQL")
except Exception as e:
    print(f"No se pudo conectar a la base de datos PostgreSQL: {e}")

@app.route('/')
def Index():
    publicaciones = consultarTodasPublicaciones()
    return render_template('index.html', publicaciones=publicaciones)

def consultarTodasPublicaciones():
    try:
        cursor = mydb.cursor()
        query = '''
            SELECT alumnos.nombre, alumnos.correo, publicaciones.contenido, publicaciones.fecha
            FROM alumnos
            JOIN publicaciones ON alumnos.idAlumno = publicaciones.idAlumno
            ORDER BY publicaciones.fecha DESC
        '''
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except Exception as e:
        print(f"Error al consultar publicaciones: {e}")
        return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
