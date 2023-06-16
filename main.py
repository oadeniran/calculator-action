def add_function(x, y):
    return x + y

def subtract_function(x, y):
    return x - y

def multiply_function(x, y):
    return x * y

def divide_function(x, y):
    return x / y

if __name__ == "__main__":

    print('Welcome calculator')
    print(''' SELECT OPTION (number-only)
            1) Addition
            2) Subtraction
            3) Multiplication
            4) Division
            ''')
    choice = int(input('selection -> '))
    num1 = float(input('Number1 - '))
    num2 = float(input('Number2 - '))
    if choice == 1:
        print(add_function(num1, num2))
    elif choice == 2:
        print(subtract_function(num1, num2))
    elif choice == 3:
        print(multiply_function(num1, num2))
    else:
        print(divide_function(num1, num2))
    
