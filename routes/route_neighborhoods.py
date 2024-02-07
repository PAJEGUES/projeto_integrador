from flask import Blueprint
from controllers.controller_neighborhood import get_neighborhood, get_neighborhoods_by_id, delete_neighborhoods_by_id, set_neighborhoods

bp_neighborhoods = Blueprint ("bp_neighborhoods",__name__)

bp_neighborhoods.route("/get_neighborhood", methods=["GET"])(get_neighborhood)

bp_neighborhoods.route("/neighborhoods/<int:id>", methods = ["GET"])(get_neighborhoods_by_id)

bp_neighborhoods.route("/neighborhoods",methods=["DELETE"])(delete_neighborhoods_by_id)

bp_neighborhoods.route("/neighborhoods", methods=["POST"]) (set_neighborhoods)

