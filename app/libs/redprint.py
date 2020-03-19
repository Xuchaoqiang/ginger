# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

"""
自定义红图为了优化两个问题：
1.对于book视图函数来说 '/v1/book/get', '/v1/book/create' 前面的'/v1/book/'都是重复的
2.flask提供的blueprint不是用来拆分试图函数的，而是用来拆分模块级别的
"""

class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)