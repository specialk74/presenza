import sqlite3
from datetime import datetime

connection = sqlite3.connect('/home/pi/Presenza/database.db')
connection.row_factory = sqlite3.Row

rows = connection.execute('SELECT * FROM presenza ORDER BY id').fetchall()

for row in rows:
 print(row['cenaDefault'])

 d = datetime.now()
 
 if (d.weekday() == 0):
  shiftter = 6
 else:
  shiftter = d.weekday() - 1
  
 newPranzo = row['pranzo'] >> 1
 if (row['pranzoDefault'] & (1 << shiftter)) != 0:
   newPranzo = newPranzo | (1 << 6)

 newCena = row['cena'] >> 1
 if (row['cenaDefault'] & (1 << shiftter)) != 0:
   newCena = newCena | (1 << 6)

 newDormire = row['dormire'] >> 1
 if (row['dormireDefault'] & (1 << shiftter)) != 0:
  newDormire = newDormire | (1 << 6)

 connection.execute('UPDATE presenza SET pranzo=?, cena=?, dormire=? WHERE id=?', (newPranzo, newCena, newDormire, row['id']))

connection.commit()


connection.close()
