import re
def sorted_nicely(list):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)
list = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.5.jpg', '9.jpg']
print(list)
print(sorted_nicely(list))
print(sorted(list))
print(sorted(list, key=lambda x: float(x[:-4])))