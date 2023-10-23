def decimal_to_binary_array(decimal_array):
    binary_array = [bin(num)[2:] for num in decimal_array]
    return binary_array

# Example usage:
decimal_numbers = [10, 20, 30, 40]
binary_numbers = decimal_to_binary_array(decimal_numbers)
print(binary_numbers)