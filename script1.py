from flask import Flask, render_template

#Instanciamos Flask, le pasamos la palabra reservada __name__ en el constructor  (esta palabra representa el nombre de nuestro script 
# de python) y lo guardamos en una variable
app = Flask(__name__)

#Usamos nuestra instancia de flask como decorador (con el prefijo "@"") e invocamos a su método route, el cual
#recibirá el nombre de la ruta de nuestro sitio que queremos mostrar en forma de string
@app.route("/")
#Justo después de definir la ruta, creamos una función que maneje la petición
def home():
    #Para renderizar un sitio web completo en vez de sólo un string, deberemos crear un archivo html aparte dentro de una carpeta
    #llamada templates. Una vez que lo tengamos invocamos al método "render_template"´(que deberemos importar previamente desde flask) 
    #en el return de nuestra función controladora y le pasamos el nombre de neustro archivo en forma de string 
    return render_template("home.html")

#Podemos crear tantas rutas como necesitemos siguiendo el mismo procedimiento, por ejemplo aquí crearé una para la sección "acerca de"
@app.route("/about/")
def about():
    return render_template("about.html")

#Cuando ejecutemos un script desde su propio archivo, el intérprete de python siempre le asignara el nombre __main__, en cambio si lo 
#importamos y lo ejecutamos desde otro script, se le asignará el nombre con el que hayamos guardado el archivo, por tanto antes de ejecutar
#la aplicación verificamos que el nombre sea igual a __main__ 
if __name__ == "__main__":
    app.run(debug=True)