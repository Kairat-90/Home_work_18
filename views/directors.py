from flask_restx import Resource, Namespace
from dao.model.directors import DirectorsSchema
from implemented import directors_service

directors_ns = Namespace('directors')

director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = directors_service.get_all()
        return directors_schema.dump(all_directors), 200

@directors_ns.route('/<int:did>')
class DirectorsView(Resource):
    def get(self, did: int):
        try:
            director = directors_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404