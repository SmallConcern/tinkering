from flood_fill_string import FloodFillString
from flood_fill_string import InputStringError
import pytest

def get_email_string():
    return [
        "##### ###",
        "# # # #   ",
        "# # #     ",
        "# ######  ",
        "#### #    "
    ]

class TestFloodFillString():
    def test_flood_fill_string_init(self):
        ffs = FloodFillString(["foo"], 0, 0)
        assert ffs.string_list == ["foo"]
        assert ffs.rows == 0
        assert ffs.cols == 0

    def test_flood_fill_string_errors(self):
        with pytest.raises(InputStringError) as exc:
            ffs = FloodFillString(None, 0, 0)
        assert "Provided string_list is None." in str(exc.value)
        with pytest.raises(InputStringError) as exc:
            ffs = FloodFillString("foo", 0, 0)
        assert "Provided string_list is not a list." in str(exc.value)

    def test_flood_fill_single_string(self):
        with pytest.raises(InputStringError) as exc:
            FloodFillString.fill_string('', 0)
        assert "Provided string is empty" in str(exc.value)
        assert FloodFillString.fill_string(" ", 1) == ("#", 0, 1)
        assert FloodFillString.fill_string("# #", 2) == ("###", 1, 2)
