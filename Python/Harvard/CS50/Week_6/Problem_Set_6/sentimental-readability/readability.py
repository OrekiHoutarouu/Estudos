def main():
    text = str(input("Text: "))

    letters = countLetters(text)
    words = countWords(text)
    sentences = countSentences(text)
    L = (letters / words) * 100
    S = (sentences / words) * 100
    grade = (0.0588 * L) - (0.296 * S) - 15.8

    if grade < 1:
        print("Before Grade 1")

    elif grade >= 1 and grade < 16:
        print(f"Grade {grade:.0f}")

    else:
        print("Grade 16+")


def countLetters(text):
    letters = 0
    for letter in text:
        if letter.isalpha():
            letters += 1

    return letters


def countWords(text):
    words = 1
    for word in text:
        if word.isspace():
            words += 1

    return words


def countSentences(text):
    sentences = 0
    for sentence in text:
        if sentence == "!" or sentence == "?" or sentence == ".":
            sentences += 1

    return sentences


if __name__ == "__main__":
    main()
