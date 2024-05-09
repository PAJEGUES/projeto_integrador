from flask import Flask, request, jsonify
from models.models_administrators import Administrator
from app import db 

def set_administrators ():

    new_administrator = request.get_json()
    o_SetAdministrators = Administrator.from_json(new_administrator)
    db.session.add(o_SetAdministrators)
    db.session.commit()
    return jsonify(o_SetAdministrators.to_json()), 201
            

def get_administrators_by_id(id):

    administrator = Administrator.query.first_or_404(id)
    return jsonify(administrator.to_json())

def put_administrators (id):

    update_administrators = request.get_json()
    o_PutAdministrators = db.get_or_404(Administrator, id)
    o_PutAdministrators.login = update_administrators.get('login')
    o_PutAdministrators.password = update_administrators.get('password')
    db.session.commit
    return jsonify(o_PutAdministrators.to_json()), 201
    

def del_administrators (id):

    o_DelAdministrators = db.get_or_404(Administrator, id)
    db.session.delete(o_DelAdministrators)
    db.session.commit()
    return jsonify ("Deletado com sucesso"),200
    
def get_administrators ():

    administrators = Administrator.query.all()
    return jsonify ([administrator.to_json() for administrator in administrators])


