base = ['Вика', 'Иван', 'Максим', 'Юлия Иванкова']


def hello(name):
    print('Здравствуйте, {}! Вашу карту ищут...'.format(name))


def search_card(name):
    global base
    if name in base:
        print('Ваша карта с номероом {} найдена'.format(base.index(name) + 1))
    else:
        print('Ваша карта не найдена')


name = input()
hello(name)
search_card(name)
