def palindrome(text):
    text = ''.join(text.split())
    text = text.lower()
    if text[::-1] == text:
        print('Палиндром')
    else:
        print('Не палиндром')


palindrome(input())
