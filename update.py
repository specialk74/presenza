import sqlite3

connection = sqlite3.connect('database.db')
connection.row_factory = sqlite3.Row

rows = connection.execute('SELECT * FROM presenza ORDER BY id').fetchall()

for row in rows:
 print(row['cenaDefault'])

 newPranzo = row['pranzo'] >> 1
 if row['pranzoDefault'] != 0:
   newPranzo = newPranzo | (1 << 6)

 newCena = row['cena'] >> 1
 if row['cenaDefault'] != 0:
   newCena = newCena | (1 << 6)

 newDormire = row['dormire'] >> 1
 if row['dormireDefault'] != 0:
  newDormire = newDormire | (1 << 6)

 connection.execute('UPDATE presenza SET pranzo=?, cena=?, dormire=? WHERE id=?', (newPranzo, newCena, newDormire, row['id']))

connection.commit()


connection.close()
