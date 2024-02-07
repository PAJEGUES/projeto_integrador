from flask import Flask, request, jsonify

neighborhoods = [
    {
        "id": 1,
        "neighborhood_name": "Maria Estella Faga",
        "sector_name": "Setor 1"
    }
]

def get_neighborhood ():

    neighborhood_name = request.args.get("neighborhood_name", None)
    sector_name = request.args.get("sector_name", None)
    page = request.args.get("page", None)
    limit = request.args.get("limit", None)

    if page: page = int(page)
    if limit: limit = int(limit)

    if page and limit:
        start = limit * (page - 1)
        end = start + limit 


    vector_neighborhood = []
    vector_sectorname = []

    for neighborhood in neighborhoods:
        if neighborhood_name and neighborhood_name == neighborhood ["neighborhood_name"]:
            vector_neighborhood.append(neighborhood)
        elif not neighborhood_name:
            vector_neighborhood.append(neighborhood)

    for neighborhood in vector_neighborhood:
        if sector_name and sector_name == neighborhood ["sector_name"]:
            vector_sectorname.append(neighborhood)
        elif not sector_name:        
            vector_sectorname.append(neighborhood)
    
    if page and limit:
        return jsonify (vector_sectorname[start:end]) 
    else:
        return jsonify (vector_sectorname)

def get_neighborhoods_by_id (id):

    i = 0
    for neighborhood in neighborhoods:
        if(id == neighborhood["id"]):
            return jsonify(neighborhoods[i])
        i+=1
    return ("Erro, Bairro não encontrado"), 404


def delete_neighborhoods_by_id (id):

    i = 0
    for neighborhood in neighborhoods:
        if(id == neighborhood["id"]):
            del neighborhoods[i]
            return jsonify(neighborhoods)
        i+=1
    return ("Erro, Bairro não encontrado"), 404
