# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from wtforms import StringField
from wtforms.validators import DataRequired

from app.forms.base import Form


class BookSearchForm(Form):
    q = StringField(
        validators=[DataRequired(message="搜索关键词不能为空！")]
    )
