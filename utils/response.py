from rest_framework.response import Response


class CoreResponse(Response):
    class Meta:
        code = 200
        message = "Done"

    def __init__(self, code=None, message=None, data={}, *args, **kwargs):
        code = code if code else self.Meta.code
        message = message if message else self.Meta.message
        data = {
            'code': code,
            'message': message,
            'data': data
        }
        super().__init__(data=data, status=code, *args, **kwargs)


class CoreNoContentResponse(CoreResponse):
    class Meta:
        code = 204
        message = None


class CoreBadRequestResponse(CoreResponse):
    class Meta:
        code = 400
        message = "Bad Request"


class CoreNotFoundResponse(CoreResponse):
    class Meta:
        code = 404
        message = "Not Found"


class CoreNotAcceptableResponse(CoreResponse):
    class Meta:
        code = 406
        message = "Not Acceptable"


class CoreServerErrorResponse(CoreResponse):
    class Meta:
        code = 500
        message = "Server Error"
