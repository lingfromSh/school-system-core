from django.contrib.auth.hashers import check_password, make_password


def hash_password(raw_password=None):
    """加密密码"""
    __hash_salt = "c2gxblMvNDNaVDhNd2sweVZBZlg5T1c3NGlEN3V0NVlCSGREVjJOU2lBND0="
    return make_password(password=raw_password, salt=__hash_salt)


def authenticate_password(storaged_password=None, encoded_password=None):
    """校验密码"""
    return check_password(password=storaged_password, encoded=encoded_password)
