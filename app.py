from flask import Flask 

app = flask(__name__)

@app.route('/')

def index():
   print("hello")
   return "hello, word"

app.route('/info')
def info():
   modulo = "flask"
   aula = "1"
   return f"<h1>modulo: {modulo}, aula: {aula} </h1>"

app.route('/bemvindo/<usuario>')
def bemvindo(usuario):
   modulo = "css"
   aula = "1"
   return f"<h1>modulo: {usuario.capitalize()}, aula: {aula} </h1>"



