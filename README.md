&cntrl
  imin = 0, irest = 0, ntx = 1,
  nstlim = 251000000, dt = 0.002,
  ntc = 2, ntf = 2, tol = 0.000001,
  iwrap = 1, ntb = 1, cut = 8.0,
  ntt = 3, temp0 = 300.0, gamma_ln = 1.0,
  ntpr = 500, ntwx = 1000, ntwr = 500,
  ntxo = 2, ioutfm = 1, ig = -1, ntwprt = 0,
  igamd = 3, iE = 2, irest_gamd = 0,
  ntcmd = 1000000, nteb = 1000000, ntave = 50000,
  ntcmdprep = 200000, ntebprep = 200000,
  sigma0D = 6.0, sigma0P = 6.0
&end


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
1. PDB files of all the ligands (sequentially numbered from 1-n for n belonging to any integer) in the ligands folder
2. PDB file of the receptor named as receptor.pdb

What does the scripts do:
1. Obtain PQR files for the two molecules (Ligand and Receptor in our case).
2. Convert PQR files to equivalent XML files.
3. Obtain electrostatic fields for both molecules in openDX format using APBS software.
4. Generate files defining the reaction criteria.
5. Prepare an input file for the front end program bd top.
6. Run single trajectory simulations using nam simulation (Northup-Alison-McCommon Algorithm).
7. Calculate the second reaction rate constant.

To run the scripts, simply run the commands.py python file which will run all the scripts sequentially and performa the analysis. 
To make any changes in the parameters, make changes to the parameters.py parameters file. 

