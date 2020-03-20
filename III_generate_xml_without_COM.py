from parameters import *
import os, re

for j in range(1, no_of_ligands + 1):
    command = 'pqr2xml < ligand_{}.pqr > ligand_{}-atoms.xml'.format(j,j)
    os.system(command)
    command = ''

os.system('pqr2xml < receptor.pqr > receptor-atoms.xml')

