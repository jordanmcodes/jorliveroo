import sqlite3


conn = sqlite3.connect("fooddata.db")
cursor = conn.cursor()

cursor.execute ('''CREATE TABLE IF NOT EXISTS fooditems (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                category_id INTEGER
                )''')


cursor.execute (''' CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
                )''')


cursor.execute("INSERT INTO categories (name) VALUES ('Pasta')")
cursor.execute("INSERT INTO categories (name) VALUES ('Pizza')")
cursor.execute("INSERT INTO categories (name) VALUES ('Burgers')")
cursor.execute("INSERT INTO categories (name) VALUES ('Fish')")
cursor.execute("INSERT INTO categories (name) VALUES ('Soup')")
cursor.execute("INSERT INTO categories (name) VALUES ('Sides')")
cursor.execute("INSERT INTO categories (name) VALUES ('Curry')")
cursor.execute("INSERT INTO categories (name) VALUES ('Vegan')")
cursor.execute("INSERT INTO categories (name) VALUES ('Gluten Free')")
cursor.execute("INSERT INTO categories (name) VALUES ('Saver Menu')")
cursor.execute("INSERT INTO categories (name) VALUES ('Desserts')")
cursor.execute("INSERT INTO categories (name) VALUES ('Kids Menu')")

cursor.execute("INSERT INTO fooditems (name, price, category_id) VALUES ('Pepperoni', 12.99, 2)")
cursor.execute("INSERT INTO fooditems (name, price, category_id) VALUES ('Cod', 8.99, 4)")
cursor.execute("INSERT INTO fooditems (name, price, category_id) VALUES ('GF Cheeseburger', 14.99, 9)")









conn.commit()
conn.close()