print("🔢 Simple Calculator")

def gtn(): #getting to numbers 
    return float(input("Enter first number: ")), float(input("Enter second number: "))

def gmn():#getting multiple numbers :]
    return list(map(float, input("Enter numbers separated by space: ").split()))

def calculate():
    print("""\nChoose an operation:)
    +  Add")
    -  Subtract
    *  Multiply
    /  Divide
    %  Modulus
    avg (multiple numbers)""")

    op = input("Your choice: ").strip()

    if op == "avg":
        try:
            nums = gmn()
            print("Average:", sum(nums) / len(nums))
        except:
            print("Invalid numbers. Try again.")
    elif op in ["+", "-", "*", "/", "%"]:
        try:
            a, b = gtn()
            if op == "+": print("Result:", a + b)
            elif op == "-": print("Result:", a - b)
            elif op == "*": print("Result:", a * b)
            elif op == "/": print("Result:", a / b if b != 0 else " Cannot divide by zero!")
            elif op == "%": print("Result:", a % b)
        except:
            print("Invalid input. Try again.")
    else:
        print(" Unsupported operation.")

calculate()
