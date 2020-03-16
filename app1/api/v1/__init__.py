# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

from flask import Blueprint
from app1.api.v1 import user, book


def create_blueprint_v1():
    bp_v1 = Blueprint("v1", __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1