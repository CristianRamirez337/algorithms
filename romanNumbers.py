'''
Cristian Aurelio Ramírez Anzaldo
A01066337
Examen 2do parcial
'''

numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

exceptions = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

romans = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'

}

option = int(input("1. Roman to integer\n2. Integer to roman: \n"))

if option == 1:
    roman = input("Enter roman number: ").upper()
    num = 0
    temp = ''

    for i in roman:
        if exceptions.get(temp + i):
            num = num - numbers[temp] + exceptions[temp + i]
            temp = ''
        elif numbers.get(i):
            num = num + numbers.get(i)
            temp = i
    print(num)

elif option == 2:
    dividers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    integer = int(input("Enter integer number: "))

    for i in dividers:
        num = int(integer/i)
        integer = integer - num*i
        for j in range(num):
            print(romans.get(i), end='')

else:
    print("No valid option selected")