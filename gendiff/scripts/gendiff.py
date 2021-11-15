#!/usr/bin/env python

import argparse
from gendiff.scripts.generate_diff import make_diff_str


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    # print(args.accumulate(args.first_file, args.second_file))
    # parser.print_help()

    print(make_diff_str(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
