# task 2 Write a calculator with the following operations: +, -, *, /

input_a = float(input("input number:"))

input_b = float(input("input number:"))

input_c = input("input operation +, -, *, /")

result = 0

if input_c == "+":
    result = input_a + input_b
elif input_c == "-":
    result = input_a - input_b
elif input_c == "*":
    result = input_a * input_b
elif input_c == "/" and input_b > 0:
    result = input_a / input_b
elif input_c == "/" and input_b == 0:
    print("Error: Cannot divide by 0.")

print("Result:", result)
