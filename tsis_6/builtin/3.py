def isPalindrome(s):
    if s == str.join('', list(reversed(s))):
        print('Is palindrome')
    else:
        print('Not palindrome')