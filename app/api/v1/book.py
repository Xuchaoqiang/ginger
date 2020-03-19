# -*- coding:utf-8 -*-
# @Author :xuchaoqiang


# redprint
from flask import jsonify
from sqlalchemy import or_

from app.forms.book import BookSearchForm
from app.libs.redprint import Redprint
from app.models.book import Book

api = Redprint("book")


@api.route('')
def search():
    form = BookSearchForm().validate_for_api()
    # sqlachemy模糊匹配
    q = '%' + form.q.data + '%'
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))
    ).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)
