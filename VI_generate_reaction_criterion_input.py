from parameters import *
import os, re, sys
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

filename2 = 'receptor.pqr'
file2=open(filename2)
lines=file2.readlines()
last_line = lines[-3]
numbers_receptor = find.findall(last_line)
#print(numbers_receptor)
ghost_receptor = int(numbers_receptor[0])
#print(ghost_receptor)

from parameters import *
for j in range(1, no_of_ligands + 1):
    filename1 = 'ligand_' + str(j) + '.pqr'
    file1=open(filename1)
    lines=file1.readlines()
    last_line = lines[-1]
    numbers = find.findall(last_line)
    for i in range(0, len(numbers)):
        numbers[i] = float(numbers[i])
    ghost_ligand = int(numbers[0])
    #print(ghost_ligand)
    filename = 'ligand_' + str(j) + '-receptor-rxns.xml'
    with open(filename, "w") as file:
            file.write ("<roottag>"                                                                               + "\n")
            file.write ("  <first-state>start</first-state>"                                                      + "\n")
            file.write ("  <reactions>"                                                                           + "\n")
            file.write ("    <reaction>"                                                                          + "\n")
            file.write ("      <name>bind</name>"                                                                 + "\n")
            file.write ("      <state-before>start</state-before>"                                                + "\n")
            file.write ("      <state-after>end</state-after>"                                                    + "\n")
            file.write ("      <criterion>"                                                                       + "\n")
            file.write ("        <n-needed>1</n-needed>"                                                          + "\n")
            file.write ("        <pair>"                                                                          + "\n")
            file.write ("          <atoms>" + str(ghost_receptor) + " " +  str(ghost_ligand) +  "</atoms>"        + "\n")
            file.write ("          <distance>" + str((reaction_distance_1)) + "</distance>"                       + "\n")
            file.write ("        </pair>"                                                                         + "\n")
            file.write ("      </criterion>"                                                                      + "\n")
            file.write ("    </reaction>"                                                                         + "\n")
            file.write ("  </reactions>"                                                                          + "\n")
            file.write ("</roottag>"                                                                              + "\n")
