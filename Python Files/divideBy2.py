from pythonds.basic.stack import Stack

'''
:param decNumber: value to convert to binary
:return: string displaying binary value for decNumber
'''

def divide_by_2(dec_number):

    rem_stack = Stack()

    while dec_number > 0:
        remainder = dec_number % 2
        rem_stack.push(remainder)
        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.isEmpty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print("42 is " + divide_by_2(42))

assert divide_by_2(2) == '10'
assert divide_by_2(255) == "11111111"
assert divide_by_2(8+1) == "1001"
