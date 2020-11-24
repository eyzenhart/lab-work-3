def month_name(month, language):
    eng = ['January', 'February', 'March', 'April', 'May', 'June',
           'July', 'August', 'September', 'October', 'November', 'December']
    rus = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
           'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    if language == 'en':
        print(eng[month - 1])
    else:
        print(rus[month - 1])


month_name(int(input()), input())
