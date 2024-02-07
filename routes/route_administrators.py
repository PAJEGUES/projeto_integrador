from flask import Blueprint
from controllers.controller_administrators import get_administrators_by_id

bp_administrators= Blueprint ("bp_administrators",__name__)

bp_administrators.route("/administrators/<int:id>",methods=["GET"])(get_administrators_by_id)