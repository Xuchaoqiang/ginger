# -*- coding:utf-8 -*-
# @Author :xuchaoqiang

from werkzeug.exceptions import HTTPException


class ClientTypeError(HTTPException):

    code = 400
    description = (
        "client is invalid"
    )