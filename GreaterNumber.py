# GreaterNumber.py

def find_greater_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal."

# Example usage
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = find_greater_number(num1, num2)
        print(f"The greater number is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
