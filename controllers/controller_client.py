from flask import Flask, request, jsonify
from models.models_client import Client
from app import db 


def set_client ():

    new_client = request.get_json()

    o_SetClient = Client.from_json(new_client)
    db.session.add(o_SetClient)
    db.session.commit()

    return jsonify(o_SetClient.to_json()), 201
            

def get_client(id):

    return ({"Erro": "Cliente não encontrado"}), 404

def put_client (id):

    update_client = request.get_json()

    o_PutClient = db.get_or_404(Client, id)

    o_PutClient.name = update_client.get('name')
    o_PutClient.road = update_client.get('road')
    o_PutClient.number = update_client.get('number')
    o_PutClient.neighborhood = update_client.get('neighborhood')
    o_PutClient.contact = update_client.get('contact')
    o_PutClient.paymentamount = update_client.get('paymentamount')
    o_PutClient.dateofbirth = update_client.get('dateofbirth')
    o_PutClient.formofpayment = update_client.get('formofpayment')

    db.session.commit

    return jsonify(o_PutClient.to_json()), 201
    

def del_client (id):

    o_DelClient = db.get_or_404(Client, id)

    db.session.delete(o_DelClient)
    db.session.commit()

    return jsonify ("Deletado com sucesso"),200