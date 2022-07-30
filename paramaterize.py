import os
# Save the tleap script to file that checks for the initial charge of the system

with open('initial_charge.leap', 'w') as f:
    f.write('''
source leaprc.protein.ff19SB
source leaprc.gaff
source leaprc.water.tip4pew
loadAmberParams frcmod.ionsjc_tip4pew
loadAmberParams frcmod.tip4pew
pdb = loadpdb ntl9.pdb
charge pdb
quit
''')

# Check initial charge 
os.system("tleap -f initial_charge.leap")

# Save the tleap script to file that solvates the system
with open('prepare.leap', 'w') as f:
    f.write('''
source leaprc.protein.ff19SB
source leaprc.gaff
source leaprc.water.tip4pew
set default FlexibleWater on
set default PBRadii mbondi2
WAT = T4E
HOH = T4E
loadAmberParams frcmod.ionsjc_tip4pew
loadAmberParams frcmod.tip4pew
pdb = loadpdb ntl9.pdb
solvateBox pdb TIP4PEWBOX 15
charge pdb
addions2 pdb Na+ 13
addions2 pdb Cl- 17
charge pdb
saveamberparm pdb system.prmtop system.inpcrd
saveamberparm pdb system.parm7 system.rst7
savepdb pdb system.pdb
quit
''')

# Solvate the system
os.system("tleap -f prepare.leap")

# Save the tleap script to file that checks for the final charge of the system

with open('check_final_charge.leap', 'w') as f:
    f.write('''
source leaprc.protein.ff19SB
source leaprc.gaff
source leaprc.water.tip4pew
loadAmberParams frcmod.ionsjc_tip4pew
loadAmberParams frcmod.tip4pew
pdb = loadpdb system.pdb
charge pdb
quit
''')

# Check initial charge 
os.system("tleap -f check_final_charge.leap")

os.system("rm -rf leap.log initial_charge.leap check_final_charge.leap prepare.leap")
