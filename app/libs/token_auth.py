# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
    """
    HTTPBasicAuth协议传递账号密码方式
        1.在header里面传递账号密码
        2.传递参数： key=Authorization,
                    value=basic base64(account:password)
    """
    return True
