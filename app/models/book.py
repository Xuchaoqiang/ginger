# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base


class Book(Base):
    """
    所有sqlachemy产生的orm对象都不会执行__init__方法，orm对象是通过元类的方式生成的。
    想要在生成orm对象的时候执行__init__方法，可以结组sqlachemy的内置装饰器 orm.reconstructor
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding',
                       'publisher',
                       'price','pages', 'pubdate', 'isbn',
                       'summary',
                       'image']
