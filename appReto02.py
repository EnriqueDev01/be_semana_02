from flask import Flask, request

app = Flask(__name__)

productos = {}

@app.route('/')
def index():
    return '<h3 style="color:teal">Semana 2 - Reto 2</h3>'

@app.route('/productos/')
def listarProductos():
    return productos

@app.route('/crear_producto/', methods=['POST'])
def crearProducto():
    data = request.json
    productos[data['nombre']] = {        
        'precio': data['precio'],
        'descripcion': data['descripcion']
    }
    return {'resultado': 201}

if __name__ == '__main__':
    app.run()