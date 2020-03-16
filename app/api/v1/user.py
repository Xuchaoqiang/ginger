# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

# redprint
from app.libs.redprint import Redprint

api = Redprint("user")


@api.route("", methods=["POST"])
def create_user():
    pass