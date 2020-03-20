from parameters import *
import os, sys,re
import pandas as pd
from mendeleev import element 
import itertools

def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)

for j in range(1, no_of_ligands + 1):
    command = "antechamber -i ligand_{}.pdb -fi pdb -o ligand_{}.mol2 -fo mol2 -c bcc -s 2".format(j,j)
    os.system(command) 
    with open('sqm.out') as input_data:
            for line in input_data:
                if 'Atom    Element       Mulliken Charge' in line:
                    break
            for line in input_data:
                if 'Total Mulliken Charge' in line:
                    break
                #print(line)  
                file=open("charges.txt","a")
                s = str(line)
                file.write(s+"\n")
                file.close()
    remove_empty_lines('charges.txt')
    with open('sqm.out') as input_data:
        for line in input_data:
            if 'Final Structure' in line:
                break
        for line in input_data:  
            if 'Calculation Completed' in line:
                break
            file=open("coordinates.txt","a")
            s = str(line)
            file.write(s+"\n")
            file.close()
    remove_empty_lines('coordinates.txt')
    with open('coordinates.txt', 'r') as f:
        data = f.read().splitlines(True)
    with open('coordinates.txt', 'w') as f:
        f.writelines(data[2:])
        
    df1 = pd.read_table('charges.txt', sep='\s+', header = None)
    df2 = pd.read_table('coordinates.txt', sep='\s+', header = None)
    recordName = pd.DataFrame(['ATOM'] * len(df1[0]))
    atomName = df1[[1]]
    residueName = pd.DataFrame(['ANO'] * len(df1[0]))
    residueNumber = pd.DataFrame([111] * len(df1[0]))
    X = df2[[4]].round(3)
    Y = df2[[5]].round(3)
    Z = df2[[6]].round(3)
    charge = df1[[2]].round(2)
    charge.columns = ['charges']
    atom_list = atomName[1]
    radius_list = []
    for k in atom_list:
        radius_list.append(element(k).atomic_radius_rahm /100)
    radius = pd.DataFrame(radius_list) 
    df = pd.concat([recordName,atomName,residueName,residueNumber,X,Y,Z,charge,radius], axis=1)  
    df.columns = ['recordName','atomName','residueName','residueNumber','X','Y','Z','charge','radius']
    df3 = df.sort_values(by=['atomName'])
    unique_list = list(df3.atomName.unique())
    dfs = dict(tuple(df3.groupby('atomName')))
    unique_atom_list = []
    for m in range(len(unique_list)):
        unique_atom_list.append(list(dfs[unique_list[m]]['atomName']))
    unique_atom_list_original = []
    for m in range(len(unique_list)):
        unique_atom_list_original.append(list(dfs[unique_list[m]]['atomName']))
    for l in range(len(unique_atom_list)):
        for m in range(len(unique_atom_list[l])):
            unique_atom_list[l][m] = unique_atom_list[l][m] + str(m)
            unique_atom_list[l][0] = unique_atom_list_original[l][0]
    atomlist = list(itertools.chain.from_iterable(unique_atom_list))
    serials = list(range(1, len(df3)+ 1))
    df4 = df3.drop(['atomName'], axis=1)
    df5 = df4.assign(atomName = atomlist) 
    df6 = df5.assign(serial = serials)
    df7 = df6[['recordName', 'serial','atomName','residueName','residueNumber','X','Y','Z','charge','radius']]
    df7.to_csv('pqr_ligand.pqr', sep=' ', index=False, header = None)
    file1 = open('pqr_ligand.pqr', 'r') 
    lines_all = file1.readlines() 
    for i in range(len(lines_all)): 
        words = lines_all[i].split()
        lines_all[i] = '{:>0} {:>6} {:<3} {:<3} {:>7} {:>6} {:>7} {:>7} {:>7} {:>2}'.format(*words)
    with open('ligand_' + str(j) + '.pqr', 'w') as f2:
        for items in lines_all:
            f2.write('%s\n' % items)
    os.system('rm -rf pqr_ligand.pqr charges.txt coordinates.txt sqm.in sqm.out sqm.pdb ANTECHAMBER_AC.AC ANTECHAMBER_AC.AC0 ANTECHAMBER_AM1BCC.AC ANTECHAMBER_AM1BCC_PRE.AC ANTECHAMBER_BOND_TYPE.AC ANTECHAMBER_BOND_TYPE.AC0 ATOMTYPE.INF')
    command = ''
    
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
    filename = 'ligand_' + str(j) + '.in'
    with open(filename, "w") as file:
            file.write ("read"                                           + "\n") 
            file.write ("    mol pqr ligand_{}.pqr ".format(j)           + "\n")
            file.write ("end"                                            + "\n")
            file.write ("elec name acc"                                  + "\n") 
            file.write ("    mg-auto"                                    + "\n") 
            file.write ("    dime"                                       + "\n") 
            file.write ("    cglen"                                      + "\n") 
            file.write ("    fglen"                                      + "\n") 
            file.write ("    cgcent mol 1"                               + "\n") 
            file.write ("    fgcent mol 1"                               + "\n") 
            file.write ("    mol 1"                                      + "\n") 
            file.write ("    lpbe"                                       + "\n") 
            file.write ("    bcfl sdh"                                   + "\n") 
            file.write ("    pdie 2.0"                                   + "\n") 
            file.write ("    sdie 78.0"                                  + "\n") 
            file.write ("    srfm smol"                                  + "\n") 
            file.write ("    chgm spl2"                                  + "\n") 
            file.write ("    sdens 10.0"                                 + "\n") 
            file.write ("    srad 0.0"                                   + "\n") 
            file.write ("    swin 0.3"                                   + "\n") 
            file.write ("    temp 298"                                   + "\n") 
            file.write ("    calcenergy total"                           + "\n") 
            file.write ("    calcforce no"                               + "\n") 
            file.write ("    write pot dx ligand_{}".format(j)           + "\n") 
            file.write ("end"                                            + "\n") 
            file.write ("quit"                                           + "\n")    
            
