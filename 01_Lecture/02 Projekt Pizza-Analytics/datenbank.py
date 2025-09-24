
# %%
import sqlite3


# %%
conn = sqlite3.connect('oth-gp-pizza.db')
cursor = conn.cursor()


# %%
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pizzen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        zutaten TEXT NOT NULL,
        preis REAL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS kunden (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vorname TEXT NOT NULL,
        name TEXT NOT NULL,
        strasse TEXT NOT NULL,
        hausnummer TEXT NOT NULL,
        plz TEXT NOT NULL,
        stadt TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bestellungen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kunde_id INTEGER NOT NULL,
        pizza_id INTEGER NOT NULL,
        menge INTEGER NOT NULL,
        bestellzeitpunkt TEXT NOT NULL,
        FOREIGN KEY (kunde_id) REFERENCES kunden(rowid),
        FOREIGN KEY (pizza_id) REFERENCES pizzen(rowid)
    )
''')

conn.commit()


# %%
cursor.execute('''
    INSERT INTO pizzen (name, zutaten, preis) VALUES
        ('Margherita', 'Tomaten, Käse, Basilikum', 7.50),
        ('Salami', 'Tomaten, Käse, Salami', 8.50),
        ('Hawaii', 'Tomaten, Käse, Schinken, Ananas', 9.00),
        ('Funghi', 'Tomaten, Käse, Pilze', 8.00),
        ('Prosciutto', 'Tomaten, Käse, Schinken', 8.50),
        ('Diavola', 'Tomaten, Käse, scharfe Salami', 9.50),
        ('Quattro Stagioni', 'Tomaten, Käse, Schinken, Artischocken, Pilze', 10.00),
        ('Tonno', 'Tomaten, Käse, Thunfisch, Zwiebeln', 9.50),
        ('Calzone', 'Tomaten, Käse, Schinken, Salami', 10.50),
        ('Vegetariana', 'Tomaten, Käse, Gemüse', 9.00);

''')

cursor.execute('''
    INSERT INTO kunden (vorname, name, strasse, hausnummer, plz, stadt) VALUES
        ('Max', 'Mustermann', 'Musterstraße', '1', '12345', 'Musterstadt'),
        ('Anna', 'Müller', 'Müllerstraße', '2', '54321', 'Müllerburg'),
        ('Peter', 'Schmidt', 'Schmidtweg', '3', '56789', 'Schmidthausen'),
        ('Julia', 'Meier', 'Meierstraße', '4', '67890', 'Regensburg'),
        ('Stefan', 'Fischer', 'Fischerweg', '5', '93047', 'Regensburg'),
        ('Claudia', 'Schneider', 'Schneiderstraße', '6', '93049', 'Regensburg'),
        ('Thomas', 'Wagner', 'Wagnergasse', '7', '33333', 'Wagnerstadt'),
        ('Laura', 'Weber', 'Webergasse', '8', '44444', 'Weberburg'),
        ('Michael', 'Becker', 'Beckerstraße', '9', '93053', 'Regensburg'),
        ('Sarah', 'Koch', 'Kochstraße', '10', '66666', 'Kochdorf'),
        ('Lukas', 'Richter', 'Richterstraße', '11', '93055', 'Regensburg'),
        ('Lea', 'Bauer', 'Bauerweg', '12', '88888', 'Bauerburg'),
        ('David', 'Hoffmann', 'Hoffmannstraße', '13', '93047', 'Regensburg'),
        ('Sophia', 'Schulz', 'Schulzstraße', '14', '10101', 'Schulzdorf'),
        ('Paul', 'Klein', 'Kleingasse', '15', '12121', 'Kleinburg'),
        ('Emily', 'Wolf', 'Wolfstraße', '16', '13131', 'Wolfshausen'),
        ('Jan', 'Neumann', 'Neumannweg', '17', '93053', 'Regensburg'),
        ('Emma', 'Zimmermann', 'Zimmermannstraße', '18', '15151', 'Zimmermannburg'),
        ('Oliver', 'Braun', 'Braunweg', '19', '93055', 'Regensburg'),
        ('Lena', 'Hartmann', 'Hartmannstraße', '20', '17171', 'Hartmanndorf');
''')

cursor.execute('''
    INSERT INTO bestellungen (kunde_id, pizza_id, menge, bestellzeitpunkt) VALUES
        (1, 1, 2, '2024-12-01 12:30:00'),
        (2, 3, 1, '2024-12-01 13:00:00'),
        (3, 5, 1, '2024-12-01 13:15:00'),
        (4, 2, 3, '2024-12-01 14:00:00'),
        (5, 6, 2, '2024-12-01 14:30:00'),
        (6, 4, 1, '2024-12-01 15:00:00'),
        (7, 7, 1, '2024-12-01 15:30:00'),
        (8, 9, 2, '2024-12-01 16:00:00'),
        (9, 8, 1, '2024-12-01 16:30:00'),
        (10, 10, 1, '2024-12-01 17:00:00');

''')

conn.commit()


# %%
conn.close()


# %%
