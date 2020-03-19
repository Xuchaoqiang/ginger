# -*- coding:utf-8 -*-
# @Author :xuchaoqiang
from collections import namedtuple
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()

User = namedtuple("User", ["uid", "ac_type", "scope"])


@auth.verify_password
def verify_password(token, password):
    """
    HTTPBasicAuth协议传递账号密码方式
        1.在header里面传递账号密码
        2.传递参数： key=Authorization,
                    value=basic base64(account:password)
    """
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg="token is invalid",
                         error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg="token is expired",
                         error_code=1003)
    uid = data.get("uid")
    ac_type = data.get("type")
    scope = data.get("scope")

    allow = is_in_scope(scope)
    if not allow:
        raise Forbidden()

    return User(uid, ac_type, scope)
