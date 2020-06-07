import os
import os.path
from os import path
import shutil
from PIL import Image
import re

nums = []
nums1 = []
dir = 'Warch'

for n in ['../Warch/1.pdf', '../Warch/10.pdf', '../Warch/10-5.pdf', '../Warch/2.pdf', '../Warch/3.pdf',
          '../Warch/4.pdf', '../Warch/5.pdf', '../Warch/5-5.pdf', '../Warch/6.pdf', '../Warch/7.pdf', '../Warch/8.pdf',
          '../Warch/9.pdf', '../Warch/100.pdf', '../Warch/101.pdf', '../Warch/101-1.pdf', '../Warch/92.pdf',
          '../Warch/93.pdf', '../Warch/94.pdf', '../Warch/95.pdf', '../Warch/96.pdf', '../Warch/97.pdf',
          '../Warch/98.pdf', '../Warch/99.pdf', '../Warch/102.pdf', '../Warch/103.pdf', '../Warch/104.pdf',
          '../Warch/105.pdf', '../Warch/106.pdf', '../Warch/107.pdf', '../Warch/108.pdf', '../Warch/109.pdf',
          '../Warch/109-1.pdf', '../Warch/110.pdf', '../Warch/111.pdf', '../Warch/111-1.pdf', '../Warch/112.pdf',
          '../Warch/113.pdf', '../Warch/114.pdf', '../Warch/115.pdf', '../Warch/116.pdf', '../Warch/117.pdf',
          '../Warch/118.pdf', '../Warch/119.pdf', '../Warch/120.pdf', '../Warch/121.pdf', '../Warch/121-1.pdf',
          '../Warch/122.pdf', '../Warch/123.pdf', '../Warch/124.pdf', '../Warch/125.pdf', '../Warch/126.pdf',
          '../Warch/127.pdf', '../Warch/128.pdf', '../Warch/129.pdf', '../Warch/130.pdf', '../Warch/131.pdf',
          '../Warch/131-1.pdf', '../Warch/132.pdf', '../Warch/133.pdf', '../Warch/134.pdf', '../Warch/135.pdf',
          '../Warch/136.pdf', '../Warch/137.pdf', '../Warch/138.pdf', '../Warch/139.pdf', '../Warch/140.pdf',
          '../Warch/141.pdf', '../Warch/141-1.pdf', '../Warch/142.pdf', '../Warch/143.pdf', '../Warch/144.pdf',
          '../Warch/145.pdf', '../Warch/146.pdf', '../Warch/147.pdf', '../Warch/148.pdf', '../Warch/149.pdf',
          '../Warch/150.pdf', '../Warch/151.pdf', '../Warch/151-1.pdf', '../Warch/152.pdf', '../Warch/153.pdf',
          '../Warch/154.pdf', '../Warch/155.pdf', '../Warch/156.pdf', '../Warch/157.pdf', '../Warch/158.pdf',
          '../Warch/159.pdf', '../Warch/160.pdf', '../Warch/161.pdf', '../Warch/161-1.pdf', '../Warch/162.pdf',
          '../Warch/163.pdf', '../Warch/164.pdf', '../Warch/165.pdf', '../Warch/166.pdf', '../Warch/167.pdf',
          '../Warch/168.pdf', '../Warch/169.pdf', '../Warch/170.pdf', '../Warch/171.pdf', '../Warch/171-1.pdf',
          '../Warch/172.pdf', '../Warch/172-1.pdf', '../Warch/173.pdf', '../Warch/174.pdf', '../Warch/175.pdf',
          '../Warch/176.pdf', '../Warch/177.pdf', '../Warch/178.pdf', '../Warch/179.pdf', '../Warch/180.pdf',
          '../Warch/181.pdf', '../Warch/182.pdf', '../Warch/183.pdf', '../Warch/184.pdf', '../Warch/185.pdf',
          '../Warch/186.pdf', '../Warch/187.pdf', '../Warch/11.pdf', '../Warch/12.pdf', '../Warch/13.pdf',
          '../Warch/14.pdf', '../Warch/15.pdf', '../Warch/16.pdf', '../Warch/17.pdf', '../Warch/18.pdf',
          '../Warch/19.pdf', '../Warch/20.pdf', '../Warch/20-5.pdf', '../Warch/21.pdf', '../Warch/22.pdf',
          '../Warch/23.pdf', '../Warch/24.pdf', '../Warch/25.pdf', '../Warch/26.pdf', '../Warch/27.pdf',
          '../Warch/27-5.pdf', '../Warch/28.pdf', '../Warch/29.pdf', '../Warch/30.pdf', '../Warch/30-5.pdf',
          '../Warch/31.pdf', '../Warch/32.pdf', '../Warch/33.pdf', '../Warch/34.pdf', '../Warch/35.pdf',
          '../Warch/36.pdf', '../Warch/37.pdf', '../Warch/38.pdf', '../Warch/39.pdf', '../Warch/40.pdf',
          '../Warch/40-5.pdf', '../Warch/41.pdf', '../Warch/42.pdf', '../Warch/43.pdf', '../Warch/44.pdf',
          '../Warch/45.pdf', '../Warch/45-5.pdf', '../Warch/46.pdf', '../Warch/46-5.pdf', '../Warch/47.pdf',
          '../Warch/48.pdf', '../Warch/49.pdf', '../Warch/50.pdf', '../Warch/50-5.pdf', '../Warch/51.pdf',
          '../Warch/52.pdf', '../Warch/53.pdf', '../Warch/54.pdf', '../Warch/55.pdf', '../Warch/56.pdf',
          '../Warch/57.pdf', '../Warch/58.pdf', '../Warch/59.pdf', '../Warch/60.pdf', '../Warch/60-1.pdf',
          '../Warch/61.pdf', '../Warch/62.pdf', '../Warch/63.pdf', '../Warch/64.pdf', '../Warch/64-5.pdf',
          '../Warch/65.pdf', '../Warch/66.pdf', '../Warch/67.pdf', '../Warch/68.pdf', '../Warch/69.pdf',
          '../Warch/70.pdf', '../Warch/70-1.pdf', '../Warch/71.pdf', '../Warch/72.pdf', '../Warch/73.pdf',
          '../Warch/74.pdf', '../Warch/75.pdf', '../Warch/76.pdf', '../Warch/77.pdf', '../Warch/78.pdf',
          '../Warch/79.pdf', '../Warch/80.pdf', '../Warch/80-1.pdf', '../Warch/81.pdf', '../Warch/82.pdf',
          '../Warch/83.pdf', '../Warch/83-5.pdf', '../Warch/83-51.pdf', '../Warch/84.pdf', '../Warch/85.pdf',
          '../Warch/86.pdf', '../Warch/87.pdf', '../Warch/88.pdf', '../Warch/89.pdf', '../Warch/90.pdf',
          '../Warch/91.pdf', '../Warch/91-1.pdf']:
    nums.append(n)


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def sorted_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]


for n in sorted_nicely(nums):
    # float(re.sub('[^0-9]', '', n))
    nums1.append(re.sub('[^0-9^-]', '', n))
nums = nums1
nice = False
for n in nums1:
    if nice:
        nice = False
        continue
    if '-' in n:
        print(n)
        swapPositions(nums1, nums1.index(n), nums1.index(n) + 1)
        nice = True
for n in nums1:
    nums[nums.index(n)] = '../Warch/'+n+'.pdf'
# for n in Remove(nums1):
#     if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#         print(n - 1)
#         n = n - 1
#         if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#             print(n - 1)
#             n = n - 1
#             if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#                 print(n - 1)
#                 n = n - 1
#                 if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#                     print(n - 1)
#                     n = n - 1
#                     if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#                         print(n - 1)
#                         n = n - 1
#                         if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#                             print(n - 1)
#                             n = n - 1
#                             if not path.exists('../' + dir + '/' + str(n - 1) + '.pdf'):
#                                 print(n - 1)
#                                 n = n - 1
print(nums1)
