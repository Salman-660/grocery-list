# Initialize a list with an empty string (not necessary, can start with empty list)
list = [""]

# Remove the initial empty string to start with an actual empty list
list.remove(list[0])

# Infinite loop to take user input until EOF (Ctrl+D)
while True:
    try:
        # Read input from user, convert to uppercase
        x = (input("")).upper()

        # If input is not empty or only spaces, add to the list
        if x.strip():
            list.append(x)

        # Sort the list after every new addition
        list.sort()

    # Break the loop when user signals end-of-input (Ctrl+D)
    except EOFError:
        break

# Create a dictionary with the count of each item in the list
count = {item: list.count(item) for item in list}

# Print the count and item for each unique grocery item
for c in count:
    print(f"{count[c]} {c}")
