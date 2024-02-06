from flask import Flask, request, jsonify

neighborhoods = [
    {
        "id": 1,
        "neighborhood_name": "Maria Estella Faga",
        "sector_name": "Setor 1"
    }
]

def get_neighborhoods_by_id (id):

    i = 0
    for neighborhood in neighborhoods:
        if(id == neighborhood["id"]):
            return jsonify(neighborhoods[i])
        i+=1
    return ("Erro, Bairro não encontrado"), 404