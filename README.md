# Grocery List Counter

A simple Python script that allows users to input grocery items one by one and outputs a sorted list with the quantity of each item. Input ends when the user signals EOF (Ctrl+D on Linux/macOS, Ctrl+Z on Windows).

## Features

- Adds user-entered items to a list.  
- Converts all items to uppercase for consistency.  
- Counts the frequency of each item.  
- Outputs a sorted list with item counts.  

## Usage

1. Run the script in a terminal or command prompt:

```bash
python grocery_list.py
Enter grocery items line by line.

Press Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to finish input.

The script will display the number of times each item was entered, sorted alphabetically.

# Example
Input:
apple
banana
apple
orange
banana

Output:
2 APPLE
2 BANANA
1 ORANGE
# Notes
Only non-empty inputs are counted.

Input is case-insensitive (all converted to uppercase).

# Test File
A test.py file is provided to ensure that any modifications to the program do not break its functionality.
You can run the tests with pytest in the terminal:

``` bash
pytest test.py
```
This will verify if the program still works as intended.

# Required Libraries
- pytest

