from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        return render_template('resultado_ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/submit_ejercicio2', methods=['POST'])
def submit_ejercicio2():

    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']


    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)


    cantidad_caracteres = len(nombre_mas_largo)

    return render_template('resultado_ejercicio2.html', nombreMasLargo=nombre_mas_largo, cantidadCaracteres=cantidad_caracteres)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)