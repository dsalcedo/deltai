from functools import reduce


class Factorial:
    def __init__(self, positive_digit: int):
        """
        :param positive_digit:
        """
        assert type(positive_digit) == int, "The number is not valid"
        assert positive_digit >= 0, "The number is not valid"
        self.value = positive_digit

    def calculate(self) -> int:

        factorial = 1

        if self.value == 0:
            return factorial

        factorial = reduce(lambda x, y: x * y, range(1, self.value + 1))

        return factorial


try:
    number = 20
    value = Factorial(number).calculate()
    message = "The factorial of {0} is {1}".format(number, value)
except AssertionError as ex:
    message = "Assert message: {0}".format(str(ex))
except Exception as ex:
    message = "Exception message: {0}".format(str(ex))
finally:
    print(message)
