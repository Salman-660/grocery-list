def main():
    grocery_list_counter()

def grocery_list_counter():
    grocery_list = [""]  
    grocery_list.remove(grocery_list[0])

    print("Add your groceries here:")

    while True:
        try:
            x = input("").upper()
            if x.strip():  # Ignore empty input
                grocery_list.append(x)
            grocery_list.sort()
        except EOFError:
            break

    count = {item: grocery_list.count(item) for item in grocery_list}  # Count occurrences of each item

    for c in count:
        print(f"{count[c]} {c}")

    return count   #add return for testing


if __name__ == "__main__":
    main()
