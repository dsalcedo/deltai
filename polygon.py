from typing import Optional
import math


class Polygon:

    def __create_map(self, number: int):
        """
        :param number:
        """
        factor = (number * 2) + 1
        line_center = (factor - number) - 1
        center_line_center = (factor - line_center) - 1
        lines = []
        line = []

        limit = factor - 1

        exec("line.append('');" * factor)
        exec("lines.append(line);" * factor)

        final_rangers = []
        max_limit = math.floor(limit / 2)

        x = list(range(0, max_limit + 1))
        xx = list(reversed(range(max_limit)))

        list_line = x + xx

        exec("final_rangers.append(list_line);" * factor)

        may_limit = math.floor(len(final_rangers) / 2)
        y = list(reversed(range(0, may_limit + 1)))
        yy = list(range(1, may_limit + 1))
        list_line_y = y + yy

        x = 0
        y = 0

        while y < len(final_rangers):
            x_alias = list_line[y]
            y_alias = list_line_y[y]

            new_items = [0 if x_alias == 0 else v for v in final_rangers[y]]
            new_items = [0 if x_alias * v < max_limit else v for v in new_items]
            new_items = [0 if v <= y_alias else 1 for v in new_items]

            print(new_items)

            x = x + 1
            y = y + 1

    def build(self, number: int, show_map: Optional[bool] = False) -> int:
        """
        :param number:
        :param show_map:
        """
        assert type(number) == int
        assert number > 0, "Number not valid"

        list_number = list(reversed(range(1, number + 1)))
        list_ranged = list_number[0:2]
        list_number[:] = map(lambda x: x * x, list_ranged)
        response = sum(list_number)

        if show_map:
            self.__create_map(number)

        return response


try:
    number_value = 15
    value = Polygon().build(number_value, show_map=True)
    message = "The result is {}".format(value)
except AssertionError as ex:
    message = "Assert message: {0}".format(str(ex))
except Exception as ex:
    message = "Exception message: {0}".format(str(ex))
finally:
    print(message)
