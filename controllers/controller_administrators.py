from flask import Flask, request, jsonify
from models.models_administrators import  

administrators = [

    {
        "id": 1,
        "login": "adm",
        "password": "adm"
    }
]

def set_administrators ():

    new_administrator = request.get_json()
            
    if ('login' not in new_administrator) or (new_administrator ['login'] == ""):
        return jsonify ("Erro: o login esta incorreto."), 400
    
    if ('password' not in new_administrator) or (new_administrator ['password'] == ""):
        return jsonify ("Erro: a senha esta incorreto."), 400

    for administrator in administrators:
        if (new_administrator['id'] == administrator['id']):
            return jsonify("Erro, um usuario administrador com esse id ja esta cadastrado!"), 409 

    administrators.append(new_administrator)

    return jsonify(administrators)

def get_administrators_by_id(id):
    i = 0
    for administrator in administrators:
        if(id == administrator["id"]):
            return jsonify(administrators[i])
        
        i+=1

    return ({"Erro": "Administrador não encontrado"}), 404

def put_administrators (id):

    update_administrators = request.get_json()

    i = 0

    for administrator in administrators: 
        if (id == administrator["id"]):
            administrators[i].update(update_administrators)
            return jsonify(update_administrators)
        i+=1
    return jsonify("Erro:administrador não encontrado"), 404

def del_administrators (id):

    i = 0

    for administrator in administrators:
        if(id == administrator["id"]):
            del administrators[i]
            return jsonify(administrators)
    i+=1
    return ("Erro, Administrador não encontrado"), 404

def get_administrators ():

    login = request.args.get("login", None)
    password = request.args.get("password", None)
    page = request.args.get("page", None)
    limit = request.args.get("limit", None)
    id = request.args.get("id", None)

    if id: id = int(id)
    if page: page = int(page)
    if limit: limit = int (limit)

    if page and limit:
        start = limit * (page - 1)
        end = start + limit 

    vector_login = []
    vector_password = []
    vector_id = []


    for administrator in administrators:

        if login and login == administrator ["login"]:
            vector_login.append(administrator)
        elif not login:
            vector_login.append(administrator)

    for administrator in vector_login:

        if password and password == administrator ["password"]:
            vector_password.append(administrator)
        elif not password:
            vector_password.append(administrator)

    for administrator in vector_password:

        if id and id == administrator ["id"]:
            vector_id.append(administrator)
        elif not id:
            vector_id.append(administrator)
    if page and limit:
        return jsonify (vector_id[start:end])  # Os dois pontos indicam "até", nesse caso, retorno do início até o fim 
    else:
        return jsonify (vector_id)
