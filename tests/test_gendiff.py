#import json
from gendiff.scripts.generate_diff import make_diff_str

right_answer = '''- follow : False
  host : hexlet.io
- proxy : 123.234.53.22
- timeout : 50
+ timeout : 20
+ verbose : True
'''

file_one = 'tests/fixtures/file1.json'
file_two = 'tests/fixtures/file2.json'


def test_result():
    assert make_diff_str(file_one, file_two) == right_answer


test_result()
