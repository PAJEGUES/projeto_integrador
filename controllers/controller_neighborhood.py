from flask import Flask, request, jsonify
from app import db

neighborhoods = [
    {
        "id": 1,
        "neighborhood_name": "Maria Estella Faga",
        "sector_name": "Setor 1"
    }
]

## Rota POST Bairros 

def set_neighborhoods ():

    new_neighborhoods = request.get_json()

    o_neighborhoods = neighborhoods.from_json(new_neighborhoods)
    db.session.add(o_neighborhoods)
    db.session.commit()

    return jsonify(o_neighborhoods.to_json()), 201


#ROTA GET
def get_neighborhood (id):

    i = 0
    for neighborhood in neighborhoods:
        if(id == neighborhood["id"]):
            return jsonify(neighborhoods[i])
        i+=1
    return ("Erro, Bairro não encontrado"), 404


#ROTA PUT
def put_neighborhoods (id):

    update_neighborhoods= request.get_json()

    o_Putneighborhoods= db.get_or_404(neighborhoods, id)

    db.session.commit

    return jsonify(o_Putneighborhoods.to_json()), 201



#ROTA DELETE
def delete_neighborhoods_by_id (id):

    o_Delneighborhoods = db.get_or_404(neighborhoods, id)

    db.session.delete(o_Delneighborhoods)
    db.session.commit()

    return jsonify ("Deletado com sucesso"),200