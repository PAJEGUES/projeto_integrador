from flask import Blueprint
from controllers.controller_sectors import set_sectors , put_sectors, get_sectors, delete_sectors_by_id, get_sectors_by_id

bp_sectors= Blueprint ("bp_sectors",__name__)

bp_sectors.route("/set_sectors",methods=["POST"])(set_sectors)

bp_sectors.route("/get_sector", methods=["GET"]) (get_sectors)

bp_sectors.route ("/get_sector_by_id", methods=["GET"])(get_sectors_by_id)

bp_sectors.route("/put_sectors/<int:id>", methods=["PUT"])(put_sectors)

bp_sectors.route("/del_sectors/<int:id>", methods=["DELETE"])(delete_sectors_by_id)






