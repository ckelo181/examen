from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])
        total_sin_descuento = cantidad_tarros * 9000
        descuento = 0.0

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_descuento = total_sin_descuento * descuento
        total_a_pagar = total_sin_descuento - total_descuento
        tiene_descuento = "Sí" if descuento > 0 else "No"

        return render_template('formulario.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total_descuento=total_descuento, total_a_pagar=total_a_pagar,
                               tiene_descuento=tiene_descuento)

    return render_template('formulario.html')

users = {
    'juan': 'admin',
    'pepe': 'user'
}



@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            if username == 'juan':
                mensaje = "Bienvenido administrador juan"
            elif username == 'pepe':
                mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('login.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
