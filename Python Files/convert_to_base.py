
def toStr(n,base):
    digits = '01234567890ABCDEF'
    if n < base:
        return digits[n]
    return toStr(n // base,base) + digits[n % base]

print("9145 in hex is   ", toStr(9145,16))


