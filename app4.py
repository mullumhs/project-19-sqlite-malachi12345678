from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies2.db'

db = SQLAlchemy(app)



class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    director = db.Column(db.String(100))

    year = db.Column(db.Integer)

    rating = db.Column(db.Float)



with app.app_context():

    db.create_all()


#table display
@app.route('/')

def index():

    movies = Movie.query.all()

    return render_template('index.html', movies=movies)



#add movie
@app.route('/add', methods=['GET', 'POST'])

def add_movie():

    if request.method == 'POST':

        new_movie = Movie(

            title=request.form['title'],

            director=request.form['director'],

            year=int(request.form['year']),

            rating=float(request.form['rating'])

        )

        db.session.add(new_movie)

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')


#update
@app.route('/edit/<int:id>', methods=['GET', 'POST'])

def edit_movie(id):

    movie = Movie.query.get_or_404(id)

    if request.method == 'POST':

        movie.title = request.form['title']

        movie.director = request.form['director']

        movie.year = int(request.form['year'])

        movie.rating = float(request.form['rating'])

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)

#delete
@app.route('/delete/<int:id>')

def delete_movie(id):

    movie = Movie.query.get_or_404(id)

    db.session.delete(movie)

    db.session.commit()

    return redirect(url_for('index'))

#search
@app.route('/search')

def search():

    if request.method == 'POST':

        query = request.form['title']


    movies = db.session.query(movies.title).filter(title = query).all()

    return render_template('search.html', movies=movies, query=query)









if __name__ == '__main__':

    app.run(debug=True)

