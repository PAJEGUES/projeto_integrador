from flask import Blueprint
from controllers.controller_sectors import set_sectors 

bp_sectors= Blueprint ("bp_sectors",__name__)

bp_sectors.route("/sectors",methods=["POST"])(set_sectors)






