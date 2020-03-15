# -*- coding:utf-8 -*-
# @Author :xuchaoqiang


# blueprint
from flask import Blueprint

book = Blueprint("book", __name__)


@book.route('/v1/book/get')
def get_book():
    return "get_book"


@book.route("/v1/book/create")
def create_book():
    return "create book"