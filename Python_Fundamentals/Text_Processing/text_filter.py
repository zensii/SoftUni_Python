def censor_word(banned_word):
    return len(banned_word) * '*'


def censor_text(banned_words: list, text: str):
    for word in banned_words:
        while word in text:
            text = text.replace(word, censor_word(word))
    return text


def main():
    banned_words = input().split(', ')
    text = input()
    censored_text = censor_text(banned_words, text)
    print(censored_text)


if __name__ == '__main__':
    main()

