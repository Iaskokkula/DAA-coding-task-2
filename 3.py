n = int(input("Enter an integer: "))
binary = bin(n)[2:]
print("Binary equivalent:", binary)
position = int(input("Enter position to check (0 for last bit): "))
bit = None
if position >= len(binary):
    print("Invalid position!")
else:
    bit = binary[-(position + 1)]
    print("Bit at position", position, "is", bit)
if bit == '1':
    print("True")
else:
    print("False")