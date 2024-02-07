from flask import Blueprint
from controllers.controller_night_guards import put_night_guards

bp_night_guards = Blueprint ("bp_night_guards",__name__)

bp_night_guards.route("/night_guards/<int:id>",methods=["PUT"])(put_night_guards)