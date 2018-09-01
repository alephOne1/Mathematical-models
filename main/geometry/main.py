import sys
sys.path.append("..")

from exceptions.geometry import *

class _GeometryObject:
    TYPES = []

    def __init__(self, object_type, n_dimensions=2, *args, **kwargs):
        self.type = object_type

        if self.type not in self.TYPES:
            __class__.TYPES.append(self.type)

    @staticmethod
    def is_valid_dimensions_number(n_dimensions) -> bool:
        return type(n_dimensions) == int and n_dimensions >= 0


class GeometrySpace(_GeometryObject):
    def __init__(self, n_dimensions=2, *args, **kwargs):
        if self.is_valid_dimensions_number(n_dimensions):
            self.n_dims = n_dimensions
        else:
            raise _BadDimensionsNumberException(
                "Number of dimensions must be non negative integer."
            )

        super().__init__(
            self.__class__,
            self.n_dims
        )

        self._objects = []

    def __repr__(self) -> str:
        return f"<{self.n_dims}-dimensional geometric Space at {__file__}>"

    def __str__(self) -> str:
        return self.__repr__()

    def add(self, object_to_add):
        if _GeometryObject not in object_to_add.__class__.__mro__:
            raise _NotGeometryObjectException(
                "Geometry space must contain only geometric object."
            )
        elif type(object_to_add) == GeometrySpace:
            raise _NestedSpacesException(
                "Geometry space can't contain another geometric spaces."
            )
        elif self.n_dims != object_to_add.n_dims:
            raise _BadDimensionsNumberException(
                "Space can contain geometric object with only same number of dimensions."
            )
        else:
            self._objects.append(object_to_add)

    def show_contents(self):
        print(
            f"Geometric {self.n_dims}-dimensional Space objects {{\n" + "\n".join(
                map(lambda obj: "\t" + str(obj), self._objects)
            ) + "\n}"
        )


class Point(_GeometryObject):
    def __init__(self, n_dimensions=2, point_coords=None, *args, **kwargs):
        if self.is_valid_dimensions_number(n_dimensions):
            self.n_dims = n_dimensions
        else:
            raise BadDimensionsNumberException(
                "Number of dimensions must be non negative integer."
            )

        if point_coords is None:
            self.coords = (0 for _ in range(self.n_dims))
        elif self.is_valid_coords(point_coords, self.n_dims):
            self.coords = point_coords
        else:
            raise _BadCoordinatesException(
                "Coordinates must have same number of elements as number of dimensions and consist of only numeric elements."
            )

        super().__init__(
            self.__class__,
            self.n_dims
        )

    def __repr__(self):
        return f"<{self.n_dims}-dimensional geometric Point at {__file__}>"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def is_valid_coords(coords, n_dimensions):
        return len(coords) == n_dimensions and {type(coord) for coord in coords} <= {float, int}


if __name__ == "__main__":
    space_example = GeometrySpace(3)

    point_first_example = Point(3, (1, 2, 3.1))
    point_second_example = Point(3, (2, 33, 3.1))
    point_third_example = Point(3, (11, 2, 3.1))

    space_example.add(point_first_example)
    space_example.add(point_second_example)
    space_example.add(point_third_example)

    space_example.show_contents()

    print(space_example)
