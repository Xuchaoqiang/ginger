# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    """
    封装flask的jsonencoder，重写default方法
    o为一个对象，
        o对象需定义一个keys方法，返回一个可迭代对象，对面的值为需要暴露出去的属性名
        o对象需定义__getitem__方法， 当o["xx"]的时候回去执行此方法
        dict函数内部回去拿到这个keys的返回值， 比如keys的返回值为["name", "age"]
        然后就会生成一个可序列化的字典
            {"name": o.__getitem__("name"), "age": o.__getitem__("age")}
    """
    def default(self, o):
        if hasattr(o, "keys") and hasattr(o, "__getitem__"):
            return dict(o)
        if isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder()
