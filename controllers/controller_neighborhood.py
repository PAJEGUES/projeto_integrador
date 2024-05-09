from flask import Flask, request, jsonify
from models.models_neighborhood import Neighborhood
from app import db

def set_neighborhoods ():

    new_neighborhoods = request.get_json()
    o_neighborhoods = Neighborhood.from_json(new_neighborhoods)
    db.session.add(o_neighborhoods)
    db.session.commit()

    return jsonify(o_neighborhoods.to_json()), 201

def get_neighborhood ():

    neighborhood = Neighborhood.query.all() 
    return jsonify ([neighborhoods.to_json() for neighborhoods in neighborhood])

def put_neighborhoods (id):

    update_neighborhoods= request.get_json()
    o_neighborhoods= db.get_or_404(Neighborhood, id)
    o_neighborhoods.neighborhood_name = update_neighborhoods.get('neighborhood_name')
    o_neighborhoods.sector_name = update_neighborhoods.get('sector_name')
    db.session.commit()

    return jsonify(o_neighborhoods.to_json()), 201

def delete_neighborhoods_by_id (id):

    o_Delneighborhoods = db.get_or_404(Neighborhood, id)
    db.session.delete(o_Delneighborhoods)
    db.session.commit()

    return jsonify ("Deletado com sucesso"),200

def get_neighborhoods_by_id (id):

    neighborhood = Neighborhood.query.first_or_404(id) 
    return jsonify (neighborhood.to_json())