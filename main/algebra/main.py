import sys
sys.path.append("..")

try:
    from exceptions.algebra import *
except ModuleNotFoundError as error:
    raise error

class _AlgebraObject:
    OBJECTS_TYPES = []

    def __init__(self, object_type, *args, **kwargs):
        self._object_type = object_type

        if self._object_type not in __class__.OBJECTS_TYPES:
            __class__.OBJECTS_TYPES.append(self._object_type)


class AlgebraNumber(_AlgebraObject):
    NUMERIC_TYPES = ["natural", "integer", "real"]

    def __init__(self, value=1, default_type="natural"):
        if default_type in __class__.NUMERIC_TYPES:
            self.type = default_type
        else:
            raise _BadAlgebraNumberTypeException(
                "There is no such algebraic number type."
            )

        super().__init__(__class__)

        self.validate_number_value(value, self.type)

        self.value = value

    def __repr__(self):
        return f"<Algebraic {self.type} Number at {hex(id(self))}>"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def validate_number_value(value, value_type):
        if type(value) in {int, float, bool}:
            if value_type == "natural" and (type(value) != int or value <= 0):
                raise _BadAlgebraNumberValueException(
                    "Natural number mustn't have fractional part or be less than 1 or be an element of non numerical type."
                )
            elif value_type == "integer" and type(value) != int:
                raise _BadAlgebraNumberValueException(
                    "Integer value mustn't have fractional part or be an element of non numerical type."
                )
            elif value_type == "real" and type(value) != float:
                raise _BadAlgebraNumberValueException(
                    "Real value mustn't be an element of non numerical or non float type."
                )
        else:
            raise _BadAlgebraNumberValueException(
                "Algebraic number value mustn't be an element of non numerical type."
            )


class AlgebraOperation(_AlgebraObject):
    OPERATIONS_TYPES = ["add", "subtract", "multiply", "divide"]

    def __init__(self, default_type="add", *args, **kwargs):
        if default_type in __class__.OPERATIONS_TYPES:
            self.type = default_type
        else:
            raise _BadAlgebraOperationException(
                "There is no such available algebraic operation."
            )

        super().__init__(__class__)

    def __repr__(self):
        return f"<Algebraic {self.type} Operation at {hex(id(self))}>"

    def __str__(self):
        return self.__repr__()

    def change_type(self, new_type="add"):
        if new_type in __class__.OPERATIONS_TYPES:
            self.type = new_type
        else:
            raise _BadAlgebraOperationException(
                "There is no such available algebraic operation."
            )


if __name__ == "__main__":
    number_example = AlgebraNumber(12312, "natural")

    operation_example = AlgebraOperation("add")
    operation_example.change_type("multiply")

    print(number_example, operation_example, sep="\n")
