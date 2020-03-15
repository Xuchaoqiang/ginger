# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from flask import Flask


def register_blueprints(app):
    from app1.api.v1.user import user
    from app1.api.v1.book import book
    app.register_blueprint(user)
    app.register_blueprint(book)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app1.config.setting')
    app.config.from_object('app1.config.secure')
    register_blueprints(app)
    return app