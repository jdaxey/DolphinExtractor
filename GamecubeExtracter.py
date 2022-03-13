import os 

try:
    os.mkdir('InputGC')
    os.mkdir('ExtractGC')
except:
    pass

for rom in os.listdir("InputGC/"):
    gcdir=rom.split(' . ')[0]
    os.system('wit extract InputGC/'+rom+' --dest ExtractGC/'+gcdir)