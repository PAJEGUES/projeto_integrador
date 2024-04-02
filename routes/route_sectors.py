from flask import Blueprint
from controllers.controller_sectors import set_sectors , put_sectors, get_sectors,delete_sectors_by_id

bp_sectors= Blueprint ("bp_sectors",__name__)

bp_sectors.route("/sectors",methods=["POST"])(set_sectors)

#bp_sectors.route("/sectors/<int:id>", methods = ["GET"])(get_sectors_by_id)

bp_sectors.route("/sectors/<int:id>", methods=["PUT"])(put_sectors)

bp_sectors.route("/sector", methods=["GET"]) (get_sectors)

bp_sectors.route("/sectors/<int:id>", methods=["DELETE"])(delete_sectors_by_id)