for j in range(1, no_of_ligands + 1):
    command = 'python2.7 /software/repo/moleculardynamics/apbs/2018.2.1/share/apbs/tools/manip/psize.py --cfac=3.5 --fadd=50  ligand_{}.pqr > ligand_apbs_{}.txt'.format(j,j)
    os.system(command)
    command = ''
    
for j in range(1, no_of_ligands + 1):
    filename = 'ligand_apbs_' + str(j) + '.txt'
    f=open(filename)
    lines=f.readlines()
    cglen = lines[22]
    cglen_list= find.findall(cglen)
    for i in range(0, len(cglen_list)): 
        cglen_list[i] = float(cglen_list[i])
    print(cglen_list)
    fglen = lines[23]
    fglen_list= find.findall(fglen)
    for i in range(0, len(fglen_list)): 
        fglen_list[i] = float(fglen_list[i])
    print(fglen_list)
    dime = lines[24]
    dime_list= find.findall(dime)
    for i in range(0, len(dime_list)): 
        dime_list[i] = float(dime_list[i])
    print(dime_list)
    dime = "dime " + str(tuple(dime_list)).strip("()")
    dime = dime.replace(',', '')
    cglen = "cglen " + str(tuple(cglen_list)).strip("()")
    cglen = cglen.replace(',', '')
    fglen = "fglen " + str(tuple(fglen_list)).strip("()")
    fglen = fglen.replace(',', '')
    print(dime)
    print(cglen)
    print(fglen)
    filename2 = 'ligand_' + str(j) + '.in'
    lines = open(filename2).read().splitlines()
    lines[5] = "    " + repr(dime).strip("'") 
    lines[6] = "    " + repr(cglen).strip("'") 
    lines[7] = "    " + repr(fglen).strip("'") 
    open(filename2,'w').write('\n'.join(lines))
    
for j in range(1, no_of_ligands + 1):
    command = 'apbs ligand_{}.in > ligand_{}_apbs.out'.format(j,j)
    os.system(command)
    command = ''

