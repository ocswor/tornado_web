#!/usr/bin/env python
# coding: utf-8

from copy import copy
from hashlib import md5

KEY = "Kosdp*(&iw)sd"


def check_sign(params, sign_key=None):
    if sign_key is None:
        sign_key = KEY

    data = copy(params)
    if "sign" not in data:
        return False
    sign = data.pop("sign")

    keys = sorted(data.keys())
    _str = ""
    for key in keys:
        _str += "%s=%s&" % (key, data[key])
    _str += "key=%s" % sign_key

    return md5(_str.encode("utf-8")).hexdigest() == sign


def make_sign(params, sign_key=None):
    if sign_key is None:
        sign_key = KEY

    data = copy(params)
    keys = sorted(data.keys())
    _str = ""
    for key in keys:
        _str += "%s=%s&" % (key, data[key])
    _str += "key=%s" % sign_key

    data["sign"] = md5(_str.encode("utf-8")).hexdigest()
    return data
