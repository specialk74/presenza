#!/usr/bin/python3
import requests
from argparse import ArgumentParser
import sqlite3
from datetime import datetime
import configparser
import os

last_message_filename = "/home/pi/Presenza/last_message.txt"

connection = sqlite3.connect('/home/pi/Presenza/database.db')
connection.row_factory = sqlite3.Row
rows = connection.execute('SELECT * FROM presenza ORDER BY id').fetchall()
connection.close()

config = configparser.ConfigParser()
config.read('/home/pi/Presenza/config.ini')

parser = ArgumentParser()
parser.add_argument('--message')
args = parser.parse_args()

colonna = None
if (args.message == '1'):
	colonna = 'pranzo'
elif (args.message == '2'):
	colonna = 'cena'
elif (args.message == '3'):
	colonna = 'dormire'

esci = True
for row in rows:
	if (row[colonna] & 0x01 == 0x00):
		esci = False
		break

if (esci == True):
	print("Sono tutti a casa per '{}'".format(colonna))
	exit()

TOKEN = config['DEFAULT']['TELEGRAM_TOKEN']
CHAT_ID = config['DEFAULT']['TELEGRAM_CHAT_ID']
HTTP = config['DEFAULT']['HTTP']

message = None

if (args.message == '1'):
    message = "Manca un'ora alla chiusura per prenotarsi il pranzo... -> " + HTTP
elif (args.message == '2'):
    message = "Manca un'ora alla chiusura per prenotarsi la cena... -> " + HTTP
elif (args.message == '3'):
    message = "Manca un'ora alla prenotazione prima di rimanere chiusi fuori... -> " + HTTP

if (TOKEN == None):
	print("ELEGRAM_TOKEN None")
	exit()
if (CHAT_ID == None):
	print("TELEGRAM_CHAT_ID None")
	exit()
if (message == None):
	print("message None")
	exit()
	
if os.path.exists(last_message_filename):
	with open(last_message_filename,"r") as f:
		last_message = f.readline()
		f.close()
		url = "https://api.telegram.org/bot{}/deleteMessage?chat_id={}&message_id={}".format(TOKEN,CHAT_ID,last_message)
		response = requests.get(url).json()
		print(response) # this sends the message

url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN,CHAT_ID,message)
response = requests.get(url).json()
with open(last_message_filename,"w") as f:
	f.write("{}".format(response['result']['message_id']))
	f.close()
#print(response['result']['message_id'])
print(response) # this sends the message
