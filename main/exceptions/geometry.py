class _NotGeometryObjectException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _NestedSpacesException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _BadDimensionsNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _BadCoordinatesException(Exception):
    def __init__(self, message):
        super().__init__(message)


class _NotPointsException(Exception):
    def __init__(self, message):
        super().__init__(message)


__all__ = [
    "_NotGeometryObjectException",
    "_NestedSpacesException",
    "_BadDimensionsNumberException",
    "_BadCoordinatesException",
    "_NotPointsException"
]