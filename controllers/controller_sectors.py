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