from flask import Blueprint
from controllers.controller_administrators import get_administrators_by_id, set_administrators, put_administrators, del_administrators, get_administrators 

bp_administrators= Blueprint ("bp_administrators",__name__)

bp_administrators.route("/post_administrators", methods=["POST"])(set_administrators)

bp_administrators.route("/get_administrators", methods=["GET"])(get_administrators) 

bp_administrators.route("/get_administrators_by_id/<int:id>",methods=["GET"])(get_administrators_by_id)

bp_administrators.route("/put_administrators/<int:id>", methods=["PUT"])(put_administrators)

bp_administrators.route("/del_administrators/<int:id>", methods = ["DELETE"])(del_administrators)



