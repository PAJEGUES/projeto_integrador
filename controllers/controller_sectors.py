from flask import Flask, request, jsonify
from app import db
from models.models_sector import Sector

def set_sectors():
    Model_sector= request.get_json()
    o_sector = Sector.from_json(Model_sector)
    db.session.add(o_sector)
    db.session.commit()
    return jsonify(o_sector.to_json())

def get_sectors ():
    sector = Sector.query.all()
    return jsonify ([sectors.to_json() for sectors in sector])

def get_sectors_by_id(id):
    sectors = Sector.query.first_or_404(id)
    return jsonify(sectors.to_json())

def delete_sectors_by_id(id):

    sectors = Sector.query.first_or_404(id)
    return jsonify(sectors.to_json())

def put_sectors (id):

    update_sectors = request.get_json()
    o_sectors = db.get_or_404(Sector, id)
    o_sectors.night_guard = update_sectors.get('night_guard')
    o_sectors.neighborhood =update_sectors.get('neighborhood')
    db.session.commit()
    return jsonify(o_sectors.to_json()), 201

