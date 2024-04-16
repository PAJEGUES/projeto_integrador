from flask import Flask, request, jsonify
from app import db
from models.models_sector import Sector
    
# rota POST
def set_sectors():
    Model_sector= request.get_json()

    o_sector = Model_sector.from_json(Model_sector)
    db.session.add(o_sector)
    db.session.commit()

    return jsonify(o_sector.to_json())

# rota GET
def get_sectors ():
    sectors = Sector.query.all()

    return jsonify ([Sector.to_json()for sector in sectors])


# ROTA Delete 

    return jsonify ("Setor deletado com sucesso"),200

# rota PUT
def put_sectors (night_guard,neighborhood):

    update_sectors = request.get_json()

    o_sectors = db.get_or_404(Sector, night_guard, neighborhood)

    o_sectors.night_guard = update_sectors.get('night_guard')
    o_sectors.neighborhood =update_sectors.get('neighborhood')

    db.session.commit

    return jsonify(o_sectors.to_json()), 201

