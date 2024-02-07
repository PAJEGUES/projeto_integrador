from flask import Blueprint
from controllers.controller_sectors import set_sectors ,get_sectors_by_id, put_sectors

bp_sectors= Blueprint ("bp_sectors",__name__)

bp_sectors.route("/sectors",methods=["POST"])(set_sectors)

bp_sectors.route("/sectors/<int:id>", methods = ["GET"])(get_sectors_by_id)

bp_sectors.route("/sectors/<int:id>", methods=["PUT"])(put_sectors)






