import argparse
import logging

parser = argparse.ArgumentParser()
# two integers
parser.add_argument("n", help="the first number", type=int)
parser.add_argument("m", help="the second number", type=int)
# a string, limited to a list of options
parser.add_argument("op", help="the desired arithmetic operation", choices=['add', 'sub', 'mul', 'div', 'mod'])
# an optional flag, true by default, with a short and a long name
parser.add_argument("-v", "--verbose", help="turn on verbose output", action="store_true")

opts = parser.parse_args()

if opts.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.debug("First number: %d" % opts.n)
logging.debug("Second number: %d" % opts.m)
logging.debug("Operation: %s" % opts.op)

if opts.op == "add":
    result = opts.n + opts.m
elif opts.op == "sub":
    result = opts.n - opts.m
elif opts.op == "mul":
    result = opts.n * opts.m
elif opts.op == "div":
    result = opts.n / opts.m
elif opts.op == "mod":
    result = opts.n % opts.m

print(result)