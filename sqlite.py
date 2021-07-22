import sqlite3
connection = sqlite3.connect("C:/Users/haile/Documents/GitHub/Python_Projects/test-database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, AGE INT)")
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
connection.commit()



