def main():
    text = get_text()
    word_count = get_word_count(text)
    print(word_count)
    chars = get_chars(text)
    print(chars)
    # Report text
    print(str(word_count) + " words found in the document\n")
    sorted_chars = dict(sorted(chars.items()))
    for char in sorted_chars.keys():
        if char.isalpha():
            print(
                "The "
                + "'"
                + str(char)
                + "'"
                + " character was found "
                + str(sorted_chars[char])
                + " times"
            )


def get_text():
    with open("books/frankenstein.txt", "r") as file:
        return file.read()


def get_word_count(content):
    words = content.split()
    word_count = len(words)
    return word_count


def get_chars(file):
    chars = {}
    file = file.lower()
    words = file.split()
    for word in words:
        for char in word:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1
    return chars


main()
