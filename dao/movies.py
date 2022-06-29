from dao.model.movies import Movies


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movies).all()

    def get_one(self, mid):
        return self.session.query(Movies).get(mid)

    def get_by_year(self, year):
        movie = Movies.query.filter(Movies.year == year)
        return movie

    def get_by_genre(self, genre_id):
        movie = Movies.query.filter(Movies.genre_id == genre_id)
        return movie

    def get_by_director(self, director_id):
        movie = Movies.query.filter(Movies.director_id == director_id)
        return movie

    def create(self, data):
        movies = Movies(**data)

        self.session.add(movies)
        self.session.commit()
        self.session.close()


    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
        self.session.close()

