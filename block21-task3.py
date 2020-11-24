first = input().split()
second = input().split()


def swap():
    global first
    global second
    first, second = second, first


swap()
print(first, second)
