def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    count = {}
    for ch in lowered_text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count

def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    letter_count = [
        (ch, num)
        for ch, num in count_letters(file_contents).items()
        if ch.isalpha()
    ]
    letter_count.sort(reverse=True, key=lambda x: x[1])
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for ch, num in letter_count:
        print(f"The '{ch}' character was found {num} times")
    print("--- End report ---")

main()
