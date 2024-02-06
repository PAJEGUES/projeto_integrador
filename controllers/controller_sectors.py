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


def put_sectors (id):

    update_sectors = request.get_json()

    i = 0

    for sector in sectors: 
        if (id == sector["id"]):
            sectors[i].update(update_sectors)
            return jsonify(update_sectors)
        i+=1
    return jsonify("Erro: Setor não encontrado"), 404