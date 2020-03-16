# -*- coding:utf-8 -*-
# @Author :xuchaoqiang


# redprint
from app.libs.redprint import Redprint

api = Redprint("book")


@api.route('/v1/book/get')
def get_book():
    return "get_book"


@api.route("/v1/book/create")
def create_book():
    return "create book"