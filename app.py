import sqlite3



conn = sqlite3.connect('movies.db')
cursor = conn.cursor()


cursor.execute('''

CREATE TABLE IF NOT EXISTS movies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    director TEXT,

    year INTEGER,

    rating FLOAT

)

''')

movies = [

    ('The Shawshank Redemption', 'Frank Darabont', 1994, 9.3),

    ('Inception', 'Christopher Nolan', 2010, 8.8),

    ('The Matrix', 'Lana and Lilly Wachowski', 1999, 8.7),

    ('Interstellar', 'Christopher Nolan', 2014, 8.6)

]



#Insert movies

cursor.executemany('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', movies)

#print all
cursor.execute('SELECT * FROM movies')

all_movies = cursor.fetchall()

print("All movies:")

for movie in all_movies:

    print(movie)

#prints ratings > 9
cursor.execute('''
SELECT title FROM movies WHERE rating > 9 
               ''')

high_rated = cursor.fetchall()
print("high_rated:")
for title in high_rated:
    print(title)

userinput = input("enter d to delete all ")
if userinput == "d":
    cursor.execute('DROP TABLE movies')
conn.commit()
conn.close()

