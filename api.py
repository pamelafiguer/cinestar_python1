from flask import Flask
import mysql.connector
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

localhost = {
    'host' : 'localhost',
    'user' : 'root',
    'database' : 'cinestar'
}

hostinger = {
    'host' : 'srv1467.hstgr.io',
    'user' : 'u719737586_cinestar',
    'password' : 'Senati2024@',
    'database' : 'u719737586_cinestar'
}

cnx = mysql.connector.connect(**hostinger)
cursor = cnx.cursor(dictionary=True)



@app.route("/cines")
def cines():
    cursor.callproc("sp_getCines")
    for row in cursor.stored_results() :
        cines = row.fetchall()
    
    
    cines = {'success': True, 'data': cines, 'message': message}
    cursor.close()
    return cines 



@app.route("/peliculas")
def peliculas():
    return "peliculas"


if __name__ == "__main__" :
    app.run(debug=True)