from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        cans = int(request.form['cans'])
        price_per_can = 9000

        total = cans * price_per_can

        if age >= 18 and age <= 30:
            discount = total * 0.15
        elif age > 30:
            discount = total * 0.25
        else:
            discount = 0

        total_discounted = total - discount

        result = {
            'name': name,
            'total': total,
            'discount': discount,
            'total_discounted': total_discounted
        }

        return render_template('ejercicio1.html', result=result)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'juan' and password == 'admin':
            message = f'Bienvenido administrador {username}'
        elif username == 'pepe' and password == 'user':
            message = f'Bienvenido usuario {username}'
        else:
            message = 'Usuario o contraseña incorrectos'

        return render_template('ejercicio2.html', message=message)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
