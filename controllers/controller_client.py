from flask import Flask, request, jsonify
from models.models_client import Client
from app import db 


def set_client ():

    new_client = request.get_json()
    o_SetClient = Client.from_json(new_client)
    db.session.add(o_SetClient)
    db.session.commit()
    return jsonify(o_SetClient.to_json()), 201     

def get_client():

    client = Client.query.all()
    return jsonify ([clients.to_json() for clients in client])

def put_client (id):

    update_client = request.get_json()
    o_PutClient = db.get_or_404(Client, id)
    o_PutClient.name = update_client.get('name')
    o_PutClient.address = update_client.get('address')
    o_PutClient.housenumber = update_client.get('housenumber')
    o_PutClient.neighborhood = update_client.get('neighborhood')
    o_PutClient.telephone = update_client.get('telephone')
    o_PutClient.paymentamount = update_client.get('paymentamount')
    o_PutClient.dateofpayment = update_client.get('dateofpayment')
    o_PutClient.formofpayment = update_client.get('formofpayment')
    db.session.commit()
    return jsonify(o_PutClient.to_json()), 201
    

def del_client (id):

    o_DelClient = db.get_or_404(Client, id)
    db.session.delete(o_DelClient)
    db.session.commit()
    return jsonify ("Cliente deletado com sucesso!"),200

def get_client_by_id (id):

    client = Client.query.get_or_404(id) 
    return jsonify (client.to_json())