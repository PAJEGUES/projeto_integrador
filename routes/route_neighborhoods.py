from flask import Blueprint
from controllers.controller_neighborhoods import delete_neighborhoods_by_id

bp_neighborhoods = Blueprint ("bp_neighborhoods",__name__)

bp_neighborhoods.route("/neighborhoods",methods=["DELETE"])(delete_neighborhoods_by_id)