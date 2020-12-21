


class CommonException(Exception):
    """
    Custom common exception for common case.
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f'{self.code.value}: {self.message.value}'


class InvalidException(CommonException):
    """
    Custom inherited exception from CommonException for special case.
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(self.code, self.message)

    def __str__(self):
        return f'{self.code.value}: {self.message.value}'

