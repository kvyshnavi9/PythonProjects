import logo

print(logo.calc_logo)
continue_operation = False
result = 0
sum = 0

def calc_fn(num1, num2, operation):
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
            result = first_num - second_num
    elif operation == "*":
            result = first_num * second_num
    elif operation == "/":
            result = first_num / second_num
    else:
            print("Invalid operation")
            result = None
    print(f"{first_num} {operation} {second_num} = {result}")
    return result

first_num = float(input("What's the first number \n"))
while not continue_operation:
    operation = input("+ \n*\n-\n/\nwhat's the operation? \n")
    second_num = float(input("What's the next number \n"))
    result = calc_fn(first_num, second_num, operation)
    
    fur_op = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation \n")
    if fur_op == "y":
        first_num = result
        continue_operation = False
    elif fur_op == "n":
        continue_operation = True
    else:
        continue_operation = True
        
    