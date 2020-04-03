# APBS_BrownDye_Ligand_Ranking_Scripts
Automated Kinetic Rate Calculations and Ranking for Ligand - Receptor Systems

Please go through the Slides.pdf for a better understanding of the testing of the model system.

Open Source Softwares Installation Required: 
1. Python 3 (https://www.anaconda.com/distribution/)
2. NumPy (https://numpy.org/)
3. pandas (https://pandas.pydata.org/)
4. ABPS (https://apbs-pdb2pqr.readthedocs.io/en/latest/apbs/installing.html)
5. Browndye (https://browndye.ucsd.edu/)
6. VMD (https://www.ks.uiuc.edu/Research/vmd/)

What you need before running the scripts:
1. PDB files of all the ligands (sequentially numbered from 1-n for n belonging to any integer) in the Ligands folder
2. PDB file of the receptor named as receptor.pdb

What does the scripts do:
1. Obtain PQR files for the two molecules (Ligand and Receptor in our case).
2. Convert PQR files to equivalent XML files.
3. Obtain electrostatic fields for both molecules in openDX format using APBS software.
4. Generate files defining the reaction criteria.
5. Prepare an input file for the front end program bd top.
6. Run single trajectory simulations using nam simulation (Northup-Alison-McCommon Algorithm).
7. Calculate the second reaction rate constant.

To run the scripts, simply run the parameters.py python file . 
To make any changes in the parameters, make changes to the parameters.py parameters file. 



