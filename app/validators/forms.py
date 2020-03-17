# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User

from app.validators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(
        validators=[DataRequired(message="账户名不能为空"), length(min=5, max=32)]
    )
    secret = StringField()
    type = IntegerField(
        validators=[DataRequired()]
    )

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(
        validators=[Email(message="invalidate email")]
    )
    secret = StringField(
        validators=[DataRequired(message="密码不能为空"), Regexp(r'^[A-Za-z0-9_*&$#]{6,22}$')]
    )
    nickname = StringField(
        validators=[DataRequired(), length(min=2, max=22)]
    )

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()