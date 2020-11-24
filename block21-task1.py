a = input().split()


def from_string_to_list(text, a1):
    text = text.split()
    list = a1 + text
    print(*list)


from_string_to_list(input(), a)
