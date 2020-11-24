lastTicket = input()


def lucky(ticket):
    global lastTicket
    while len(lastTicket) < 6:
        lastTicket = '0' + lastTicket
    while len(ticket) < 6:
        ticket = '0' + ticket
    f_part_n = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    s_part_n = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    f_part_p = int(lastTicket[0]) + int(lastTicket[1]) + int(lastTicket[2])
    s_part_p = int(lastTicket[3]) + int(lastTicket[4]) + int(lastTicket[5])
    if (f_part_n == s_part_n) and (s_part_p == f_part_p):
        print('Счастливый')
    else:
        print('Несчастливый')


lucky(input())
