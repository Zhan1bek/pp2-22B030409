import re
def text_match(text):
        string = '^a(b*)$'
        if re.search(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("a"))
print(text_match("ab"))
