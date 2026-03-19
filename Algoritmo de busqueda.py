def binary_search_interactive():
    """
    Performs a binary search on a predefined sorted list based on user input.
    """
    sorted_list = [11, 22, 34, 45, 56, 67, 78, 89, 91, 100]
    print("We will be searching in a mystery list")

    try:
        target_number = int(input("Please enter a number to search for: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    low = 0
    high = len(sorted_list) - 1
    found = False

    while not found and low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == target_number:
            print(f"\nSuccess! The number {target_number} was found at index {mid}.")
            found = True
            break
        elif guess < target_number:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print(f"\nSorry, the number {target_number} was not found in the list.")

if __name__ == "__main__":
    binary_search_interactive()
