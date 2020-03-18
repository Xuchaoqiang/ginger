# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

# redprint
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint("user")


@api.route("/<int:uid>", methods=["GET"])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route("/<int:uid>", methods=["DELETE"])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()