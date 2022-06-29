from dao.model.directors import Directors

class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Directors).all()

    def get_one(self, did):
        return self.session.query(Directors).get(did)