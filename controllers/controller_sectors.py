from flask import Flask, request, jsonify

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

def get_sectors ():
    nightguard_name = request.args.get("nightguard_name", None)
    sector_name = request.args.get("sector_name", None)
    id = request.args.get("id", None)

    page = request.args.get("page", None)
    limit = request.args.get("limit", None)
 
    if id: id = int(id)
    if page: page = int(page)
    if limit: limit = int (limit)

    if page and limit:
        start = limit * (page - 1)
        end = start + limit
 
    vector_sector_name = []
    vector_nightguard_name = []
    vector_id = []
 
 
    for sector in sectors:
 
        if nightguard_name and nightguard_name == sector ["nightguard_name"]:
            vector_nightguard_name.append(sector)
        elif not nightguard_name:
            vector_nightguard_name.append(sector)
 
    for sector in vector_nightguard_name:
 
        if sector_name and sector_name == sector ["sector_name"]:
            vector_sector_name.append(sector)
        elif not sector_name:
            vector_sector_name.append(sector)
 
    for sector in vector_sector_name:
 
        if id and id == sector ["id"]:
            vector_id.append(sector)
        elif not id:
            vector_id.append(sector)
 
    if page and limit:
        return jsonify (vector_id[start:end])
    else: 
        return jsonify (vector_id)

def set_sectors ():

    new_sector = request.get_json()

    if ('nightguard_id' not in new_sector) or (not new_sector['nightguard_id']):
          return jsonify({"error":"Não tem nightguard_id"}), 400
    
    for sector in sectors:
        if (new_sector['id'] == sector['id']):
            return jsonify("Erro, um setor com esse id ja esta cadastrado!"), 409 

    sectors.append(new_sector)

    return jsonify(sectors)


def put_sectors (id):

    update_sectors = request.get_json()

    i = 0

    for sector in sectors: 
        if (id == sector["id"]):
            sectors[i].update(update_sectors)
            return jsonify(update_sectors)
        i+=1
    return jsonify("Erro: Setor não encontrado"), 404

def get_sectors_by_id (id):

    i = 0
    for sector in sectors:
        if(id == sector["id"]):
            return jsonify(sectors[i])
        i+=1
    return ("Erro, Setor não encontrado"), 404

def delete_sectors_by_id (id):
 
    i = 0
    for sector in sectors:
        if(id == sector["id"]):
            del sectors[i]
            return jsonify(sectors)
        i+=1
    return ("Erro, Setor não encontrado"), 404