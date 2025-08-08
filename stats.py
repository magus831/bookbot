# The `count_words` function takes the contents of a file as a string.
def count_words(file_contents):
    # Splits the string into a list of words and gets the length of the list.
    word_count = len(file_contents.split())
    # Prints the total number of words found.
    print(f"Found {word_count} total words")
    # Calls the `letter_count` function to count the occurrences of each letter.
    letter_count(file_contents)

# The `letter_count` function also takes the file contents as a string.
def letter_count(file_contents):
    # Initializes an empty dictionary to store the letter counts.
    letter_counts = {}
    
    # Iterates through each character in the file contents.
    for char in file_contents:
        # Checks if the character is an alphabet letter.
        if char.isalpha():
            # Converts the character to lowercase to ensure case-insensitive counting.
            char_lower = char.lower()
            # If the lowercase letter is already in the dictionary, increment its count.
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            # Otherwise, add the new letter to the dictionary with a count of 1.
            else:
                letter_counts[char_lower] = 1
    
    # Calls the `sort_dict` function to sort and print the letter counts.
    sort_dict(letter_counts)

# The `sort_dict` function takes a dictionary of letter counts and an optional `reverse` parameter.
def sort_dict(letter_counts, reverse=True):
    
    # Sorts the dictionary items (key-value pairs) based on their values in descending order.
    # `lambda item: item[1]` specifies that the sorting key is the second element of each item (the value).
    sorted_items = sorted(letter_counts.items(), key=lambda item: item[1], reverse=reverse)
    print("---------- Character Count ----")
    
    # Iterates through the sorted items and prints each letter and its count.
    for key, value in sorted_items:
        print(f"{key}: {value}")




