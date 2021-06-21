import mysql.connector as mysql

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connect(**config)


query = ("INSERT INTO Person (name, surname, age) values ({}, {}, {})").format("'Giovanni'", "'Rossi'", "'18'")
cursor = cnx.cursor()
print(query)

i = 0
while i < 10:
    print("")
    i+=1

cursor.execute(query)
cnx.commit()

query = ("SELECT name, surname, age from Person")

cursor.execute(query)


for name, surname, age in cursor:
    print("My name's {} {} and I {} years old.".format(name, surname, age))

cursor.close()
cnx.close()