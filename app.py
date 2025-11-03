from flask import Flask 

app = flask(__name__)

@app.route('/')

def index():
    return "olá, mundo !"
if name == '__main__':
    app.run(debug=True)
    
    