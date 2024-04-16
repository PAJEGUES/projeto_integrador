from flask import Flask, request, jsonify
from app import db
from models.models_sector import Sector

sectors = [
    {
        "id": 1,
        "nightguard_name": "Jose",
        "sector_name": "Setor 1"
    },

    {
        "id": 2,
        "nightguard_name": "Alef",
        "sector_name": "Setor 2"
    },

    {
        "id": 3,
        "nightguard_name": "Rogerio",
        "sector_name": "Setor 3"
    },

    {
        "id": 4,
        "nightguard_name": "Vinicius",
        "sector_name": "Setor 4"
    },
    
]

#def get_sectors ():
    #nightguard_name = request.args.get("nightguard_name", None)
    #sector_name = request.args.get("sector_name", None)
    #id = request.args.get("id", None)

    #page = request.args.get("page", None)
    #limit = request.args.get("limit", None)
 
    #if id: id = int(id)
    #if page: page = int(page)
    #if limit: limit = int (limit)

    if page and limit:
        start = limit * (page - 1) 
        end = start + limit
 
    #vector_sector_name = []
    #vector_nightguard_name = []
    #vector_id = []
 #
 #
 #   #for sector in sectors:
 #
 #       if nightguard_name and nightguard_name == sector ["nightguard_name"]:
 #           vector_nightguard_name.append(sector)
 #       elif not nightguard_name:
 #           vector_nightguard_name.append(sector)
 #
 #   for sector in vector_nightguard_name:
 #
 #       if sector_name and sector_name == sector ["sector_name"]:
 #           vector_sector_name.append(sector)
 #       elif not sector_name:
 #           vector_sector_name.append(sector)
 #
 #   for sector in vector_sector_name:
 #
 #       if id and id == sector ["id"]:
 #           vector_id.append(sector)
 #       elif not id:
 #           vector_id.append(sector)
 #
 #   if page and limit:
 #       return jsonify (vector_id[start:end])
 #   else: 
 #       return jsonify (vector_id)
 #   
 #   
## rota POST

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

