from grocery_list import grocery_list_counter

def test_grocery_counter():
    data = ["apple", "banana", "Apple", "orange", "banana"]
    expected = {"APPLE": 2, "BANANA": 2, "ORANGE": 1}
    
    # Call function with list argument instead of interactive input
    result = grocery_list_counter(data)
    
    assert dict(result) == expected
