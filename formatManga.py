import os
manga = 'KomiNew'
mangaPath = '%USERPROFILE%/Desktop/' + manga
mapPath = 'map.txt'

from Format import *

purge.purge(manga, mangaPath)

rename.rename(manga, mangaPath)

convert.convert(manga, mangaPath)

landscape.landscape(manga, mangaPath)

map.map(manga, mangaPath, mapPath)

chaptersToPDF.chaptersToPDF(manga, mangaPath, mapPath)

masterPDF.merge_pdfs(mangaPath, mapPath)

clearMap.clearMap(mapPath)
