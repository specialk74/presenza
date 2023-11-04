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

@app.route('/<int:idx>/update', methods=('POST',))
def update(idx):
    connection = connect()
    data = request.get_json()
    
    pranzo = data['data']['pranzo']
    cena = data['data']['cena']
    dormire = data['data']['dormire']

    values = connection.execute('SELECT * FROM presenza WHERE id=?', (idx,)).fetchall()

    connection.execute('UPDATE presenza SET pranzo=?, cena=?, dormire=?, lastupdate WHERE id=?', (pranzo, cena, dormire, datetime(), idx))
    connection.commit()    

    connection.close()

    return redirect('/presenza')
 
if __name__ == '__main__':
    print(args)
    print("Port: " + args.port)
    print("Path: " + args.path)
    app.run(host='0.0.0.0', port=args.port, threaded=True)
       
