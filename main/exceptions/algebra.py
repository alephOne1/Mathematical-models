class _BadAlgebraOperationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _BadAlgebraNumberTypeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _BadAlgebraNumberValueException(Exception):
    def __init__(self, message):
        super().__init__(message)


__all__ = [
    "_BadAlgebraOperationException",
    "_BadAlgebraNumberTypeException",
    "_BadAlgebraNumberValueException"
]