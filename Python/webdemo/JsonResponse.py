# -- coding: utf-8 --

class JsonResponse(object):
    """
    统一的json返回格式
    """

    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @classmethod
    def success(cls, code=0, msg='success', data=None):
        return cls(code, msg, data)

    @classmethod
    def error(cls, code=-1, msg='error', data=None):
        return cls(code, msg, data)

    def to_dict(self):
        return {
            "code": self.code,
            "msg": self.msg,
            "data": self.data
        }
