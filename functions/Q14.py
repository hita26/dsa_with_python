# 14. Check palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("madam"))
