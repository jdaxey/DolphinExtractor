import os

try:
    os.mkdir('OutputGC')
except:
    pass

wiidir=input("Extraxted GameCube game directory: ")
os.system('wit copy ExtractGC/'+wiidir+' --dest OutputGC/'+wiidir+'.iso')