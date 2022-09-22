#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    length = len(sys.argv) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == "+":
        res = add(a, b)
    if op == "-":
        res = sub(a, b)
    if op == "*":
        res = mul(a, b)
    if op == "/":
        res = div(a, b)
    print("{:d} {:s} {:d} = {}".format(a, op, b, res))
