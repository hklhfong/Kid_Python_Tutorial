def fizz_buzz(input):
    int_input = int(input)
    if int_input % 3 == 0 and int_input % 5 != 0:
        return 'Fizz'
    elif int_input % 5 == 0 and int_input % 3 != 0: 
        return 'Buzz'
    elif int_input % 3 == 0 and int_input % 5 == 0:
        return 'Fizz Buzz'
    else :
        return input

value = ''
while value != 'end':
    value = input("Enter value:")
    print(fizz_buzz(value))



    