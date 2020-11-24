def ask_password(text, attempt=0):
    attempt += 1
    if attempt < 3 and text == 'password':
        print('Пароль приянт')
        attempt = 3
    elif attempt > 2:
        print('В доступе отказано')
    else:
        ask_password(input(), attempt)


ask_password(input())
