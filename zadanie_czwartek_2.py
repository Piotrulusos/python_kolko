user_input = int(input('Give number in range of [101 - 99999]: '))


if 100 < user_input < 100000:
    print('Your reverse number: ' + str(user_input)[::-1])
else:
    print('Number out of range')
