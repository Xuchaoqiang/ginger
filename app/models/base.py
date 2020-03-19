# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

"""
1. Base类要声明为基类
    因为在 app db.create_all的时候，sqlalchemy会将所有继承于 db.Model的类都创建一张名字与类名对应的表。
    所以我们用 __abstract__ = True将Base 声明为一个基类，只用于被继承。

2. 解决在每次sqlalchemy入库的时候执行的事务于回滚
    每次入库要写的重复代码：
        try:
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    解决方法：对SQLAlchemy进行一层封装
        用python内置的上下文管理器和yield实现。
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import inspect, Column, Integer, SmallInteger, orm
from contextlib import contextmanager

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if "status" not in kwargs.keys():
            kwargs["status"] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def keys(self):
        return self.fields

    """
    hide 和 append可以灵活的改写model下面的fields属性，灵活的控制返回给用户的字段信息
    """

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)