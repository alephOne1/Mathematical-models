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

    def __call__(self):
        return self.value

    @staticmethod
    def validate_number_value(value, value_type):
        if type(value) in {int, float, bool}:
            if value_type == "natural" and (type(value) != int or value <= 0):
                raise _InvalidAlgebraNumberValueException(
                    "Natural number mustn't have fractional part or be less than 1 or be an element of non numerical type."
                )
            elif value_type == "integer" and type(value) != int:
                raise _InvalidAlgebraNumberValueException(
                    "Integer value mustn't have fractional part or be an element of non numerical type."
                )
            elif value_type == "real" and type(value) != float:
                raise _InvalidAlgebraNumberValueException(
                    "Real value mustn't be an element of non numerical or non float type."
                )
        else:
            raise _InvalidAlgebraNumberValueException(
                "Algebraic number value mustn't be an element of non numerical type."
            )


class AlgebraOperation(_AlgebraObject):
    OPERATIONS_TYPES = ["add", "subtract", "multiply", "divide"]

    def __init__(self, default_type="add", *args, **kwargs):
        if default_type in __class__.OPERATIONS_TYPES:
            self.type = default_type
        else:
            raise _InvalidAlgebraOperationException(
                "There is no such available algebraic operation."
            )

        super().__init__(__class__)

    def __repr__(self):
        return f"<Algebraic {self.type} Operation at {hex(id(self))}>"

    def __str__(self):
        return self.__repr__()

    def __call__(self, *args):
        return getattr(self, self.type)(*args)

    def change_type(self, new_type="add"):
        if new_type in __class__.OPERATIONS_TYPES:
            self.type = new_type
        else:
            raise _InvalidAlgebraOperationException(
                "There is no such available algebraic operation."
            )

    def add(self, *args):
        if set(map(type, args)) != {AlgebraNumber}:
            raise _InvalidOperationArgumentsException(
                "Algebra operation arguments must be elements of numeric type."
            )
        else:
            result_value = 0
            result_type = "natural"

            available_numeric_types = AlgebraNumber.NUMERIC_TYPES

            for number in args:
                if available_numeric_types.index(number.type) > available_numeric_types.index(result_type):
                    result_type = number.type
                result_value += number()

            return AlgebraNumber(result_value, result_type)

    def subtract(self, *args):
        if set(map(type, args)) != {AlgebraNumber}:
            raise _InvalidOperationArgumentsException(
                "Algebra operation arguments must be elements of numeric type."
            )
        else:
            result_value = args[0]()
            result_type = args[0].type

            available_numeric_types = AlgebraNumber.NUMERIC_TYPES

            for number in args[1:]:
                if available_numeric_types.index(number.type) > available_numeric_types.index(result_type):
                    result_type = number.type
                result_value -= number()

            return AlgebraNumber(result_value, result_type)

    def multiply(self, *args):
        if set(map(type, args)) != {AlgebraNumber}:
            raise _InvalidOperationArgumentsException(
                "Algebra operation arguments must be elements of numeric type."
            )
        else:
            result_value = 1
            result_type = "natural"

            available_numeric_types = AlgebraNumber.NUMERIC_TYPES

            for number in args:
                if available_numeric_types.index(number.type) > available_numeric_types.index(result_type):
                    result_type = number.type
                result_value *= number()

            return AlgebraNumber(result_value, result_type)

    def divide(self, *args):
        if set(map(type, args)) != {AlgebraNumber}:
            raise _InvalidOperationArgumentsException(
                "Algebra operation arguments must be elements of numeric type."
            )
        else:
            result_value = args[0]()
            result_type = args[0].type

            available_numeric_types = AlgebraNumber.NUMERIC_TYPES

            for number in args[1:]:
                if available_numeric_types.index(number.type) > available_numeric_types.index(result_type):
                    result_type = number.type

                if number() == 0:
                    raise ZeroDivisionError
                else:
                    result_value /= number()

            if result_value == int(result_value):
                return AlgebraNumber(int(result_value), result_type)
            else:
                return AlgebraNumber(result_value, "real")


if __name__ == "__main__":
    number_first_example = AlgebraNumber(12312, "natural")
    number_second_example = AlgebraNumber(-1232214, "integer")

    operation_example = AlgebraOperation("divide")

    result = operation_example(number_first_example, number_second_example)

    print(result())
