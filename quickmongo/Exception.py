# Base Error Class
class QuickMongoError(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

# Value not int error
class ValueNotIntError(QuickMongoError):

    def __init__(self, message: str):
        super().__init__(message)

# Invaid event error
class InvalidEventError(QuickMongoError):

    def __init__(self, message: str):
        super().__init__(message)
