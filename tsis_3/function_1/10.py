def polindrome(word):
    rev_word = ''.join(reversed(word))
    if(word == rev_word):
        print("Yes")
    else:
        print("No")


word = input()
polindrome(word)