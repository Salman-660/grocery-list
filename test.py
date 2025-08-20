from grocery_list import grocery_list_counter
import sys, io

def test_grocery_counter():
    data = "apple\nbanana\nApple\norange\nbanana\n"
    sys.stdin = io.StringIO(data)  # simulate typing input

    result = grocery_list_counter()  # no arguments, reads from "fake" stdin

    expected = {"APPLE": 2, "BANANA": 2, "ORANGE": 1}
    assert result == expected

