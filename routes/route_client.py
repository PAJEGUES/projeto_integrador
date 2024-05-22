from flask import Blueprint
from controllers.controller_client import set_client, put_client, del_client, get_client 

bp_client= Blueprint ("bp_client",__name__)

bp_client.route("/post_client", methods=["POST"])(set_client)

bp_client.route("/get_client", methods=["GET"])(get_client) 

bp_client.route("/put_client/<int:id>", methods=["PUT"])(put_client)

bp_client.route("/del_client/<int:id>", methods = ["DELETE"])(del_client)
