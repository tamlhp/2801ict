decimal = 128
binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2
print(binary)