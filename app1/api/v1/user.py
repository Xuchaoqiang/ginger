# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

# redprint
from app1.libs.redprint import Redprint

api = Redprint("user")


@api.route("/v1/user/get")
def get_user():
    return 'get_user'