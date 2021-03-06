def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    number = int(input('enter a number: '))

    while number != 1:
        number = collatz(number)

except ValueError:
    print('error: you can use this program with integers only')
