#! /usr/bin/python


import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument("sqare", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# parser.add_argument('-q', '--qqqq', action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.sqare ** 2
# # ass = args.square + answer
# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# # elif args.qqqq:
# #     print ass
# else:
#     print(answer)


# def arg_parser():
#     parser = argparse.ArgumentParser()
def ff():
    return 5

parser = argparse.ArgumentParser()
parser.add_argument("-v")
parser.add_argument('-b')
parser.add_argument('q')
args = parser.parse_args()
if args.v:
    print args.v
elif args.b:
    print int(args.b) + 4
elif args.q:
    print ff()