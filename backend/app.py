# app.py
from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_student():
    data = request.json
    name = data.get('name')
    code = data.get('code')
    date = data.get('date')

    # Aquí puedes agregar código para insertar los datos en la base de datos
    # Por ejemplo, puedes usar SQLite para la base de datos localmente
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, code, date) VALUES (?, ?, ?)', (name, code, date))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Student registered successfully'})

@app.errorhandler(Exception)
def handle_error(error):
    logging.error('An error occurred: %s', error)
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
