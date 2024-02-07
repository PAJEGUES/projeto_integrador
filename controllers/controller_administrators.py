from flask import Flask, request, jsonify

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

def del_administrators (id):

    i = 0

    for administrator in administrators:
        if(id == administrator["id"]):
            del administrators[i]
            return jsonify(administrators)
    i+=1
    return ("Erro, Administrador não encontrado"), 404

def get_administrators_by_id(id):
    i = 0
    for administrator in administrators:
        if(id == administrator["id"]):
            return jsonify(administrators[i])
        
        i+=1

    return ({"Erro": "Administrador não encontrado"}), 404

