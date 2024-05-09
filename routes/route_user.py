from flask import Blueprint
from controllers.controller_user import login_user, set_user

bp_users= Blueprint ("bp_users",__name__)

bp_users.route("/login", methods=["POST"])(login_user)

bp_users.route("/register", methods=["POST"])(set_user)


