import os
from parameters import *

for j in range(1, no_of_ligands + 1):
        make_folders = "mkdir ligand_{}".format(j)
        os.system(make_folders)
        command = ''

for j in range(1, no_of_ligands + 1):
    command = "bd_top ligand_input_{}.xml ".format(j)
    os.system(command)
    command = ''

for j in range(1, no_of_ligands + 1):
    command = "nam_simulation receptor-ligand_{}-simulation.xml ".format(j)
    os.system(command)
    move = "mv traj* ligand_{}".format(j)
    os.system(move)
    command = ''             
