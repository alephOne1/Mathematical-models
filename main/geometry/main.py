import sys
sys.path.append("..")

try:
    from exceptions.geometry import *
except ModuleNotFoundError as error:
    raise error

class _GeometryObject:
    OBJECT_TYPES = []

    def __init__(self, object_type, n_dimensions=2, *args, **kwargs):
        self._object_type = object_type

        if self._object_type not in __class__.OBJECT_TYPES:
            __class__.OBJECT_TYPES.append(self._object_type)

    def __len__(self) -> int:
        return self._n_dims

    @staticmethod
    def is_valid_dimensions_number(n_dimensions) -> bool:
        return type(n_dimensions) == int and n_dimensions >= 0


class GeometrySpace(_GeometryObject):
    def __init__(self, n_dimensions=2, *args, **kwargs):
        if self.is_valid_dimensions_number(n_dimensions):
            self._n_dims = n_dimensions
        else:
            raise _BadDimensionsNumberException(
                "Number of dimensions must be non negative integer."
            )

        super().__init__(
            __class__,
            self._n_dims
        )

        self._objects = []

    def __repr__(self) -> str:
        return f"<{self._n_dims}-dimensional geometric Space at {hex(id(self))}>"

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, index) -> float:
        if type(index) not in {int, bool}:
            raise IndexError(
                "Index must be integer or boolean value."
            )
        elif index >= len(self._objects) or index < 0:
            raise IndexError(
                "Number of objects of this space is not correlated with coordinate index."
            )
        else:
            return self._objects[index]

    def add(self, object_to_add):
        if _GeometryObject not in object_to_add.__class__.__mro__:
            raise _NotGeometryObjectException(
                "Geometry space must contain only geometric object."
            )
        elif type(object_to_add) == GeometrySpace:
            raise _NestedSpacesException(
                "Geometry space can't contain another geometric spaces."
            )
        elif self._n_dims != object_to_add._n_dims:
            raise _BadDimensionsNumberException(
                "Space can contain geometric object with only same number of dimensions."
            )
        else:
            self._objects.append(object_to_add)

    def show_contents(self):
        print(
            f"Geometric {self._n_dims}-dimensional Space objects {{\n" + "\n".join(
                map(
                    lambda obj: "\t" + str(obj),
                    self._objects
                )
            ) + "\n}"
        )


class GeometryPoint(_GeometryObject):
    def __init__(self, n_dimensions=2, point_coords=None, *args, **kwargs):
        if self.is_valid_dimensions_number(n_dimensions):
            self._n_dims = n_dimensions
        else:
            raise BadDimensionsNumberException(
                "Number of dimensions must be non negative integer."
            )

        if point_coords is None:
            self.coords = (0 for _ in range(self._n_dims))
        elif self.is_valid_coords(point_coords, self._n_dims):
            self.coords = point_coords
        else:
            raise _BadCoordinatesException(
                "Coordinates must have same number of elements as number of dimensions and consist of only numeric elements."
            )

        super().__init__(
            __class__,
            self._n_dims
        )

    def __repr__(self) -> str:
        return f"<{self._n_dims}-dimensional geometric Point at {hex(id(self))}>"

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, index) -> float:
        if type(index) not in {int, bool}:
            raise IndexError(
                "Index must be integer or boolean value."
            )
        elif index >= len(self):
            raise IndexError(
                "Number of dimensions of this point is not correlated with coordinate index."
            )
        else:
            return self.coords[index]


    def distance(self, *args) -> list:
        if args:
            if set(map(type, args)) != {GeometryPoint}:
                raise _NotPointsException(
                    "Distance can be computed only between points."
                )
            else:
                distances = []

                for point in args:
                    current_squared_distance = 0

                    for index in range(len(point)):
                        if index >= len(self):
                            current_squared_distance += point[index]**2
                        else:
                            current_squared_distance += (point[index] - self[index])**2

                    distances.append(current_squared_distance ** 0.5)

                return distances
        else:
            return [sum(map(lambda coord: coord**2, self.coords)) ** 0.5]

    @staticmethod
    def is_valid_coords(coords, n_dimensions) -> bool:
        return len(coords) == n_dimensions and {type(coord) for coord in coords} <= {float, int}


if __name__ == "__main__":
    space_example = GeometrySpace(3)

    point_first_example = GeometryPoint(3, (1, 2, 3.1))
    point_second_example = GeometryPoint(3, (2, 33, 3.1))
    point_third_example = GeometryPoint(3, (11, 2, 3.1))

    space_example.add(point_first_example)
    space_example.add(point_second_example)
    space_example.add(point_third_example)

    space_example.show_contents()

    print(
        point_first_example.distance(),
        point_first_example.distance(
            point_second_example,
            point_third_example
        ),
        space_example[2],
        sep="\n"
    )
