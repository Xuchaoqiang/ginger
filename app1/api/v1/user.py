# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

# blueprint
from flask import Blueprint

user = Blueprint("user", __name__)


@user.route("/v1/user/get")
def get_user():
    return 'get_user'