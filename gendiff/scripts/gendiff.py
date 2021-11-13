#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')

    #args = parser.parse_args()
    #print(args.accumulate(args.first_file, args.second_file))
    parser.print_help()


if __name__ == '__main__':
    main()