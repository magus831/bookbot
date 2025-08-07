def get_book_text(file_contents):
    print(file_contents)

def main():
    file_path = "../books/frankenstein.txt"
    with open(file_path) as file:
        file_contents = file.read()
    
    get_book_text(file_contents)

main()
