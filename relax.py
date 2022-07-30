import os
"""
os.system("pmemd.cuda -O -i 1min.in -o 1min.out -p system.prmtop -c system.inpcrd -r 1min.rst7 -inf 1min.info -ref system.inpcrd -x mdcrd.1min")
os.system("pmemd.cuda -O -i 2mdheat.in -o 2mdheat.out -p system.prmtop -c 1min.rst7 -r 2mdheat.rst7 -inf 2mdheat.info -ref 1min.rst7 -x mdcrd.2mdheat")
os.system("pmemd.cuda -O -i 3md.in -o 3md.out -p system.prmtop -c 2mdheat.rst7 -r 3md.rst7 -inf 3md.info -ref 2mdheat.rst7 -x mdcrd.3md")
os.system("pmemd.cuda -O -i 4md.in -o 4md.out -p system.prmtop -c 3md.rst7 -r 4md.rst7 -inf 4md.info -ref 3md.rst7 -x mdcrd.4md")
"""
os.system("pmemd.cuda -O -i 5min.in -o 5min.out -p system.prmtop -c 4md.rst7 -r 5min.rst7 -inf 5min.info -ref 4md.rst7 -x mdcrd.5min")
os.system("pmemd.cuda -O -i 5min.in -o 5min.out -p system.prmtop -c 4md.rst7 -r 5min.rst7 -inf 5min.info -ref 4md.rst7 -x mdcrd.5min")
os.system("pmemd.cuda -O -i 6md.in -o 6md.out -p system.prmtop -c 5min.rst7 -r 6md.rst7 -inf 6md.info -ref 5min.rst7 -x mdcrd.6md")
os.system("pmemd.cuda -O -i 7md.in -o 7md.out -p system.prmtop -c 6md.rst7 -r 7md.rst7 -inf 7md.info -ref 6md.rst7 -x mdcrd.7md")
os.system("pmemd.cuda -O -i 8md.in -o 8md.out -p system.prmtop -c 7md.rst7 -r 8md.rst7 -inf 8md.info -ref 7md.rst7 -x mdcrd.8md")
os.system("pmemd.cuda -O -i 9md.in -o 9md.out -p system.prmtop -c 8md.rst7 -r 9md.rst7 -inf 9md.info -ref 8md.rst7 -x mdcrd.9md")

