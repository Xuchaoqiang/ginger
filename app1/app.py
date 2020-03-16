# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from flask import Flask


def register_blueprints(app):
    from app1.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix="/v1")


def create_app():
    app = Flask(__name__)
    app.config.from_object('app1.config.setting')
    app.config.from_object('app1.config.secure')
    register_blueprints(app)
    return app