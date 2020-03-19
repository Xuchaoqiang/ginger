# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

"""
权限控制scope思路
1.应该在哪里进行权限校验？为什么？
    AOP思想(面向切片)：在程序运行、编译时，动态的在某一个地方加上一段代码。其作用是把逻辑代码和处理琐碎事务的代码分离开，
    以便能够分离复杂度。在python中最能体现AOP思想的是装饰器。

    所以应该在登录验证装饰器@auth.login_required中进行权限校验。
    可以大量减少重复代码的使用，而且对外部隐藏了内部的实现细节，对调用者也显得十分友好。

2.@auth.login_required鉴权具体实现
    2.1 数据库的用户表会有一个auth字段，代指用户属于系统的什么角色（超级管理员、经理、组长）。
    2.2 在生成用户token令牌的时候，把用户的scope也写到令牌里面，后续用户访问服务器不用再次查询auth（scope为auth字段对应的权限类名）
    2.3 创建libs/scope.py模块，里面每一个类对应着一个角色的权限

3.scope模块具体实现
第一个方案：使用endpoint进行进行单个视图函数的控制
    此方案要注意：因为我们是通过蓝图把视图函数注册到flask对象的，所以endpoint会在原有的数据前面加上蓝图名字"v1."

随着业务的迭代，视图函数肯定会变得越来越多，当一个视图模块下100个视图函数都需要授权给某个角色访问，那我们就要在allow_api添加100个视图函数
第二个方案：
    每个角色类添加一个变量：allow_module， 实现视图模块级别的权限控制
    此方案实现比较友好的办法，不变动调用方式（加参数），直接在endpoint做手脚。
    在把视图函数注册到红图的时候，在定义endpoint的时候做点手脚：endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
这样就把视图模块名加到endpoint里面了。
    然后is_in_scope函数将视图模块名分隔出来，再与角色类定义的allow_module进行鉴权。

知识点：
    1. __add__内置方法
    2. 考虑三个粒度的判断顺序: allow_api, allow_module, forbidden


"""


class Scope:
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    forbidden = ['v1.user+super_get_user', 'v1.user+super_delete_user']

    def __init__(self):
        pass


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False

