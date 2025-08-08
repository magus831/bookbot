# The 'sys' module provides access to system-specific parameters and functions.
import sys

# We're importing the 'count_words' function from a local module named 'stats'.
# It's assumed this function takes a string (the file's contents) and performs a word count.
from stats import count_words

# This function takes the text content of a book and calls the 'count_words' function.
def get_book_text(file_contents):
    count_words(file_contents)

def main():
    
    # Check if the correct number of command-line arguments were provided.
    # We expect 2: the script name and the file path.
    if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

    # Get the file path from the command-line arguments.
    # sys.argv[1] is the first argument after the script name.
    file_path = sys.argv[1]
    
    # We use a `try...except` block to handle potential file-related errors gracefully.
    try:    
        # The `with open(...) as file:` syntax ensures the file is automatically closed.
        with open(file_path) as file:
            # Reads the entire content of the file into a single string.
            file_contents = file.read()
    # If the file specified by `file_path` doesn't exist, a `FileNotFoundError` is raised.
    except FileNotFoundError:
        print(f"Error: the file at {file_path} was not found.")
        sys.exit(1)

    
    # Prints a series of headers and informational messages.
    print("============ BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count --------")
    get_book_text(file_contents)
    print("============ END ==============")

# This line ensures that the `main` function is called when the script is executed.
main()
