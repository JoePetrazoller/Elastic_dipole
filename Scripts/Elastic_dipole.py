# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:47:03 2023

@author: petrazol2
"""


import os
import subprocess
import glob
import numpy as np
import math
import pandas as pd
from math import *
from numpy.linalg import inv



global E
global nu
WORKDIR = glob.glob(os. getcwd())[0]

#Inclusion ?
E=130 #GPa
nu = 0.34
E=E*10**9 #Pa

def findline(file_path, word):

    with open(file_path, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        count = 0
        for line in lines:
            count = count+1
            if line.find(word) != -1:
                if line[0:5] == 'print':
                    line = lines[count]
                    return(line)
                else:
                    return(line)


def findword(file_path, word, first, last):
    line = findline(file_path, word)
    try:
        start = line.index(first) + len(first)
        end = line.index(last, start)
        value = line[start:end]
        return value
    except ValueError:
                return ""   


    
    
filename='log_step3.lammps'
with open(filename,'r') as file:
    line=file.readlines()
    

marker = findline(WORKDIR+'\\log_step3.lammps', 'Loop time')


           
for i in range(0,len(line)):
    if line[i]==marker:
        here=i

here=here-1


line_here=line[here].split()


pxx=float(line_here[4])*10**5
pyy=float(line_here[5])*10**5
pzz=float(line_here[6])*10**5
pxy=float(line_here[7])*10**5
pxz=float(line_here[8])*10**5
pyz=float(line_here[9])*10**5

volume=float(line_here[10])
volume=volume*10**-30



P11=pxx*volume*6242000000000000000
P22=pyy*volume*6242000000000000000
P33=pzz*volume*6242000000000000000
P12=pxy*volume*6242000000000000000
P13=pxz*volume*6242000000000000000
P23=pyz*volume*6242000000000000000



print('P11 = '+str(P11) +' eV')
print('P22 = '+str(P22) +' eV')
print('P33 = '+str(P33) +' eV')
print('P12 = '+str(P12) +' eV')
print('P13 = '+str(P13) +' eV')
print('P23 = '+str(P23) +' eV\n')





radius=1.28*10**-10
O=4/3*pi*radius**3
S = np.array([[1/E, -nu/E, -nu/E, 0, 0, 0], [-nu/E, 1/E, -nu/E, 0, 0, 0],[-nu/E, -nu/E, 1/E, 0, 0, 0],[0, 0, 0, (2+2*nu)/E, 0, 0],[0, 0, 0, 0, (2+2*nu)/E, 0],[0, 0, 0, 0, 0, (2+2*nu)/E]])



exx=(S[0][0]*P11+S[0][1]*P22+S[0][2]*P33)*(1/O)
eyy=(S[1][0]*P11+S[1][1]*P22+S[1][2]*P33)*(1/O)
ezz=(S[2][0]*P11+S[2][1]*P22+S[2][2]*P33)*(1/O)

e=exx+eyy+ezz
e=e/6.242e+18

print("dilatation a l'equilibre : " + str(e))