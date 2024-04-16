from flask import Flask, request, jsonify
from models.model_neightguards import guard
from app import db


def set_neightguard():

    new_guard = request.get_json()

    o_guard = guard.from_jason(new_guard)
    db.session.add(o_guard)
    db.session.commit()
    
    return jsonify(o_guard.to_jason()), 201

def get_nightguards ():

    neightguard = guard.query.all() 
    return jsonify ([neight_guard.to_jason() for neight_guard in neightguard])
     

def put_night_guards (id):

    update_night_guards = request.get_json()
    o_guard = db.get_or_404(guard,id)

    o_guard.name = update_night_guards.get('name')
    o_guard.vehicle = update_night_guards.get('vehicle')
    o_guard.licenseplate = update_night_guards.get('licenseplate')
    o_guard.dateofbirth = update_night_guards.get('dateofbirth')
    o_guard.formofpayment = update_night_guards.get('formofpayment')
    o_guard.neighborhood = update_night_guards.get('neighborhood')

    db.session.commit()
    return jsonify(o_guard.to_json()),201

def delete_night_guards_by_id (id):

    o_guard = db.get_or_404(guard,id)
    
    db.session.delte(o_guard)
    db.session.commit()
    return jsonify("DEletado com sucesso"),200
 
    

def get_night_guards_by_id (id):

    neightguard = guard.query.all(id) 
    return jsonify ([neight_guard.to_jason() for neight_guard in neightguard])
    


