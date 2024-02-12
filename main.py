import mysql.connector

# pip install mysql-connector-python


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="my123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")


###


# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)


###

#mycursor.execute("CREATE TABLE customers2 (name VARCHAR(255), address VARCHAR(255))")


###

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

###

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")


###


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 record inserted, ID:", mycursor.lastrowid)


### SELECT


# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)



### Вибір стовпців


# mycursor.execute("SELECT name, address FROM customers")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


###

# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchone()
#
# print(myresult)


###

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


###

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#
# mycursor.execute(sql, adr)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


###

# sql = "SELECT * FROM customers ORDER BY address DESC, name DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


###

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) deleted")


###

# sql = "UPDATE customers SET address = %s WHERE id = %s"
# val = ("Yellow Garden 2", 10)
#
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) affected")


###

# mycursor.execute("SELECT * FROM customers LIMIT 5")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


###

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)