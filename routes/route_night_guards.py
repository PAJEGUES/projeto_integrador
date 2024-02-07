from flask import Blueprint
from controllers.controller_nightguards import put_night_guards, get_nightguards, post_nightguards, delete_night_guards_by_id

bp_night_guards = Blueprint ("bp_night_guards",__name__)

# Rota POST Nightguard
bp_night_guards.route("/post_nightguard", methods=["POST"])(post_nightguards)

bp_night_guards.route("/night_guards/<int:id>",methods=["PUT"])(put_night_guards)

bp_night_guards.route("/get_nightguard", methods=["GET"])(get_nightguards)

bp_night_guards.route("/night_guards/<int:id>", methods=["DELETE"]) (delete_night_guards_by_id)

