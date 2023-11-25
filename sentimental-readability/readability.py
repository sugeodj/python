def calculateLetters(input_string):
    letters = 0
    for char in range(len(input_string)):
        if input_string[char] >= 'a' and input_string[char] <= 'z':
            letters += 1
    return letters


def calculateWords(input_string):
    words = 1
    for char in range(len(input_string)):
        if input_string[char] == ' ':
            words += 1
    return words


def calculateSentences(input_string):
    sentences = 0
    for char in range(len(input_string)):
        if input_string[char] == '.' or input_string[char] == '!' or input_string[char] == '?':
            sentences += 1
    return sentences


def results(i):
    if i < 1:
        print('Before Grade 1')
    elif i >= 16:
        print('Grade 16+')
    else:
        print(f'Grade {i}')


input_string = input("Text: ").lower()
length = len(input_string)

L = 100 * (calculateLetters(input_string) / calculateWords(input_string))
S = 100 * (calculateSentences(input_string) / calculateWords(input_string))
index = round(0.0588 * L - 0.296 * S - 15.8)

results(index)