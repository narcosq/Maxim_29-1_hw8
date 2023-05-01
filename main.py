import sqlite3

conn = sqlite3.connect('company.db')

conn.execute('''CREATE TABLE countries
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL);''')

conn.execute("INSERT INTO countries (title) VALUES ('Kyrgyzstan')")
conn.execute("INSERT INTO countries (title) VALUES ('Germany')")
conn.execute("INSERT INTO countries (title) VALUES ('China')")

conn.execute('''CREATE TABLE cities
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            area REAL DEFAULT 0,
            country_id INTEGER NOT NULL,
            FOREIGN KEY(country_id) REFERENCES countries(id));''')

conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Bishkek', 127, 1)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Talas', 891.8, 2)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Naryn', 16410.54, 3)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Kant', 1270, 4)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Tokmok', 8911.8, 5)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Osh', 164150.54, 6)")
conn.execute("INSERT INTO cities (title, area, country_id) VALUES ('Balykchy', 1227, 7)")


conn.execute('''CREATE TABLE employees
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            city_id INTEGER NOT NULL,
            FOREIGN KEY(city_id) REFERENCES cities(id));''')

conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('John', 'Doe', 1)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Jane', 'Doe', 4)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Max', 'Mustermann', 2)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Anna', 'Musterfrau', 2)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Li', 'Ming', 7)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Keanu', 'Season', 5)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Matthew', 'Parker', 6)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sadyr', 'Japarov', 3)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Valera', 'Kolbaev', 7)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Lil', 'Peep', 2)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Oleg', 'Nechiporenko', 1)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('John', 'Smitt', 6)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Maxim', 'Egorov', 5)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Lera', 'Leontyeva', 7)")
conn.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Chief', 'Keef', 3)")

conn.commit()
conn.close()

print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

for city in cities:
    print(city[0], city[1])

while True:
    city_id = input("Введите id города (для выхода введите 0): ")
    if city_id == '0':
        break


    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT employees.first_name, employees.last_name, countries.title, cities.title
        FROM employees
        INNER JOIN cities ON employees.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    employees = cursor.fetchall()
    conn.close()


    if len(employees) == 0:
        print("Нет сотрудников в данном городе.")
    else:
        print("Сотрудники в выбранном городе:")
        for employee in set(employees):
            print("Имя:", employee[0])
            print("Фамилия:", employee[1])
            print("Страна:", employee[2])
            print("Город:", employee[3])
