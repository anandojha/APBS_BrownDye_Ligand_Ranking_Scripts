import os

os.system("python I_generate_ligand_input.py")

os.system ("python II_generate_receptor_input.py")

os.system("python III_generate_xml_without_COM")

os.system("python IV_generate_pqr_com.py")

os.system("python V_generate_browndye_input.py")

os.system("python VI_generate_reaction_criterion_input.py")

os.system("python VII_bd_simulations.py")

os.system("python VIII_analysis.py")
