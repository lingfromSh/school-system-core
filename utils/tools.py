import os
from base64 import urlsafe_b64encode


def unique_id(length=32):
    """生成base64串"""
    return urlsafe_b64encode(os.urandom(length)).decode()[:length]
