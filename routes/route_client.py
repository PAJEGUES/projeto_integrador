from flask import Blueprint
from controllers.controller_client import set_client, put_client, del_client, get_client 

bp_client= Blueprint ("bp_client",__name__)

bp_client.route("/client", methods=["POST"])(set_client)

bp_client.route("/client", methods=["GET"])(get_client) 

bp_client.route("/client/<int:id>", methods=["PUT"])(put_client)

bp_client.route("/client/<int:id>", methods = ["DELETE"])(del_client)
