from flask import Flask, request

app = Flask(__name__)

tareas = {}

@app.route('/')
def index():
    return '<h3 style="color:teal">Semana 2 - Reto 3</h3>'

@app.route('/tareas/')
def listarProductos():
    return tareas

@app.route('/crear_tarea/', methods=['POST'])
def crearProducto():
    data = request.json
    tareas[data['id']] = {        
        'nombre': data['nombre'],
        'prioridad': data['prioridad']
    }
    return {'resultado': 201}

@app.route('/actualizar_tarea/', methods=['PUT'])
def actualizarTarea():
    id = request.args.get('id')
    data = request.json
    tareas[id] = data
    return {'resultado': 204}

@app.route('/eliminar_tarea/', methods=['DELETE'])
def eliminarTarea():
    id = request.args.get('id')
    tareas.pop(id)
    return {'resultado': 204}

if __name__ == '__main__':
    app.run()