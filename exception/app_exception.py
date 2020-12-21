


class CommonException(Exception):
    """
    Custom common exception for common case.
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return repr(self.message), repr(self.code)


class InvalidException(CommonException):
    """
    Custom inherited exception from CommonException for special case.
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def __str__(self):
        return repr(self.message), repr(self.code)

