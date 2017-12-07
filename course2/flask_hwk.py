from flask import Flask, render_template, request, redirect
from pymongo import 

client = MongoClient()

db = client.coleccion

app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/login", methods=['GET','POST'])
def foo():
    dics = {}
    usuario = request.form["usuario"]
    clave = request.form["clave"]
    edad = request.form["edad"]
	# TODO: Validar usuario y clave
    print("Ingresando con {} ({}) y edad {}".format(usuario, clave, edad))
    dics['usuario'] = usuario
    dics['clave'] =  clave
    dics['edad'] = edad
    result = db.coleccion.insert_one({
        "usuario" = dics['usuario'],
        "clave" = dics['clave'],
        "edad" = dics['edad']
    })
    
    print(dics)

    return redirect("/")

@app.route("/personas")
def impr_forma():
    forma = db.coleccion.find()
    print("Personas: \n {}".format(forma))
    

app.run()