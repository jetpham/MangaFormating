import os
import os.path
import re

array = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.5.jpg', '8.jpg', '9.5.jpg', '9.jpg',
         '10.5.jpg']

print(sorted(array, key=lambda x: float(x[:-4])))
sorted(array, key=lambda x: float(x[:-4]))