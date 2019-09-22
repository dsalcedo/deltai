class Isbn10:
    MULTI = 11
    STRING_LENGTH = 13
    NUMERIC_LENGTH = 10
    SEPARATOR = "-"

    def __init__(self, str_input: str):
        """
        :param str_input:
        """
        assert type(str_input) == str, "The input most be string"

        if len(str_input) == self.STRING_LENGTH:
            assert "-" in str_input, "The input has incorrect format"
            assert str_input.count("-") == 3,  "The input has incorrect format"
            assert len(str_input.replace("-", "")) == 10, "The input has incorrect format"
            assert int(str_input.replace("-", ""))
            str_input = str_input.replace("-", "")
        else:
            assert len(str_input) == self.NUMERIC_LENGTH, "The input should be 13 string or 10 numeric length size"

        str_reversed = str_input[::-1]

        results = []
        operations_str = []
        operations_sums_str = []

        for i in reversed(range(0, 10)):
            index = i + 1
            digit = int(str_reversed[i])

            operations_str.append(
                "{} x {}".format(digit, index)
            )

            operation = digit * index

            operations_sums_str.append(operation)

            results.append(operation)

        self.result = sum(results)
        self.operations_str = operations_str
        self.operations_sums_str = operations_sums_str

    def debugg(self):
        """
        Prints in console the process
        :return:
        """
        print("Multiply: {}".format(self.operations_str))
        print("Sums: {}".format(self.operations_sums_str))
        print("Result: {}".format(self.result))
        return self

    def check(self) -> bool:
        """
        Check if the result is multiple of some number
        """

        is_multi = False

        if self.result > self.MULTI != 0:
            x = self.result

            while x > 0:
                x -= self.MULTI

            if x != 0 or x < 0:
                is_multi = False
            elif x == 0:
                is_multi = True

        return is_multi


try:
    isbn = Isbn10("0-306-40615-2").debugg().check()
    message = isbn
except AssertionError as ex:
    message = "Assert message: {0}".format(str(ex))
except Exception as ex:
    message = "Exception message: {0}".format(str(ex))
finally:
    print(message)
