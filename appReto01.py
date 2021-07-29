from flask import Flask

app = Flask(__name__)

departamentos = [
    {'nombre':'amazonas', 'capital':'chachapoyas', 'superficie':39249},
    {'nombre':'ancash', 'capital':'huaraz', 'superficie':35914},
    {'nombre':'apurimac', 'capital':'abancay', 'superficie':20895},
    {'nombre':'arequipa', 'capital':'arequipa', 'superficie':63345},
    {'nombre':'ayacucho', 'capital':'ayacucho', 'superficie':43814},
    {'nombre':'cajamarca', 'capital':'cajamarca', 'superficie':33317},
    {'nombre':'callao', 'capital':'callao', 'superficie':146},
    {'nombre':'cusco', 'capital':'cusco', 'superficie':71986},
    {'nombre':'huancavelica', 'capital':'huancavelica', 'superficie':22131},
    {'nombre':'huanuco', 'capital':'huanuco', 'superficie':36848},
    {'nombre':'ica', 'capital':'ica', 'superficie':21327},
    {'nombre':'junin', 'capital':'huancayo', 'superficie':44197},
    {'nombre':'la libertad', 'capital':'trujillo', 'superficie':25499}
]

@app.route('/')
def index():
    return '<h3 style="color:teal">Semana 2 - Reto 1</h3>'

@app.route('/departamentos/')
def listarDepartamentos():
    mensaje = 'departamentos del Peru'
    return {
        'ok': True,
        'content': departamentos,
        'message': mensaje
    }        

if __name__ == '__main__':
    app.run()