from parameters import *
import os, re

numeric_const_pattern = r"""
         [-+]? # optional sign
         (?:
             (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
             |
             (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
         )
         # followed by optional exponent part if desired
         (?: [Ee] [+-]? \d+ ) ?
         """
find = re.compile(numeric_const_pattern, re.VERBOSE)

for j in range(1, no_of_ligands + 1):
    filename1 = 'com_ligand_' + str(j) + '.tcl'
    with open(filename1, "w") as file1:
        file1.write ("mol new ligand_{}.pdb".format(j)                        + "\n")
        file1.write ("set ligand [atomselect top all]"                        + "\n")
        file1.write ("$ligand get name"                                       + "\n")
        file1.write ("set center [measure  center $ligand weight mass]"       + "\n")
        file1.write ("quit"                                                   + "\n")
        
for j in range(1, no_of_ligands + 1):
    command = "vmd -dispdev text -e com_ligand_{}.tcl > com_ligand_{}.txt".format(j,j)
    os.system(command)
    command = ''
        
filename2 = 'com_receptor.tcl'
with open(filename2, "w") as file2:
        file2.write ("mol new receptor.pqr"                                 + "\n")
        file2.write ("set receptor [atomselect top all]"                    + "\n")
        file2.write ("$receptor get name"                                   + "\n")
        file2.write ("set center [measure  center $receptor weight mass]"   + "\n")
        file2.write ("quit"                                                 + "\n")

os.system('vmd -dispdev text -e com_receptor.tcl > com_receptor.txt')

for j in range(1, no_of_ligands + 1):
    filename3 = 'com_ligand_' + str(j) + '.txt'
    file3=open(filename3)
    lines=file3.readlines()
    com_line = lines[-4]
    com_ligand = find.findall(com_line)
    for i in range(0, len(com_ligand)): 
        com_ligand[i] = float(com_ligand[i])
    com_ligand = [round(num, 3) for num in com_ligand]
    com_ligand = str(com_ligand).replace(',', ' ')
    com_ligand = com_ligand.strip(']')
    com_ligand = com_ligand.strip('[')
    filename4 = 'ligand_' + str(j) + '.pqr'
    file4=open(filename4)
    lines=file4.readlines()
    last_line = lines[-1]
    numbers = find.findall(last_line)
    #print(numbers)
    for i in range(0, len(numbers)): 
        numbers[i] = float(numbers[i])
    serial = int(numbers[0])
    last_line_needed = ["ATOM    ", str(serial+1), "LA", " ANO    ",str(111), str(com_ligand), "    0.00", "0.00"]
    last_line_needed = str(last_line_needed).replace(',', '')
    last_line_needed = str(last_line_needed).replace("'", "")
    last_line_needed = last_line_needed.strip(']')
    last_line_needed = last_line_needed.strip('[')
    #print(last_line_needed)
    with open(filename4, "a") as file5:
        file5.write(last_line_needed)


filename6 = 'com_receptor.txt'
file6=open(filename6)
lines=file6.readlines()
com_line = lines[-4]
com_receptor = find.findall(com_line)
for i in range(0, len(com_receptor)): 
    com_receptor[i] = float(com_receptor[i])
com_receptor = [round(num, 4) for num in com_receptor]
com_receptor = str(com_receptor).replace(',', ' ')
com_receptor = com_receptor.strip(']')
com_receptor = com_receptor.strip('[')
#print(com_receptor)
filename7 = 'receptor.pqr'
file7=open(filename7)
lines=file7.readlines()
last_line = lines[-3]
numbers = find.findall(last_line)
#print(numbers)
for i in range(0, len(numbers)): 
    numbers[i] = float(numbers[i])
serial = int(numbers[0])
residueNumber = int(numbers[2])
last_line_needed = ["ATOM  ", str(serial+1), " RA ", "GST ",str(residueNumber + 1) + "     " , str(com_receptor) , "0.0000","0.0000"]
last_line_needed = str(last_line_needed).replace(',', '')
last_line_needed = str(last_line_needed).replace("'", "")
last_line_needed = last_line_needed.strip(']')
last_line_needed = last_line_needed.strip('[')
with open('receptor.pqr') as file8:
    lines = file8.readlines()
with open('receptor.pqr','w') as file9:
    file9.writelines(lines[:-2])
with open("receptor.pqr", "a") as file10:
    file10.write(last_line_needed + "\n")
with open("receptor.pqr", "a+") as file11:
    file11.write("TER"  + "\n")
    file11.write("END"  + "\n")

for j in range(1, no_of_ligands + 1):
    command = 'pqr2xml < ligand_{}.pqr > ligand_{}-atoms.xml'.format(j,j)
    os.system(command)
    command = ''

os.system('pqr2xml < receptor.pqr > receptor-atoms.xml')
