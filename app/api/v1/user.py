# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

# redprint
from app.libs.redprint import Redprint
from app.libs.token_auth import auth

api = Redprint("user")


@api.route("", methods=["GET"])
@auth.login_required
def get_user():
    return "test"