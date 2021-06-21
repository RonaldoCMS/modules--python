import mysql.connector as mysql

def executeQuery(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    print('Operation complete!')

def insertPerson(connection, name, surname, age):
    query = "INSERT INTO person (name, surname, age) values (\"{}\", \"{}\", \"{}\")".format(name, surname, age)
    executeQuery(connection, query)

def updatePerson(connection, name, surname, age, id):
    query = "UPDATE person SET name = \"{}\", surname = \"{}\", age = \"{}\" WHERE id = {}".format(name, surname, age, id)
    executeQuery(connection, query)

def selectPeople(connection):
    query = "SELECT * FROM person"
    cursor = connection.cursor()
    cursor.execute(query)
    myresult = cursor.fetchall()
    for id, name, surname, age in myresult:
        print("id: {}\t {} {} {}".format(id, name, surname, age))

if __name__ == '__main__':
    config = {
        "host":"127.0.0.1",
        "port":3306,
        "user": "root",
        "database": "pydb",
        "password": "" 
    }

    connection = mysql.connect(**config)
    selectPeople(connection)
    #insertPerson(connection, "Giovanni", "Pascoli", 22)
    #updatePerson(connection, "paolo", "cannone", 35, 4)


