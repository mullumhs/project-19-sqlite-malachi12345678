from flask import Flask, render_template, request, redirect, url_for

import sqlite3



app = Flask(__name__)


#connects to db
def get_db_connection():

    conn = sqlite3.connect('movies2.db')

    return conn


#returns table of all movies
@app.route('/')

def index():

    conn = get_db_connection()

    conn.row_factory = sqlite3.Row

    movies = conn.execute('SELECT * FROM movies').fetchall()

    conn.close()

    return render_template('index.html', movies=movies)






@app.route('/add', methods=['GET', 'POST'])

def add_movie():
    # On a form submission (POST)

    if request.method == 'POST':

        title = request.form['title']

        director = request.form['director']

        year = int(request.form['year'])

        rating = float(request.form['rating'])

        

        conn = get_db_connection()

        conn.execute('INSERT INTO movies (title, director, year, rating) VALUES (?, ?, ?, ?)',

                     (title, director, year, rating))

        conn.commit()

        conn.close()

        return redirect(url_for('index'))

    
    # On visiting the page (GET)

    return render_template('add.html')



if __name__ == '__main__':

    app.run(debug=True)