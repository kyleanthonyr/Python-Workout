
def to_base10(num, base=16):
    """
    A function that takes a hex number and returns the decimal equivalent.

    Hex to decimal conversion follows the conversion: 
        33B(hex) = (3*16^2) + (3*16^1) + (11*16^0) = 768 + 48 + 11 = 827(base10)
    """

    decimal = 0
    # reverses input and gets power from enumerate
    for power, char in enumerate(reversed(num)):

        # Calculates base 16 to base 10 conversion
        decimal += int(char, base) * (base ** power)

    return decimal


# Convert from base 2
base2_to_decimal = to_base10('0101011', 2)
print(base2_to_decimal)

# Convert from 13
base13_to_decimal = to_base10('AAAAAA', 13)
print(base13_to_decimal)

# Convert from base 16
base16_to_decimal = to_base10('AAAAAA', 16)
print(base16_to_decimal)
