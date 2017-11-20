def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter something:")
if is_palindrome(something):
    print('yes, it is palindrome')
else:
    print('no, it is not palindrom')
