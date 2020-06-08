import os
import os.path
import re

array = ['1','2','3','3.5','4','5']

def sorted_nicely(list):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)

print(sorted_nicely(array))