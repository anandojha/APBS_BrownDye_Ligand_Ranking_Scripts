import os, re, sys
from parameters import *
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
    f=open('ligand_'+ str(j) + '_apbs.out')
    lines=f.readlines()
    debye = lines[84]
    debye_length = find.findall(debye)
    debye_length = str(debye_length)
    debye_length = debye_length.replace('[', '')
    debye_length = debye_length.replace(']', '')
    debye_length = debye_length.replace(']', '')
    debye_length = debye_length.replace("'", '')

    
for j in range(1, no_of_ligands + 1): 
    filename = 'ligand_input_' + str(j) + '.xml'
    with open(filename, "w") as file:
        file.write ("<root>"                                                             + "\n")
        file.write (" <solvent>"                                                         + "\n")
        file.write ("    <dielectric>78</dielectric>"                                    + "\n")
        file.write ("    <debye-length>8</debye-length>"                                 + "\n")
        file.write (" </solvent>"                                                        + "\n")
        file.write (" <output>receptor_ligand_{}_results.xml</output>".format(j)         + "\n")
        file.write (" <start-at-site>false</start-at-site>"                              + "\n")
        file.write (" <trajectory-file>traj</trajectory-file>"                           + "\n")
        file.write (" <include-desolvation-forces>true</include-desolvation-forces>"     + "\n")
        file.write (" <n-trajectories>50000</n-trajectories>"                           + "\n")
        file.write (" <n-threads>10</n-threads>"                                         + "\n")
        file.write ("  <molecule0>"                                                      + "\n")
        file.write ("    <prefix>receptor</prefix>"                                      + "\n")
        file.write ("    <atoms>receptor-atoms.xml</atoms>"                              + "\n")
        file.write ("    <apbs-grids>"                                                   + "\n")
        file.write ("     <grid>receptor.dx</grid>"                                      + "\n")
        file.write ("    </apbs-grids>"                                                  + "\n")
        file.write ("    <solute-dielectric>2.0</solute-dielectric>"                     + "\n")
        file.write ("  </molecule0>"                                                     + "\n")
        file.write ("  <molecule1>"                                                      + "\n")
        file.write ("    <prefix>ligand_{} </prefix>".format(j)                          + "\n")
        file.write ("    <atoms>ligand_{}-atoms.xml</atoms>".format(j)                   + "\n")
        file.write ("    <apbs-grids>"                                                   + "\n")
        file.write ("     <grid>ligand_{}.dx</grid>".format(j)                           + "\n")
        file.write ("    </apbs-grids>"                                                  + "\n")
        file.write ("    <solute-dielectric> 2.0 </solute-dielectric>"                   + "\n")
        file.write ("  </molecule1>"                                                     + "\n")
        file.write ("  <time-step-tolerances>"                                           + "\n")
        file.write ("   <minimum-dx>0.001</minimum-dx>"                                  + "\n")
        file.write ("  </time-step-tolerances>"                                          + "\n")
        file.write ("  <reactions>ligand_{}-receptor-rxns.xml</reactions>" .format(j)    + "\n")
        file.write ("  <seed>11111111</seed>"                                            + "\n")
        file.write ("  <n-trajectories-per-output>1000</n-trajectories-per-output>"      + "\n")
        file.write ("</root>"                                                            + "\n")    
