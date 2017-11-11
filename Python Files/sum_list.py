
def sum_list(a_list):
    if len(a_list) == 0: # empty
        return 0
    return a_list[0] + sum_list(a_list[1:])

def test_sum(a_list): # I built a testing function
    expected = sum(a_list) # sum builtin to python
    total = sum_list(a_list)
    print("testing sum of ", a_list, " is ", expected)
    assert expected == total, "list: " + str(a_list) + " is " + str(total)


test_sum( [1,2,3,4])
test_sum( [])  # testing special case
test_sum( [10]) # testing special case
test_sum( [ 100, 120, 50, 50, 60 ])