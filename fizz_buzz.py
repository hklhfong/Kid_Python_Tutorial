def fizz_buzz(num):
    int_input = int(num)
    if int_input % 3 == 0 and int_input % 5 != 0:
        return 'Fizz'
    elif int_input % 5 == 0 and int_input % 3 != 0:
        return 'Buzz'
    elif int_input % 3 == 0 and int_input % 5 == 0:
        return 'Fizz Buzz'
    else:
        return num

if __name__ == "__main__":
    value = ''
    while value != 'end':
        value = input("Enter value:")
        print(fizz_buzz(value))
