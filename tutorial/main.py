from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    print('Antes de la petición')

@app.after_request
def after_request(response):
    print('Después de la petición')
    return response
    
@app.route('/')
def index():
    name = 'codi'
    course = 'Python web'
    is_premium = False
    courses = ['Python', 'Ruby', 'Java']

    return render_template('index.html', username=name, course_name=course, is_premium=is_premium, courses=courses)

@app.route('/usuario/<username>/<int:age>')
def usuario(username, age):
    return 'Hola ' + username + ' ' + str(age)

@app.route('/datos')
def datos():
    id = request.args.get('id')

    return 'Listado de datos' + str(id)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=9000)