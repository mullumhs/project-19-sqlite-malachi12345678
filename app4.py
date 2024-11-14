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



@app.route('/')

def index():

    movies = Movie.query.all()

    return render_template('index.html', movies=movies)



if __name__ == '__main__':

    app.run(debug=True)