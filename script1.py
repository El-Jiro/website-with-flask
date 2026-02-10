from flask import Flask #importamos la clase Flask desde la librería homónima

#Instanciamos Flask, le pasamos la palabra reservada __name__ en el constructor  (esta palabra representa el nombre de nuestro script 
# de python) y lo guardamos en una variable
app = Flask(__name__)

#Usamos nuestra instancia de flask como decorador (con el prefijo "@"") e invocamos a su método route, el cual
#recibirá el nombre de la ruta de nuestro sitio que queremos mostrar en forma de string
@app.route("/")
#Justo después de definir la ruta, creamos una función que maneje la petición
def show_home():
    return "El contenido del sitio va aquí"

#Cuando ejecutemos un script desde su propio archivo, el intérprete de python siempre le asignara el nombre __main__, en cambio si lo 
#importamos y lo ejecutamos desde otro script, se le asignará el nombre con el que hayamos guardado el archivo, por tanto antes de ejecutar
#la aplicación verificamos que el nombre sea igual a __main__ 
if __name__ == "__main__":
    app.run(debug=True)