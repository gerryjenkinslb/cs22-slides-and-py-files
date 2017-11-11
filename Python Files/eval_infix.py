from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):  # fix this code to do floats
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):  # also fix this to do floats
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

def eval_infix(s):
    '''to do replace this line with your code '''


### Keep all this code AS-IS, do not modify
###   This code runs a unit test and will report errors
###   when it detects your result is different than the expected result
###
### do not modify the following, if you get an error, it is in
### your code

import math

import unittest
class TestEvalInfix(unittest.TestCase):

    def setUp(self):
        self.tests = tests = (
            "1", "1 + 2", "3 * 2 + 1", "1 + 2 * 3",
            "( 0.5 + 1.5 + 2.0 )", "( 2.0 * 3 ) - 1",
            "( 1.0 - .5 ) * ( 2.5 / .5 )", "( 1 ) * ( .33333333 ) * ( 3.00000 )"
        )

    def test_expressions(self):
        for expression in self.tests:
            print("Testing expression '%s'" % (expression))
            expected = eval(expression)
            got = eval_infix(expression)
            self.assertAlmostEqual( got, expected, "got: "+ str(got) + " expect: " + str(expected) )
#                             "Expression '%s' resulted in value %.4f, expected value was %.4f" %
#                             (expression,got,expected) )

if __name__ == '__main__':
    print("STARTING TESTS")
    unittest.main()
