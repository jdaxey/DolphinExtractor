import os

try:
    os.mkdir('ExtractWii')
    os.mkdir('InputWii')
except:
    pass

for rom in os.listdir("InputWii/"):
    wiidir=rom.split('.')[0]
    os.system('wit extract InputWii/'+rom+' --dest ExtractWii/'+wiidir)
