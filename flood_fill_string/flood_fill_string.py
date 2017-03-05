class InputStringError(Exception):
    pass

class FloodFillString(object):
    def __init__(self, string_list, rows, cols):
        if not string_list:
            raise InputStringError("Provided string_list is None.")
        if not isinstance(string_list, list):
            raise InputStringError("Provided string_list is not a list.")
        self.string_list = string_list
        self.rows = rows
        self.cols = cols

    @staticmethod
    def fill_string(input_str, pos):
        if not input_str:
            raise InputStringError("Provided string is empty.")
        col = pos - 1
        left_point = input_str.rfind('#', 0, col) + 1
        right_point = input_str.find('#', col)
        if right_point == -1:
            right_point = len(input_str)
        input_str = input_str[:left_point] + \
               '#'*(right_point - left_point) + input_str[right_point:]
        return input_str, left_point, right_point

    def flood_fill(self, row, col):
        start_string = self.string_list[row]
        self.string_list[row], left_pos, right_pos = \
            FloodFillString.fill_string(start_string, col)
        if left_pos == col and right_pos == col:
            return

