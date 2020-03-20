import os, re, itertools
import numpy as np
import matplotlib.pyplot as plt
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
    command = "compute_rate_constant < receptor_ligand_{}_results.xml > rate_constant_{}.txt".format(j,j)
    os.system(command)
    command = ''
    
rate_constants=[]
for j in range(1, no_of_ligands + 1):
    f=open('rate_constant_' + str(j) + '.txt')
    lines=f.readlines()
    needed_line = find.findall(lines[6])
    rate_constants.append(needed_line)
    
rate_constant = list(itertools.chain.from_iterable(rate_constants))
for i in range(0, len(rate_constant)): 
    rate_constant[i] = float(rate_constant[i])
    
list_ligands = []
for j in range(1, no_of_ligands + 1):
    list_ligands.append("Lig"+ str(j))
    
rate_constant_array  = np.array(rate_constant)
#print(rate_constant_array)
rate_constant_array_sorted = np.sort(rate_constant_array)
#print(rate_constant_array_sorted)
index_sorted = np.argsort(rate_constant_array)
#index_sorted
sorted_list_ligands = []
for j in index_sorted:
    sorted_list_ligands.append("Lig"+ str(j))
    
y = rate_constant_array_sorted
x = sorted_list_ligands
fig = plt.figure(figsize=(18,12))
ax = fig.add_subplot(111)
plt.plot(x,y,'bs')
plt.title("Rate Constant for Different Ligands")
plt.ylabel("Rate Constant (1 /M s)")
plt.xlabel("Ligand")
y1 = [j/100000000 for j in y]
y2 = [round(num, 4) for num in y1]
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j))
plt.show()
fig.savefig("sorted_Rate_Constants.png")
