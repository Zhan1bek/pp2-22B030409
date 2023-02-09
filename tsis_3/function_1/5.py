def reverse(split_word):
    rev_word = reversed(split_word)
    final = ' '.join(rev_word)
    print(final)


word = input()
split_word = word.split(' ')
reverse(split_word)