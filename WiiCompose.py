import os

try:
    os.mkdir('OutputWii')
except:
    pass

wiidir=input("Extraxted Wii game directory: ")
os.system('wit copy ExtractWii/'+wiidir+' --dest OutputWii/'+wiidir+'.wbfs')