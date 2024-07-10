# -*- coding:utf-8 -*-

from cookie import hedra_auth


def get_token():
    token = hedra_auth.get_token()
    try:
        yield token
    finally:
        pass
