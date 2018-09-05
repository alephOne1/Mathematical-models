class _InvalidAlgebraOperationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _BadAlgebraNumberTypeException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _InvalidAlgebraNumberValueException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _InvalidOperationArgumentsException:
    def __init__(self, message):
        super().__init__(message)


__all__ = [
    "_InvalidAlgebraOperationException",
    "_BadAlgebraNumberTypeException",
    "_InvalidAlgebraNumberValueException",
    "_InvalidOperationArgumentsException"
]