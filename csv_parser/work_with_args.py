#! /usr/bin/python


import argparse
from csv_parser import test_counter


def all_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v')
    parser.add_argument('-b')
    args = parser.parse_args()
    return args


def main():
    args = all_args()
    if args.v:
        return test_counter(args.v)
    elif args.b:
        return test_counter(args.b, False)


if __name__ == '__main__':
    print main()
