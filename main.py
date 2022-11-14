from random import randint

random_numbers = randint(1, 256)
print('Wylosowana została liczba z przedziału 1 do 256')
while True:
    answer = int(input('Zgadnij liczbe: '))
    if answer > random_numbers:
        print('za dużo')
    elif answer < random_numbers:
        print('za mało')
    elif answer == random_numbers:
        print('Zgadłeś wylosowaną liczbę!')
        print('Czy chcesz zagrać ponownie? (tak lub nie) ')
        repeat = input('')
        random_numbers = randint(1, 256)
        if repeat == 'nie':
            break
