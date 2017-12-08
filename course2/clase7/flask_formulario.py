from flask import Flask, render_template, request, redirect
from pymongo import MongoClient 
from pprint import pprint

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
    ocupacion = request.form["ocupacion"]
	# TODO: Validar usuario y clave
    print("Ingresando con {} ({}) y edad {}".format(usuario, clave, edad))
    dics['usuario'] = usuario
    dics['clave'] =  clave
    dics['edad'] = edad
    dics['ocupacion'] = ocupacion
    result = db.reg.insert_one({
    "usuario" : dics['usuario'],
    "clave" : dics['clave'],
    "edad" : dics['edad'],
    "ocupacion" : dics['ocupacion']
    })
    
    print(dics)

    return redirect("/")

@app.route("/personas")
def impr_forma():
    forma = db.reg.find({})
    lista = []
    for docs in forma:
        lista.append(docs)
    return "Personas: \n {}".format(lista)

app.run()