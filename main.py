
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]


decimal_number = int(input("Enter a decimal number: "))


binary_result = decimal_to_binary(decimal_number)
print(f"Binary representation: {binary_result}")
