from flask import Flask, render_template, redirect, request, json
import os
import sqlite3
import pathlib
import click
from argparse import ArgumentParser

app = Flask(__name__)
parser = ArgumentParser()
parser.add_argument('--port')
parser.add_argument('--path')
args = parser.parse_args()

def connect():
    connection = sqlite3.connect(args.path + '/database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/presenza')
def index():
    connection = connect()

    presenze = connection.execute('SELECT * FROM presenza ORDER BY id').fetchall()
        
    connection.close()

    return render_template('index.html', presenze=presenze)

@app.route('/update', methods=('POST',))
def update():
    connection = connect()
    data = request.get_json()
    value = data['data']['value']
    oldValue = 0
    action = "";
    
    if ('pranzo' in value):
        action = 'pranzo'
    elif ('cena' in value):
        action = 'cena'
    elif ('dormire' in value):
        action = 'dormire'

    value = value[len(action):]
    giorno = int(value[1])
    idx = int(value[3])
    
    presenze = connection.execute('SELECT * FROM presenza WHERE id='+str(idx)).fetchall()
    oldValue = presenze[0][action]
    newValue = oldValue ^ (1 << giorno)
    update_str = 'UPDATE presenza SET '+action+'=? WHERE id=?'
    
    connection.execute(update_str, (newValue, idx))
    connection.commit()    

    connection.close()

    return redirect('/presenza')
 
if __name__ == '__main__':
    print(args)
    print("Port: " + args.port)
    print("Path: " + args.path)
    app.run(host='0.0.0.0', port=args.port, threaded=True)
       
