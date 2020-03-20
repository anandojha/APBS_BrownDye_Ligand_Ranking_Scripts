import re, os
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

os.system('pdb2pqr.py --nodebump --noopt --drop-water --ff=parse --verbose --summary receptor.pdb receptor.pqr')

filename = 'receptor.in'
with open(filename, "w") as file:
    file.write ("read"                                           + "\n")
    file.write ("    mol pqr receptor.pqr"                       + "\n")
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
    file.write ("    write pot dx receptor"                      + "\n")
    file.write ("end"                                            + "\n")
    file.write ("quit"                                           + "\n")

os.system('python2.7 /software/repo/moleculardynamics/apbs/2018.2.1/share/apbs/tools/manip/psize.py --cfac=3.5 --fadd=50 receptor.pqr > receptor_apbs.txt')

filename = 'receptor_apbs.txt'
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
filename2 = 'receptor.in'
lines = open(filename2).read().splitlines()
lines[5] = "    " + repr(dime).strip("'") 
lines[6] = "    " + repr(cglen).strip("'") 
lines[7] = "    " + repr(fglen).strip("'") 
open(filename2,'w').write('\n'.join(lines))

os.system("apbs receptor.in > receptor_apbs.out")
