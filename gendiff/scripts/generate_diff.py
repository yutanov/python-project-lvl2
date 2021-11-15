#!/usr/bin/env python

import json


def make_diff_str(file_one, file_two):
    file_one = json.load(open(file_one))
    file_two = json.load(open(file_two))
    diff_str = ''
    keys = list(file_one.keys() | file_two.keys())
    for key in sorted(keys):
        diff_str += compare_values(key, file_one, file_two)
        diff_str += '\n'
    return diff_str


def compare_values(key, file_one, file_two):
    first_value = file_one.get(key)
    second_value = file_two.get(key)

    if second_value is None:
        return '- {0} : {1}'.format(key, first_value)

    elif first_value is None:
        return '+ {0} : {1}'.format(key, second_value)
    elif second_value == first_value:
        return '  {0} : {1}'.format(key, first_value)
    elif second_value != first_value:
        return '''- {0} : {1}
+ {0} : {2}'''.format(key, first_value, second_value)
