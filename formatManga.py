manga = 'Stone'
user = 'Jet Pham'
mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
mapPath = 'map.txt'

from Format import purge

purge.purge(manga, mangaPath)

from Format import rename

rename.rename(manga, mangaPath)

from Format import convert

convert.convert(manga, mangaPath)

from Format import landscape

landscape.lanscape(manga, mangaPath)

from Format import map

map.map(manga, mangaPath, mapPath)

from Format import chaptersToPDF

chaptersToPDF.chaptersToPDF(manga, mangaPath, mapPath, 895, 1300)

from Format import masterPDF

masterPDF.merge_pdfs(mangaPath, mapPath)

from Format import clearMap

clearMap.clearMap(mapPath)
