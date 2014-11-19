def ConvertToHex(dec):
    x = (dec % 15)



        return digits[x]
    return ConvertToHex(rest) + digits[x]

numbers = [0, 11, 16, 32, 33, 41, 45, 678, 574893]
print [ConvertToHex(x) for x in numbers]
print [hex(x) for x in numbers]