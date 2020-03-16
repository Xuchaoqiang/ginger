# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from flask import request

from app.api.models.user import User
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.api.validators.forms import ClientForm

api = Redprint("client")


@api.route('/register', methods=['POST'])
def create_client():
    # 注册
    # 参数校验：WTForms 验证表单
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    return "success"


def __register_user_by_email(form):
    form = UserEmailForm(data=request.json)
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)