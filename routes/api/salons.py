from app import app, api, db
from flask import request, Response
from flask_restful import Resource
from models import Salon
from utils.helpers import convert_list


class SalonResource(Resource):

    def get(self):
        salons = Salon.query.all()
        return convert_list(salons)

    def post(self):
        data = request.json
        salon = Salon(name=data['name'], city=data['city'], address=data['address'])
        db.session.add(salon)
        db.session.commit()
        return salon.serialize


class SalonSingleResource(Resource):
    def get(self, id):
        salon = Salon.query.get(id)
        return salon.serialize

    def put(self, id):
        data = request.json
        salon = Salon.query.get(id)
        salon.name = data['name'] if data.get('name', False) else salon.name
        salon.city = data['city'] if data.get('city', False) else salon.city
        salon.address = data['address'] if data.get('address', False) else salon.address
        salon.director_id = data['director_id'] if data.get('director_id', False) else salon.director_id
        db.session.add(salon)
        db.session.commit()
        return salon.serialize

    def delete(self, id):
        salon = Salon.query.get(id)
        db.session.delete(salon)
        db.session.commit()
        return "", 204


class SalonDirectorResource(Resource):
    def get(self, id):
        try:
            salon = Salon.get_by_id(id)
            director = Salon.director(salon['director_id'])
            if director is None:
                return "Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404


api.add_resource(SalonResource, "/api/v1/salons")
api.add_resource(SalonSingleResource, "/api/v1/salons/<int:id>")
api.add_resource(SalonDirectorResource, "/api/v1/salons/<int:id>/director")
