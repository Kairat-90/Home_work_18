from flask_restx import Resource, Namespace
from dao.model.genres import GenresSchema
from implemented import genres_service

genres_ns = Namespace('genres')

genre_schema = GenresSchema()
genres_schema = GenresSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genres_service.get_all()
        return genres_schema.dump(all_genres), 200

@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid: int):
        try:
            genre = genres_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404