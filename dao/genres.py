from dao.model.genres import Genres


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genres).all()

    def get_one(self, gid):
        return self.session.query(Genres).get(gid)