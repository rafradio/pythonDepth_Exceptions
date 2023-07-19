class UserException(Exception):
    pass

class DataValueError(UserException):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value