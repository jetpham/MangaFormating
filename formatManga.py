from Format import purge
from Format import rename
from Format import convert
from Format import landscape
from Format import map
from Format import chaptersToPDF
from Format import masterPDF
from Format import clearMap

manga = 'Food'
user = 'Jet Pham'
mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
mapPath = 'map.txt'

purge.purge(manga, mangaPath)
rename.rename(manga, mangaPath)
convert.convert(manga, mangaPath)
landscape.lanscape(manga, mangaPath)
map.map(manga, mangaPath, mapPath)
chaptersToPDF.chaptersToPDF(manga, mangaPath, mapPath)
masterPDF.merge_pdfs(mangaPath)
clearMap.clearMap(mapPath)
