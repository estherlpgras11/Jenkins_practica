import os
from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flaskext.mysql import MySQL


app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD',
                                                  'root')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB', 'data')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'db')
app.config['MYSQL_DATABASE_PORT'] = os.getenv('MYSQL_DATABASE_PORT', 3306)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12345')


mysql = MySQL(app)


@app.route('/register', methods=['POST'])
@cross_origin(headers=['Content-Type'])
def register():
    content = request.get_json()
    email = content['email']
    name = content['name']
    error = False
    conn = mysql.connect()
    cur = conn.cursor()
    try:
        cur.execute(f'INSERT INTO orders (email, name) VALUES ("{email}","{name}")')
        conn.commit()
        msg = 'Registered successfully'
    except Exception:
        error = True
        msg = f'Error occured: please try again later.'
    conn.close()
    response = jsonify({'error': error, 'msg': msg})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/items')
def items():
    result = None
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items;')
    result = cur.fetchall()
    conn.close()
    response = jsonify({'error': False, 'result': result})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    debug = bool(os.getenv('APP_DEBUG', False))
    app.run(debug=debug, host='0.0.0.0', port=5000)
