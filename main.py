def main():
    word_count = 0
    letter_count = {}
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    with open(book) as f:
        file_contents = f.read()
    for word in file_contents.split():
        word_count += 1
    print(f"{word_count} words found in the document\r\n")

    for letter in file_contents:
        if letter.isalpha():
            lowercase_letter = letter.lower()
            if lowercase_letter in letter_count:
                letter_count[lowercase_letter] += 1
            else:
                letter_count[lowercase_letter] = 1

    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")

main()