# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    return app