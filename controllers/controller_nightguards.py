from flask import Flask, request, jsonify
from models.models_nightguards import Nightguard
from app import db

def set_nightguard():

    new_guard = request.get_json()
    o_guard = Nightguard.from_jason(new_guard)
    db.session.add(o_guard)
    db.session.commit()
    return jsonify(o_guard.to_json()), 201

def get_nightguards ():

    nightguard = Nightguard.query.all() 
    return jsonify ([night_guard.to_json() for night_guard in nightguard])
     
def put_nightguards (id):

    update_night_guards = request.get_json()
    o_guard = db.get_or_404(Nightguard,id)
    o_guard.name = update_night_guards.get('name')
    o_guard.vehicle = update_night_guards.get('vehicle')
    o_guard.licenseplate = update_night_guards.get('licenseplate')
    o_guard.dateofbirth = update_night_guards.get('dateofbirth')
    o_guard.formofpayment = update_night_guards.get('formofpayment')
    o_guard.neighborhood = update_night_guards.get('neighborhood')
    db.session.commit()
    return jsonify(o_guard.to_json()),201

def delete_nightguards_by_id (id):

    o_guard = db.get_or_404(Nightguard,id)
    db.session.delete(o_guard)
    db.session.commit()
    return jsonify("DEletado com sucesso"),200

def get_nightguards_by_id (id):

    nightguard = Nightguard.query.first_or_404(id) 
    return jsonify (nightguard.to_json)
