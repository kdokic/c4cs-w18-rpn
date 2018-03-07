#!/usr/bin/env python3

import operator
import logging
import sys

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def summation(stack):
    total = 0
    while len(stack) > 0:
       total += stack.pop()
    stack.append(total)

def calculate(arg):
    stack = list()
    for token in arg.split():
        logger.debug('token is ' + token)
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if token == 's':
                logger.debug('token is summation')
                summation(stack)
            elif token == 'r':
                logger.debug('rotating')
                stack.reverse()
            elif token == 'c':
                logger.debug('copying')
                stack.append(stack[len(stack) - 1])
            else:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        logger.debug(stack)

    if len(stack) != 1:
        raise TypeError

    return stack.pop()
            

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
