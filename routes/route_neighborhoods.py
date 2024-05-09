from flask import Blueprint
from controllers.controller_neighborhood import get_neighborhood, delete_neighborhoods_by_id, set_neighborhoods, put_neighborhoods, get_neighborhoods_by_id

bp_neighborhoods = Blueprint ("bp_neighborhoods",__name__)

bp_neighborhoods.route("/post_neighborhoods", methods=["POST"]) (set_neighborhoods)

bp_neighborhoods.route("/get_neighborhood", methods=["GET"])(get_neighborhood)

bp_neighborhoods.route("/get_neighborhoods_by_id/<int:id>", methods = ["GET"])(get_neighborhoods_by_id)

bp_neighborhoods.route("/put_neighborhoods/<int:id>", methods=["PUT"])(put_neighborhoods)

bp_neighborhoods.route("/del_neighborhoods",methods=["DELETE"])(delete_neighborhoods_by_id)





