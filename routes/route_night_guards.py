from flask import Blueprint
from controllers.controller_nightguards import put_nightguards, get_nightguards, delete_nightguards_by_id,get_nightguards_by_id, set_nightguard

bp_night_guards = Blueprint ("bp_night_guards",__name__)

bp_night_guards.route("/post_nightguard", methods=["POST"])(set_nightguard)

bp_night_guards.route("/get_nightguard", methods=["GET"])(get_nightguards)

bp_night_guards.route("/get_nightguards_by_id/<int:id>", methods = ["GET"])(get_nightguards_by_id)

bp_night_guards.route("/put_nightguards/<int:id>",methods=["PUT"])(put_nightguards)

bp_night_guards.route("/del_nightguards/<int:id>", methods=["DELETE"]) (delete_nightguards_by_id)



