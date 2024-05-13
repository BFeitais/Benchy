import re
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})

# ------------------------------------------------------------------------------ BARE METAL

word1 = 'events per second:'

# -----------------------------------------------------------1
with open(".Results/1Baremetal/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU1_1 = line1

with open(".Results/1Baremetal/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU2_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Baremetal/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU1_2 = line1

with open(".Results/2Baremetal/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU2_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Baremetal/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU1_3 = line1

with open(".Results/3Baremetal/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU2_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Baremetal/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU1_4 = line1

with open(".Results/4Baremetal/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU2_4 = line1                                    

# -----------------------------------------------------------5
with open(".Results/5Baremetal/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU1_5 = line1

with open(".Results/5Baremetal/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareCPU2_5 = line1   

word4 = 'transferred'

# -----------------------------------------------------------1
with open(".Results/1Baremetal/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMr_1 = line4

with open(".Results/1Baremetal/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMw_1 = line4

# -----------------------------------------------------------2
with open(".Results/2Baremetal/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMr_2 = line4

with open(".Results/2Baremetal/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMw_2 = line4           

# -----------------------------------------------------------3
with open(".Results/3Baremetal/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMr_3 = line4

with open(".Results/3Baremetal/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMw_3 = line4           

# -----------------------------------------------------------4
with open(".Results/4Baremetal/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMr_4 = line4

with open(".Results/4Baremetal/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMw_4 = line4           

# -----------------------------------------------------------5
with open(".Results/5Baremetal/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMr_5 = line4

with open(".Results/5Baremetal/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            bareRAMw_5 = line4           



word1 = 'read, MiB/s:'
word2 = 'written, MiB/s: '
word3 = 'fsyncs/s:'

# -----------------------------------------------------------1
with open(".Results/1Baremetal/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareMEMr_1 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            bareMEMw_1 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            bareMEMf_1 = line3    
 
# -----------------------------------------------------------2
with open(".Results/2Baremetal/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareMEMr_2 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            bareMEMw_2 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            bareMEMf_2 = line3    
   
# -----------------------------------------------------------3
with open(".Results/3Baremetal/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareMEMr_3 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            bareMEMw_3 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            bareMEMf_3 = line3    
    
# -----------------------------------------------------------4
with open(".Results/4Baremetal/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareMEMr_4 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            bareMEMw_4 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            bareMEMf_4 = line3    
    
# -----------------------------------------------------------5
with open(".Results/5Baremetal/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            bareMEMr_5 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            bareMEMw_5 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            bareMEMf_5 = line3    



word1 = 'Package id 0:'
word2 = 'temp1'
temp1_1 = temp1_2 = temp1_3 = temp1_4 = temp1_5 = None
temp2_1 = temp2_2 = temp2_3 = temp2_4 = temp2_5 = None

# -----------------------------------------------------------1
with open(".Results/1Baremetal/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp1_1 = line1

    if temp1_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp1_1 = line2

with open(".Results/1Baremetal/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp2_1 = line1

    if temp2_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp2_1 = line2                

# -----------------------------------------------------------2
with open(".Results/2Baremetal/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp1_2 = line1

    if temp1_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp1_2 = line2

with open(".Results/2Baremetal/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp2_2 = line1

    if temp2_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp2_2 = line2  
                
# -----------------------------------------------------------3
with open(".Results/3Baremetal/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp1_3 = line1

    if temp1_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp1_3 = line2

with open(".Results/3Baremetal/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp2_3 = line1

    if temp2_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp2_3 = line2   
                
# -----------------------------------------------------------4
with open(".Results/4Baremetal/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp1_4 = line1

    if temp1_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp1_4 = line2

with open(".Results/4Baremetal/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp2_4 = line1

    if temp2_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp2_4 = line2                
             
# -----------------------------------------------------------5
with open(".Results/5Baremetal/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp1_5 = line1

    if temp1_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp1_5 = line2

with open(".Results/5Baremetal/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            temp2_5 = line1

    if temp2_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                temp2_5 = line2                         




bareCPU1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU1_1)]
bareCPU2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU2_1)]
bareRAMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMr_1)]
bareRAMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMw_1)]
bareMEMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMr_1)]
bareMEMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMw_1)]
bareMEMf_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMf_1)]
temp1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp1_1)]
temp2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp2_1)]

bareCPU1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU1_2)]
bareCPU2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU2_2)]
bareRAMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMr_2)]
bareRAMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMw_2)]
bareMEMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMr_2)]
bareMEMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMw_2)]
bareMEMf_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMf_2)]
temp1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp1_2)]
temp2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp2_2)]

bareCPU1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU1_3)]
bareCPU2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU2_3)]
bareRAMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMr_3)]
bareRAMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMw_3)]
bareMEMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMr_3)]
bareMEMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMw_3)]
bareMEMf_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMf_3)]
temp1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp1_3)]
temp2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp2_3)]

bareCPU1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU1_4)]
bareCPU2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU2_4)]
bareRAMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMr_4)]
bareRAMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMw_4)]
bareMEMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMr_4)]
bareMEMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMw_4)]
bareMEMf_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMf_4)]
temp1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp1_4)]
temp2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp2_4)]

bareCPU1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU1_5)]
bareCPU2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareCPU2_5)]
bareRAMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMr_5)]
bareRAMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareRAMw_5)]
bareMEMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMr_5)]
bareMEMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMw_5)]
bareMEMf_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', bareMEMf_5)]
temp1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp1_5)]
temp2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', temp2_5)]


# ------------------------------------------------------------------------------ DOCKER

word1 = 'events per second:'

# -----------------------------------------------------------1
with open(".Results/1Docker/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU1_1 = line1

with open(".Results/1Docker/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU2_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Docker/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU1_2 = line1

with open(".Results/2Docker/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU2_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Docker/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU1_3 = line1

with open(".Results/3Docker/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU2_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Docker/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU1_4 = line1

with open(".Results/4Docker/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU2_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Docker/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU1_5 = line1

with open(".Results/5Docker/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerCPU2_5 = line1

word4 = 'transferred'

# -----------------------------------------------------------1
with open(".Results/1Docker/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMr_1 = line4

with open(".Results/1Docker/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMw_1 = line4

# -----------------------------------------------------------2
with open(".Results/2Docker/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMr_2 = line4

with open(".Results/2Docker/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMw_2 = line4
            
# -----------------------------------------------------------3
with open(".Results/3Docker/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMr_3 = line4

with open(".Results/3Docker/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMw_3 = line4

# -----------------------------------------------------------4
with open(".Results/4Docker/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMr_4 = line4

with open(".Results/4Docker/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMw_4 = line4

# -----------------------------------------------------------5
with open(".Results/5Docker/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMr_5 = line4

with open(".Results/5Docker/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            dockerRAMw_5 = line4

word1 = 'benchy'

# -----------------------------------------------------------1
with open(".Results/1Docker/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerSize_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Docker/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerSize_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Docker/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerSize_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Docker/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerSize_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Docker/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerSize_5 = line1

# -----------------------------------------------------------1
word1 = 'real'

with open(".Results/1Docker/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTime_1 = line1

with open(".Results/1Docker/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerContainerTime_1 = line1            

with open(".Results/1Docker/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTimerm_1 = line1              

# -----------------------------------------------------------2
word1 = 'real'

with open(".Results/2Docker/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTime_2 = line1

with open(".Results/2Docker/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerContainerTime_2 = line1            

with open(".Results/2Docker/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTimerm_2 = line1    
            
# -----------------------------------------------------------3
word1 = 'real'

with open(".Results/3Docker/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTime_3 = line1

with open(".Results/3Docker/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerContainerTime_3 = line1            

with open(".Results/3Docker/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTimerm_3 = line1     
            
# -----------------------------------------------------------4
word1 = 'real'

with open(".Results/4Docker/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTime_4 = line1

with open(".Results/4Docker/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerContainerTime_4 = line1            

with open(".Results/4Docker/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTimerm_4 = line1    
            
# -----------------------------------------------------------5
word1 = 'real'

with open(".Results/5Docker/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTime_5 = line1

with open(".Results/5Docker/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerContainerTime_5 = line1            

with open(".Results/5Docker/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerImageTimerm_5 = line1              
                   

word1 = 'read, MiB/s: '
word2 = 'written, MiB/s: '
word3 = 'fsyncs/s:'

# -----------------------------------------------------------1
with open(".Results/1Docker/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerMEMr_1 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            dockerMEMw_1 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            dockerMEMf_1 = line3       

# -----------------------------------------------------------2
with open(".Results/2Docker/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerMEMr_2 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            dockerMEMw_2 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            dockerMEMf_2 = line3    
            
# -----------------------------------------------------------3
with open(".Results/3Docker/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerMEMr_3 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            dockerMEMw_3 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            dockerMEMf_3 = line3       

# -----------------------------------------------------------4
with open(".Results/4Docker/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerMEMr_4 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            dockerMEMw_4 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            dockerMEMf_4 = line3   
            
# -----------------------------------------------------------5
with open(".Results/5Docker/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockerMEMr_5 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            dockerMEMw_5 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            dockerMEMf_5 = line3         


word1 = 'Package id 0:'
word2 = 'temp1'
dockertemp1_1 = dockertemp1_2 = dockertemp1_3 = dockertemp1_4 = dockertemp1_5 = None
dockertemp2_1 = dockertemp2_2 = dockertemp2_3 = dockertemp2_4 = dockertemp2_5 = None

# -----------------------------------------------------------1
with open(".Results/1Docker/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp1_1 = line1

    if dockertemp1_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp1_1 = line2

with open(".Results/1Docker/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp2_1 = line1

    if dockertemp2_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp2_1 = line2                         
                
# -----------------------------------------------------------2
with open(".Results/2Docker/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp1_2 = line1

    if dockertemp1_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp1_2 = line2

with open(".Results/2Docker/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp2_2 = line1

    if dockertemp2_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp2_2 = line2 
                
# -----------------------------------------------------------3
with open(".Results/3Docker/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp1_3 = line1

    if dockertemp1_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp1_3 = line2

with open(".Results/3Docker/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp2_3 = line1

    if dockertemp2_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp2_3 = line2       
                
# -----------------------------------------------------------4
with open(".Results/4Docker/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp1_4 = line1

    if dockertemp1_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp1_4 = line2

with open(".Results/4Docker/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp2_4 = line1

    if dockertemp2_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp2_4 = line2                              
                       
# -----------------------------------------------------------5
with open(".Results/5Docker/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp1_5 = line1

    if dockertemp1_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp1_5 = line2

with open(".Results/5Docker/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            dockertemp2_5 = line1

    if dockertemp2_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                dockertemp2_5 = line2                              

dockerCPU1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU1_1)]
dockerCPU2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU2_1)]
dockerRAMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMr_1)]
dockerRAMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMw_1)]
dockerMEMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMr_1)]
dockerMEMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMw_1)]
dockerMEMf_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMf_1)]
dockerSize_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerSize_1)]
dockerImageTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         dockerImageTime_1)]
dockerImageTimerm_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     dockerImageTimerm_1)]
dockerContainerTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerContainerTime_1)]
dockertemp1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp1_1)]
dockertemp2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp2_1)]

dockerCPU1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU1_2)]
dockerCPU2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU2_2)]
dockerRAMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMr_2)]
dockerRAMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMw_2)]
dockerMEMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMr_2)]
dockerMEMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMw_2)]
dockerMEMf_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMf_2)]
dockerSize_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerSize_2)]
dockerImageTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         dockerImageTime_2)]
dockerImageTimerm_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     dockerImageTimerm_2)]
dockerContainerTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerContainerTime_2)]
dockertemp1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp1_2)]
dockertemp2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp2_2)]

dockerCPU1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU1_3)]
dockerCPU2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU2_3)]
dockerRAMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMr_3)]
dockerRAMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMw_3)]
dockerMEMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMr_3)]
dockerMEMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMw_3)]
dockerMEMf_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMf_3)]
dockerSize_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerSize_3)]
dockerImageTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         dockerImageTime_3)]
dockerImageTimerm_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     dockerImageTimerm_3)]
dockerContainerTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerContainerTime_3)]
dockertemp1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp1_3)]
dockertemp2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp2_3)]

dockerCPU1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU1_4)]
dockerCPU2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU2_4)]
dockerRAMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMr_4)]
dockerRAMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMw_4)]
dockerMEMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMr_4)]
dockerMEMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMw_4)]
dockerMEMf_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMf_4)]
dockerSize_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerSize_4)]
dockerImageTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         dockerImageTime_4)]
dockerImageTimerm_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     dockerImageTimerm_4)]
dockerContainerTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerContainerTime_4)]
dockertemp1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp1_4)]
dockertemp2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp2_4)]

dockerCPU1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU1_5)]
dockerCPU2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerCPU2_5)]
dockerRAMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMr_5)]
dockerRAMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerRAMw_5)]
dockerMEMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMr_5)]
dockerMEMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMw_5)]
dockerMEMf_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerMEMf_5)]
dockerSize_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerSize_5)]
dockerImageTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         dockerImageTime_5)]
dockerImageTimerm_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     dockerImageTimerm_5)]
dockerContainerTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockerContainerTime_5)]
dockertemp1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp1_5)]
dockertemp2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', dockertemp2_5)]


# ------------------------------------------------------------------------------ PODMAN

word1 = 'events per second:'

# -----------------------------------------------------------1
with open(".Results/1Podman/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU1_1 = line1

with open(".Results/1Podman/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU2_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Podman/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU1_2 = line1

with open(".Results/2Podman/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU2_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Podman/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU1_3 = line1

with open(".Results/3Podman/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU2_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Podman/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU1_4 = line1

with open(".Results/4Podman/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU2_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Podman/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU1_5 = line1

with open(".Results/5Podman/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanCPU2_5 = line1

word4 = 'transferred'

# -----------------------------------------------------------1
with open(".Results/1Podman/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMr_1 = line4

with open(".Results/1Podman/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMw_1 = line4

# -----------------------------------------------------------2
with open(".Results/2Podman/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMr_2 = line4

with open(".Results/2Podman/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMw_2 = line4

# -----------------------------------------------------------3
with open(".Results/3Podman/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMr_3 = line4

with open(".Results/3Podman/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMw_3 = line4

# -----------------------------------------------------------4
with open(".Results/4Podman/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMr_4 = line4

with open(".Results/4Podman/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMw_4 = line4

# -----------------------------------------------------------5
with open(".Results/5Podman/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMr_5 = line4

with open(".Results/5Podman/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            podmanRAMw_5 = line4

word1 = 'benchy'

# -----------------------------------------------------------1
with open(".Results/1Podman/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanSize_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Podman/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanSize_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Podman/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanSize_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Podman/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanSize_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Podman/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanSize_5 = line1


word1 = 'real'

# -----------------------------------------------------------1
with open(".Results/1Podman/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTime_1 = line1      

with open(".Results/1Podman/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTimerm_1 = line1              

with open(".Results/1Podman/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanContainerTime_1 = line1  

# -----------------------------------------------------------2
with open(".Results/2Podman/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTime_2 = line1      

with open(".Results/2Podman/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTimerm_2 = line1              

with open(".Results/2Podman/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanContainerTime_2 = line1  

# -----------------------------------------------------------3
with open(".Results/3Podman/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTime_3 = line1      

with open(".Results/3Podman/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTimerm_3 = line1              

with open(".Results/3Podman/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanContainerTime_3 = line1  

# -----------------------------------------------------------4
with open(".Results/4Podman/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTime_4 = line1      

with open(".Results/4Podman/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTimerm_4 = line1              

with open(".Results/4Podman/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanContainerTime_4 = line1  

# -----------------------------------------------------------5
with open(".Results/5Podman/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTime_5 = line1      

with open(".Results/5Podman/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanImageTimerm_5 = line1              

with open(".Results/5Podman/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanContainerTime_5 = line1  


word1 = 'read, MiB/s: '
word2 = 'written, MiB/s: '
word3 = 'fsyncs/s:'

# -----------------------------------------------------------1
with open(".Results/1Podman/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanMEMr_1 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            podmanMEMw_1 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            podmanMEMf_1 = line3    

# -----------------------------------------------------------2
with open(".Results/2Podman/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanMEMr_2 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            podmanMEMw_2 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            podmanMEMf_2 = line3    

# -----------------------------------------------------------3
with open(".Results/3Podman/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanMEMr_3 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            podmanMEMw_3 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            podmanMEMf_3 = line3    

# -----------------------------------------------------------4
with open(".Results/4Podman/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanMEMr_4 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            podmanMEMw_4 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            podmanMEMf_4 = line3    

# -----------------------------------------------------------5
with open(".Results/5Podman/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmanMEMr_5 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            podmanMEMw_5 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            podmanMEMf_5 = line3    


word1 = 'Package id 0:'
word2 = 'temp1'
podmantemp1_1 = podmantemp1_2 = podmantemp1_3 = podmantemp1_4 = podmantemp1_5 = None
podmantemp2_1 = podmantemp2_2 = podmantemp2_3 = podmantemp2_4 = podmantemp2_5 = None

# -----------------------------------------------------------1
with open(".Results/1Podman/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp1_1 = line1

    if podmantemp1_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp1_1 = line2

with open(".Results/1Podman/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp2_1 = line1

    if podmantemp2_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp2_1 = line2                                                

# -----------------------------------------------------------2
with open(".Results/2Podman/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp1_2 = line1

    if podmantemp1_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp1_2 = line2

with open(".Results/2Podman/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp2_2 = line1

    if podmantemp2_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp2_2 = line2   
                
# -----------------------------------------------------------3
with open(".Results/3Podman/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp1_3 = line1

    if podmantemp1_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp1_3 = line2

with open(".Results/3Podman/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp2_3 = line1

    if podmantemp2_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp2_3 = line2                                                
                                             
# -----------------------------------------------------------4
with open(".Results/4Podman/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp1_4 = line1

    if podmantemp1_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp1_4 = line2

with open(".Results/4Podman/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp2_4 = line1

    if podmantemp2_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp2_4 = line2                                                

# -----------------------------------------------------------5
with open(".Results/5Podman/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp1_5 = line1

    if podmantemp1_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp1_5 = line2

with open(".Results/5Podman/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            podmantemp2_5 = line1

    if podmantemp2_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                podmantemp2_5 = line2                                                


podmanCPU1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU1_1)]
podmanCPU2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU2_1)]
podmanRAMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMr_1)]
podmanRAMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMw_1)]
podmanMEMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMr_1)]
podmanMEMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMw_1)]
podmanMEMf_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMf_1)]
podmanSize_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanSize_1)]
podmanImageTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         podmanImageTime_1)]    
podmanImageTimerm_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     podmanImageTimerm_1)]   
podmanContainerTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanContainerTime_1)]   
podmantemp1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp1_1)]
podmantemp2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp2_1)]

podmanCPU1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU1_2)]
podmanCPU2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU2_2)]
podmanRAMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMr_2)]
podmanRAMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMw_2)]
podmanMEMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMr_2)]
podmanMEMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMw_2)]
podmanMEMf_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMf_2)]
podmanSize_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanSize_2)]
podmanImageTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         podmanImageTime_2)]    
podmanImageTimerm_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     podmanImageTimerm_2)]   
podmanContainerTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanContainerTime_2)]   
podmantemp1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp1_2)]
podmantemp2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp2_2)]

podmanCPU1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU1_3)]
podmanCPU2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU2_3)]
podmanRAMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMr_3)]
podmanRAMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMw_3)]
podmanMEMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMr_3)]
podmanMEMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMw_3)]
podmanMEMf_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMf_3)]
podmanSize_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanSize_3)]
podmanImageTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         podmanImageTime_3)]    
podmanImageTimerm_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     podmanImageTimerm_3)]   
podmanContainerTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanContainerTime_3)]   
podmantemp1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp1_3)]
podmantemp2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp2_3)]

podmanCPU1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU1_4)]
podmanCPU2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU2_4)]
podmanRAMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMr_4)]
podmanRAMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMw_4)]
podmanMEMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMr_4)]
podmanMEMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMw_4)]
podmanMEMf_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMf_4)]
podmanSize_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanSize_4)]
podmanImageTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         podmanImageTime_4)]    
podmanImageTimerm_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     podmanImageTimerm_4)]   
podmanContainerTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanContainerTime_4)]   
podmantemp1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp1_4)]
podmantemp2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp2_4)]

podmanCPU1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU1_5)]
podmanCPU2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanCPU2_5)]
podmanRAMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMr_5)]
podmanRAMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanRAMw_5)]
podmanMEMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMr_5)]
podmanMEMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMw_5)]
podmanMEMf_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanMEMf_5)]
podmanSize_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanSize_5)]
podmanImageTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         podmanImageTime_5)]    
podmanImageTimerm_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     podmanImageTimerm_5)]   
podmanContainerTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmanContainerTime_5)]   
podmantemp1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp1_5)]
podmantemp2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', podmantemp2_5)]


# ------------------------------------------------------------------------------ SINGULARITY

word1 = 'events per second:'

# -----------------------------------------------------------1
with open(".Results/1Singularity/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU1_1 = line1

with open(".Results/1Singularity/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU2_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Singularity/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU1_2 = line1

with open(".Results/2Singularity/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU2_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Singularity/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU1_3 = line1

with open(".Results/3Singularity/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU2_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Singularity/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU1_4 = line1

with open(".Results/4Singularity/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU2_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Singularity/resultsCPU1.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU1_5 = line1

with open(".Results/5Singularity/resultsCPU2.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityCPU2_5 = line1

word4 = 'transferred'

# -----------------------------------------------------------1
with open(".Results/1Singularity/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMr_1 = line4

with open(".Results/1Singularity/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMw_1 = line4

# -----------------------------------------------------------2
with open(".Results/2Singularity/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMr_2 = line4

with open(".Results/2Singularity/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMw_2 = line4

# -----------------------------------------------------------3
with open(".Results/3Singularity/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMr_3 = line4

with open(".Results/3Singularity/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMw_3 = line4

# -----------------------------------------------------------4
with open(".Results/4Singularity/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMr_4 = line4

with open(".Results/4Singularity/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMw_4 = line4

# -----------------------------------------------------------5
with open(".Results/5Singularity/resultsRAMread.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMr_5 = line4

with open(".Results/5Singularity/resultsRAMwrite.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line4 in lines:
        # check if string present on a current line
        if line4.find(word4) != -1:
            singularityRAMw_5 = line4


word1 = 'Benchy'

# -----------------------------------------------------------1
with open(".Results/1Singularity/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitySize_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Singularity/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitySize_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Singularity/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitySize_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Singularity/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitySize_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Singularity/ImageSize.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitySize_5 = line1



word1 = 'real'

# -----------------------------------------------------------1
with open(".Results/1Singularity/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTime_1 = line1

with open(".Results/1Singularity/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTimerm_1 = line1           

with open(".Results/1Singularity/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityContainerTime_1 = line1

# -----------------------------------------------------------2
with open(".Results/2Singularity/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTime_2 = line1

with open(".Results/2Singularity/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTimerm_2 = line1           

with open(".Results/2Singularity/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityContainerTime_2 = line1

# -----------------------------------------------------------3
with open(".Results/3Singularity/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTime_3 = line1

with open(".Results/3Singularity/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTimerm_3 = line1           

with open(".Results/3Singularity/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityContainerTime_3 = line1

# -----------------------------------------------------------4
with open(".Results/4Singularity/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTime_4 = line1

with open(".Results/4Singularity/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTimerm_4 = line1           

with open(".Results/4Singularity/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityContainerTime_4 = line1

# -----------------------------------------------------------5
with open(".Results/5Singularity/ImageTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTime_5 = line1

with open(".Results/5Singularity/ImageTimeRemove.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityImageTimerm_5 = line1           

with open(".Results/5Singularity/ContainerTime.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityContainerTime_5 = line1

word1 = 'read, MiB/s: '
word2 = 'written, MiB/s: '
word3 = 'fsyncs/s:'

# -----------------------------------------------------------1
with open(".Results/1Singularity/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityMEMr_1 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            singularityMEMw_1 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            singularityMEMf_1 = line3      

# -----------------------------------------------------------2
with open(".Results/2Singularity/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityMEMr_2 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            singularityMEMw_2 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            singularityMEMf_2 = line3    
            
# -----------------------------------------------------------3
with open(".Results/3Singularity/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityMEMr_3 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            singularityMEMw_3 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            singularityMEMf_3 = line3    
            
# -----------------------------------------------------------4
with open(".Results/4Singularity/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityMEMr_4 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            singularityMEMw_4 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            singularityMEMf_4 = line3    
            
# -----------------------------------------------------------5
with open(".Results/5Singularity/resultsMEM.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularityMEMr_5 = line1

    for line2 in lines:
        # check if string present on a current line
        if line2.find(word2) != -1:
            singularityMEMw_5 = line2
            
    for line3 in lines:
        # check if string present on a current line
        if line3.find(word3) != -1:
            singularityMEMf_5 = line3      
  

word1 = 'Package id 0:'
word2 = 'temp1'
singularitytemp1_1 = singularitytemp1_2 = singularitytemp1_3 = singularitytemp1_4 = singularitytemp1_5 = None
singularitytemp2_1 = singularitytemp2_2 = singularitytemp2_3 = singularitytemp2_4 = singularitytemp2_5 = None

# -----------------------------------------------------------1
with open(".Results/1Singularity/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp1_1 = line1

    if singularitytemp1_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp1_1 = line2

with open(".Results/1Singularity/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp2_1 = line1

    if singularitytemp2_1 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp2_1 = line2                           

# -----------------------------------------------------------2
with open(".Results/2Singularity/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp1_2 = line1

    if singularitytemp1_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp1_2 = line2

with open(".Results/2Singularity/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp2_2 = line1

    if singularitytemp2_2 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp2_2 = line2   
                
# -----------------------------------------------------------3
with open(".Results/3Singularity/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp1_3 = line1

    if singularitytemp1_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp1_3 = line2

with open(".Results/3Singularity/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp2_3 = line1

    if singularitytemp2_3 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp2_3 = line2  
                
# -----------------------------------------------------------4
with open(".Results/4Singularity/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp1_4 = line1

    if singularitytemp1_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp1_4 = line2

with open(".Results/4Singularity/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp2_4 = line1

    if singularitytemp2_4 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp2_4 = line2   
                
# -----------------------------------------------------------5
with open(".Results/5Singularity/1temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp1_5 = line1

    if singularitytemp1_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp1_5 = line2

with open(".Results/5Singularity/2temp.txt", "r") as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line1 in lines:
        # check if string present on a current line
        if line1.find(word1) != -1:
            singularitytemp2_5 = line1

    if singularitytemp2_5 is None:
        for line2 in lines:
            # check if string present on a current line
            if line2.find(word2) != -1:
                singularitytemp2_5 = line2                           
                        
singularityCPU1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU1_1)]
singularityCPU2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU2_1)]
singularityRAMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMr_1)]
singularityRAMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMw_1)]
singularityMEMr_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMr_1)]
singularityMEMw_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMw_1)]
singularityMEMf_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMf_1)]
singularitySize_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitySize_1)]
singularityImageTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         singularityImageTime_1)]    
singularityImageTimerm_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     singularityImageTimerm_1)] 
singularityContainerTime_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityContainerTime_1)]    
singularitytemp1_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp1_1)]
singularitytemp2_1 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp2_1)]
                        
singularityCPU1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU1_2)]
singularityCPU2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU2_2)]
singularityRAMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMr_2)]
singularityRAMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMw_2)]
singularityMEMr_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMr_2)]
singularityMEMw_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMw_2)]
singularityMEMf_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMf_2)]
singularitySize_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitySize_2)]
singularityImageTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         singularityImageTime_2)]    
singularityImageTimerm_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     singularityImageTimerm_2)] 
singularityContainerTime_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityContainerTime_2)]    
singularitytemp1_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp1_2)]
singularitytemp2_2 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp2_2)]
                        
singularityCPU1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU1_3)]
singularityCPU2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU2_3)]
singularityRAMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMr_3)]
singularityRAMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMw_3)]
singularityMEMr_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMr_3)]
singularityMEMw_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMw_3)]
singularityMEMf_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMf_3)]
singularitySize_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitySize_3)]
singularityImageTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         singularityImageTime_3)]    
singularityImageTimerm_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     singularityImageTimerm_3)] 
singularityContainerTime_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityContainerTime_3)]    
singularitytemp1_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp1_3)]
singularitytemp2_3 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp2_3)]
                        
singularityCPU1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU1_4)]
singularityCPU2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU2_4)]
singularityRAMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMr_4)]
singularityRAMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMw_4)]
singularityMEMr_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMr_4)]
singularityMEMw_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMw_4)]
singularityMEMf_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMf_4)]
singularitySize_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitySize_4)]
singularityImageTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         singularityImageTime_4)]    
singularityImageTimerm_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     singularityImageTimerm_4)] 
singularityContainerTime_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityContainerTime_4)]    
singularitytemp1_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp1_4)]
singularitytemp2_4 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp2_4)]
                        
singularityCPU1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU1_5)]
singularityCPU2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityCPU2_5)]
singularityRAMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMr_5)]
singularityRAMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityRAMw_5)]
singularityMEMr_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMr_5)]
singularityMEMw_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMw_5)]
singularityMEMf_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityMEMf_5)]
singularitySize_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitySize_5)]
singularityImageTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',         singularityImageTime_5)]    
singularityImageTimerm_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*',     singularityImageTimerm_5)] 
singularityContainerTime_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularityContainerTime_5)]    
singularitytemp1_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp1_5)]
singularitytemp2_5 = [float(s) for s in re.findall(r'-?\d+\.?\d*', singularitytemp2_5)]


# ------------------------------------------------------------------------------ GRÁFICOS

tec = ['Bare Metal', 'Docker', 'Podman', 'Singularity']

bareCPU1 = (bareCPU1_1[0] + bareCPU1_2[0] + bareCPU1_3[0] + bareCPU1_4[0] + bareCPU1_5[0])/5
dockerCPU1 = (dockerCPU1_1[0] + dockerCPU1_2[0] + dockerCPU1_3[0] + dockerCPU1_4[0] + dockerCPU1_5[0])/5
podmanCPU1 = (podmanCPU1_1[0] + podmanCPU1_2[0] + podmanCPU1_3[0] + podmanCPU1_4[0] + podmanCPU1_5[0])/5
singularityCPU1 = (singularityCPU1_1[0] + singularityCPU1_2[0] + singularityCPU1_3[0] + singularityCPU1_4[0] + singularityCPU1_5[0])/5

minbareCPU1 = min([bareCPU1_1[0], bareCPU1_2[0], bareCPU1_3[0], bareCPU1_4[0], bareCPU1_5[0]])
mindockerCPU1 = min([dockerCPU1_1[0], dockerCPU1_2[0], dockerCPU1_3[0], dockerCPU1_4[0], dockerCPU1_5[0]])
minpodmanCPU1 = min([podmanCPU1_1[0], podmanCPU1_2[0], podmanCPU1_3[0], podmanCPU1_4[0], podmanCPU1_5[0]])
minsingularityCPU1 = min([singularityCPU1_1[0], singularityCPU1_2[0], singularityCPU1_3[0], singularityCPU1_4[0], singularityCPU1_5[0]])

maxbareCPU1 = max([bareCPU1_1[0], bareCPU1_2[0], bareCPU1_3[0], bareCPU1_4[0], bareCPU1_5[0]])
maxdockerCPU1 = max([dockerCPU1_1[0], dockerCPU1_2[0], dockerCPU1_3[0], dockerCPU1_4[0], dockerCPU1_5[0]])
maxpodmanCPU1 = max([podmanCPU1_1[0], podmanCPU1_2[0], podmanCPU1_3[0], podmanCPU1_4[0], podmanCPU1_5[0]])
maxsingularityCPU1 = max([singularityCPU1_1[0], singularityCPU1_2[0], singularityCPU1_3[0], singularityCPU1_4[0], singularityCPU1_5[0]])

valor = [round(bareCPU1,1), round(dockerCPU1,1), round(podmanCPU1,1), round(singularityCPU1,1)]

plt.figure(1)
_min = [minbareCPU1, mindockerCPU1, minpodmanCPU1, minsingularityCPU1]
_max = [maxbareCPU1, maxdockerCPU1, maxpodmanCPU1, maxsingularityCPU1]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.bar(tec, valor, yerr=yerr, capsize=10)
plt.xticks(tec)
plt.ylabel('Eventos por segundo')
plt.title('Eventos por segundo do CPU (1 thread)')
plt.savefig('4-CPU1thread.png', bbox_inches='tight')
plt.figure(1).clear

bareCPU2 = (bareCPU2_1[0] + bareCPU2_2[0] + bareCPU2_3[0] + bareCPU2_4[0] + bareCPU2_5[0])/5
dockerCPU2 = (dockerCPU2_1[0] + dockerCPU2_2[0] + dockerCPU2_3[0] + dockerCPU2_4[0] + dockerCPU2_5[0])/5
podmanCPU2 = (podmanCPU2_1[0] + podmanCPU2_2[0] + podmanCPU2_3[0] + podmanCPU2_4[0] + podmanCPU2_5[0])/5
singularityCPU2 = (singularityCPU2_1[0] + singularityCPU2_2[0] + singularityCPU2_3[0] + singularityCPU2_4[0] + singularityCPU2_5[0])/5

minbareCPU2 = min([bareCPU2_1[0], bareCPU2_2[0],  bareCPU2_3[0],  bareCPU2_4[0], bareCPU2_5[0]])
mindockerCPU2 = min([dockerCPU2_1[0], dockerCPU2_2[0], dockerCPU2_3[0], dockerCPU2_4[0], dockerCPU2_5[0]])
minpodmanCPU2 = min([podmanCPU2_1[0], podmanCPU2_2[0], podmanCPU2_3[0], podmanCPU2_4[0], podmanCPU2_5[0]])
minsingularityCPU2 = min([singularityCPU2_1[0], singularityCPU2_2[0], singularityCPU2_3[0],  singularityCPU2_4[0], singularityCPU2_5[0]])

maxbareCPU2 = max([bareCPU2_1[0], bareCPU2_2[0],  bareCPU2_3[0],  bareCPU2_4[0], bareCPU2_5[0]])
maxdockerCPU2 = max([dockerCPU2_1[0], dockerCPU2_2[0], dockerCPU2_3[0], dockerCPU2_4[0], dockerCPU2_5[0]])
maxpodmanCPU2 = max([podmanCPU2_1[0], podmanCPU2_2[0], podmanCPU2_3[0], podmanCPU2_4[0], podmanCPU2_5[0]])
maxsingularityCPU2 = max([singularityCPU2_1[0], singularityCPU2_2[0], singularityCPU2_3[0],  singularityCPU2_4[0], singularityCPU2_5[0]])

valor = [round(bareCPU2,1), round(dockerCPU2,1), round(podmanCPU2,1), round(singularityCPU2,1)]

plt.figure(2)
_min = [minbareCPU2, mindockerCPU2, minpodmanCPU2, minsingularityCPU2]
_max = [maxbareCPU2, maxdockerCPU2, maxpodmanCPU2, maxsingularityCPU2]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Eventos por segundo')
plt.title('Eventos por segundo do CPU (2 threads)')
plt.savefig('5-CPU2thread.png', bbox_inches='tight')
plt.figure(2).clear

bareRAMr = (bareRAMr_1[1] + bareRAMr_2[1] + bareRAMr_3[1] + bareRAMr_4[1] + bareRAMr_5[1])/5
dockerRAMr = (dockerRAMr_1[1] + dockerRAMr_2[1] + dockerRAMr_3[1] + dockerRAMr_4[1] + dockerRAMr_5[1])/5
podmanRAMr = (podmanRAMr_1[1] + podmanRAMr_2[1] + podmanRAMr_3[1] + podmanRAMr_4[1] + podmanRAMr_5[1])/5
singularityRAMr = (singularityRAMr_1[1] + singularityRAMr_2[1] + singularityRAMr_3[1] + singularityRAMr_4[1] + singularityRAMr_5[1])/5

minbareRAMr = min([bareRAMr_1[1], bareRAMr_2[1], bareRAMr_3[1], bareRAMr_4[1], bareRAMr_5[1]])
mindockerRAMr = min([dockerRAMr_1[1], dockerRAMr_2[1], dockerRAMr_3[1], dockerRAMr_4[1], dockerRAMr_5[1]])
minpodmanRAMr = min([podmanRAMr_1[1], podmanRAMr_2[1], podmanRAMr_3[1], podmanRAMr_4[1], podmanRAMr_5[1]])
minsingularityRAMr = min([singularityRAMr_1[1], singularityRAMr_2[1], singularityRAMr_3[1], singularityRAMr_4[1], singularityRAMr_5[1]])

maxbareRAMr = max([bareRAMr_1[1], bareRAMr_2[1], bareRAMr_3[1], bareRAMr_4[1], bareRAMr_5[1]])
maxdockerRAMr = max([dockerRAMr_1[1], dockerRAMr_2[1], dockerRAMr_3[1], dockerRAMr_4[1], dockerRAMr_5[1]])
maxpodmanRAMr = max([podmanRAMr_1[1], podmanRAMr_2[1], podmanRAMr_3[1], podmanRAMr_4[1], podmanRAMr_5[1]])
maxsingularityRAMr = max([singularityRAMr_1[1], singularityRAMr_2[1], singularityRAMr_3[1], singularityRAMr_4[1], singularityRAMr_5[1]])

valor = [round(bareRAMr,1), round(dockerRAMr,1), round(podmanRAMr,1), round(singularityRAMr,1)]

plt.figure(3)
_min = [minbareRAMr, mindockerRAMr, minpodmanRAMr, minsingularityRAMr]
_max = [maxbareRAMr, maxdockerRAMr, maxpodmanRAMr, maxsingularityRAMr]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Transferência de dados (MiB/s)')
plt.title('Velocidade de leitura da RAM')
plt.savefig('6-RAMread.png', bbox_inches='tight')
plt.figure(3).clear

bareRAMw = (bareRAMw_1[1] + bareRAMw_2[1] + bareRAMw_3[1] + bareRAMw_4[1] + bareRAMw_5[1])/5
dockerRAMw = (dockerRAMw_1[1] + dockerRAMw_2[1] + dockerRAMw_3[1] + dockerRAMw_4[1] + dockerRAMw_5[1])/5
podmanRAMw = (podmanRAMw_1[1] + podmanRAMw_2[1] + podmanRAMw_3[1] + podmanRAMw_4[1] + podmanRAMw_5[1])/5
singularityRAMw = (singularityRAMw_1[1] + singularityRAMw_2[1] + singularityRAMw_3[1] + singularityRAMw_4[1] + singularityRAMw_5[1])/5

minbareRAMw = min([bareRAMw_1[1], bareRAMw_2[1], bareRAMw_3[1], bareRAMw_4[1], bareRAMw_5[1]])
mindockerRAMw = min([dockerRAMw_1[1], dockerRAMw_2[1], dockerRAMw_3[1], dockerRAMw_4[1], dockerRAMw_5[1]])
minpodmanRAMw = min([podmanRAMw_1[1], podmanRAMw_2[1], podmanRAMw_3[1], podmanRAMw_4[1], podmanRAMw_5[1]])
minsingularityRAMw = min([singularityRAMw_1[1], singularityRAMw_2[1], singularityRAMw_3[1], singularityRAMw_4[1], singularityRAMw_5[1]])

maxbareRAMw = max([bareRAMw_1[1], bareRAMw_2[1], bareRAMw_3[1], bareRAMw_4[1], bareRAMw_5[1]])
maxdockerRAMw = max([dockerRAMw_1[1], dockerRAMw_2[1], dockerRAMw_3[1], dockerRAMw_4[1], dockerRAMw_5[1]])
maxpodmanRAMw = max([podmanRAMw_1[1], podmanRAMw_2[1], podmanRAMw_3[1], podmanRAMw_4[1], podmanRAMw_5[1]])
maxsingularityRAMw = max([singularityRAMw_1[1], singularityRAMw_2[1], singularityRAMw_3[1], singularityRAMw_4[1], singularityRAMw_5[1]])

valor = [round(bareRAMw,1), round(dockerRAMw,1), round(podmanRAMw,1), round(singularityRAMw,1)]

plt.figure(4)
_min = [minbareRAMw, mindockerRAMw, minpodmanRAMw, minsingularityRAMw]
_max = [maxbareRAMw, maxdockerRAMw, maxpodmanRAMw, maxsingularityRAMw]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Transferência de dados (MiB/s)')
plt.title('Velocidade de escrita da RAM')
plt.savefig('7-RAMwrite.png', bbox_inches='tight')
plt.figure(4).clear

bareMEMw = (bareMEMw_1[0] + bareMEMw_2[0] + bareMEMw_3[0] + bareMEMw_4[0] + bareMEMw_5[0])/5
dockerMEMw = (dockerMEMw_1[0] + dockerMEMw_2[0] + dockerMEMw_3[0] + dockerMEMw_4[0] + dockerMEMw_5[0])/5
podmanMEMw = (podmanMEMw_1[0] + podmanMEMw_2[0] + podmanMEMw_3[0] + podmanMEMw_4[0] + podmanMEMw_5[0])/5
singularityMEMw = (singularityMEMw_1[0] + singularityMEMw_2[0] + singularityMEMw_3[0] + singularityMEMw_4[0] + singularityMEMw_5[0])/5

minbareMEMw = min([bareMEMw_1[0], bareMEMw_2[0], bareMEMw_3[0], bareMEMw_4[0], bareMEMw_5[0]])
mindockerMEMw = min([dockerMEMw_1[0], dockerMEMw_2[0], dockerMEMw_3[0], dockerMEMw_4[0], dockerMEMw_5[0]])
minpodmanMEMw = min([podmanMEMw_1[0], podmanMEMw_2[0], podmanMEMw_3[0], podmanMEMw_4[0], podmanMEMw_5[0]]) 
minsingularityMEMw = min([singularityMEMw_1[0], singularityMEMw_2[0], singularityMEMw_3[0], singularityMEMw_4[0], singularityMEMw_5[0]])

maxbareMEMw = max([bareMEMw_1[0], bareMEMw_2[0], bareMEMw_3[0], bareMEMw_4[0], bareMEMw_5[0]])
maxdockerMEMw = max([dockerMEMw_1[0], dockerMEMw_2[0], dockerMEMw_3[0], dockerMEMw_4[0], dockerMEMw_5[0]])
maxpodmanMEMw = max([podmanMEMw_1[0], podmanMEMw_2[0], podmanMEMw_3[0], podmanMEMw_4[0], podmanMEMw_5[0]])
maxsingularityMEMw = max([singularityMEMw_1[0], singularityMEMw_2[0], singularityMEMw_3[0], singularityMEMw_4[0], singularityMEMw_5[0]])

valor = [round(bareMEMw,1), round(dockerMEMw,1), round(podmanMEMw,1), round(singularityMEMw,1)]

plt.figure(8)
_min = [minbareMEMw, mindockerMEMw, minpodmanMEMw, minsingularityMEMw]
_max = [maxbareMEMw, maxdockerMEMw, maxpodmanMEMw, maxsingularityMEMw]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('MiB/s')
plt.title('Velocidade de escrita da memória')
plt.savefig('8-MEMwrite.png', bbox_inches='tight')
plt.figure(8).clear

bareMEMr = (bareMEMr_1[0] + bareMEMr_2[0] + bareMEMr_3[0] + bareMEMr_4[0] + bareMEMr_5[0])/5
dockerMEMr = (dockerMEMr_1[0] + dockerMEMr_2[0] + dockerMEMr_3[0] + dockerMEMr_4[0] + dockerMEMr_5[0])/5
podmanMEMr = (podmanMEMr_1[0] + podmanMEMr_2[0] + podmanMEMr_3[0] + podmanMEMr_4[0] + podmanMEMr_5[0])/5
singularityMEMr = (singularityMEMr_1[0] + singularityMEMr_2[0] + singularityMEMr_3[0] + singularityMEMr_4[0] + singularityMEMr_5[0])/5

minbareMEMr = min([bareMEMr_1[0], bareMEMr_2[0], bareMEMr_3[0], bareMEMr_4[0], bareMEMr_5[0]])
mindockerMEMr = min([dockerMEMr_1[0], dockerMEMr_2[0], dockerMEMr_3[0], dockerMEMr_4[0], dockerMEMr_5[0]])
minpodmanMEMr = min([podmanMEMr_1[0], podmanMEMr_2[0], podmanMEMr_3[0], podmanMEMr_4[0], podmanMEMr_5[0]])
minsingularityMEMr = min([singularityMEMr_1[0], singularityMEMr_2[0], singularityMEMr_3[0], singularityMEMr_4[0], singularityMEMr_5[0]])

maxbareMEMr = max([bareMEMr_1[0], bareMEMr_2[0], bareMEMr_3[0], bareMEMr_4[0], bareMEMr_5[0]])
maxdockerMEMr = max([dockerMEMr_1[0], dockerMEMr_2[0], dockerMEMr_3[0], dockerMEMr_4[0], dockerMEMr_5[0]])
maxpodmanMEMr = max([podmanMEMr_1[0], podmanMEMr_2[0], podmanMEMr_3[0], podmanMEMr_4[0], podmanMEMr_5[0]])
maxsingularityMEMr = max([singularityMEMr_1[0], singularityMEMr_2[0], singularityMEMr_3[0], singularityMEMr_4[0], singularityMEMr_5[0]])

valor = [round(bareMEMr,1), round(dockerMEMr,1), round(podmanMEMr,1), round(singularityMEMr,1)]

plt.figure(9)
_min = [minbareMEMr, mindockerMEMr, minpodmanMEMr, minsingularityMEMr]
_max = [maxbareMEMr, maxdockerMEMr, maxpodmanMEMr, maxsingularityMEMr]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('MiB/s')
plt.title('Velocidade de leitura da memória')
plt.savefig('9-MEMread.png', bbox_inches='tight')
plt.figure(9).clear

bareMEMf = (bareMEMf_1[0] + bareMEMf_2[0] + bareMEMf_3[0] + bareMEMf_4[0] + bareMEMf_5[0])/5
dockerMEMf = (dockerMEMf_1[0] + dockerMEMf_2[0] + dockerMEMf_3[0] + dockerMEMf_4[0] + dockerMEMf_5[0])/5
podmanMEMf = (podmanMEMf_1[0] + podmanMEMf_2[0] + podmanMEMf_3[0] + podmanMEMf_4[0] + podmanMEMf_5[0])/5
singularityMEMf = (singularityMEMf_1[0] + singularityMEMf_2[0] + singularityMEMf_3[0] + singularityMEMf_4[0] + singularityMEMf_5[0])/5

minbareMEMf = min([bareMEMf_1[0], bareMEMf_2[0], bareMEMf_3[0], bareMEMf_4[0], bareMEMf_5[0]])
mindockerMEMf = min([dockerMEMf_1[0], dockerMEMf_2[0], dockerMEMf_3[0], dockerMEMf_4[0], dockerMEMf_5[0]])
minpodmanMEMf = min([podmanMEMf_1[0], podmanMEMf_2[0], podmanMEMf_3[0], podmanMEMf_4[0], podmanMEMf_5[0]])
minsingularityMEMf = min([singularityMEMf_1[0], singularityMEMf_2[0], singularityMEMf_3[0], singularityMEMf_4[0], singularityMEMf_5[0]])

maxbareMEMf = max([bareMEMf_1[0], bareMEMf_2[0], bareMEMf_3[0], bareMEMf_4[0], bareMEMf_5[0]])
maxdockerMEMf = max([dockerMEMf_1[0], dockerMEMf_2[0], dockerMEMf_3[0], dockerMEMf_4[0], dockerMEMf_5[0]])
maxpodmanMEMf = max([podmanMEMf_1[0], podmanMEMf_2[0], podmanMEMf_3[0], podmanMEMf_4[0], podmanMEMf_5[0]])
maxsingularityMEMf = max([singularityMEMf_1[0], singularityMEMf_2[0], singularityMEMf_3[0], singularityMEMf_4[0], singularityMEMf_5[0]])

valor = [round(bareMEMf,1), round(dockerMEMf,1), round(podmanMEMf,1), round(singularityMEMf,1)]

plt.figure(10)
_min = [minbareMEMf, mindockerMEMf, minpodmanMEMf, minsingularityMEMf]
_max = [maxbareMEMf, maxdockerMEMf, maxpodmanMEMf, maxsingularityMEMf]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Fsyncs por segundo')
plt.title('Fsyncs/s')
plt.savefig('10-MEMf.png', bbox_inches='tight')
plt.figure(10).clear

temp1 = (temp1_1[1] + temp1_2[1] + temp1_3[1] + temp1_4[1] + temp1_5[1])/5
dockertemp1 = (dockertemp1_1[1] + dockertemp1_2[1] + dockertemp1_3[1] + dockertemp1_4[1] + dockertemp1_5[1])/5
podmantemp1 = (podmantemp1_1[1] + podmantemp1_2[1] + podmantemp1_3[1] + podmantemp1_4[1] + podmantemp1_5[1])/5
singularitytemp1 = (singularitytemp1_1[1] + singularitytemp1_2[1] + singularitytemp1_3[1] + singularitytemp1_4[1] + singularitytemp1_5[1])/5
temp2 = (temp2_1[1] + temp2_2[1] + temp2_3[1] + temp2_4[1] + temp2_5[1])/5
dockertemp2 = (dockertemp2_1[1] + dockertemp2_2[1] + dockertemp2_3[1] + dockertemp2_4[1] + dockertemp2_5[1])/5
podmantemp2 = (podmantemp2_1[1] + podmantemp2_2[1] + podmantemp2_3[1] + podmantemp2_4[1] + podmantemp2_5[1])/5
singularitytemp2 = (singularitytemp2_1[1] + singularitytemp2_2[1] + singularitytemp2_3[1] + singularitytemp2_4[1] + singularitytemp2_5[1])/5
valor1 = [round(temp1,1), round(dockertemp1,1), round(podmantemp1,1), round(singularitytemp1,1)]
valor2 = [temp2, dockertemp2, podmantemp2, singularitytemp2]

plt.figure(13)
X_axis = np.arange(len(tec)) 
plt.bar(X_axis - 0.2, valor1, 0.4, color='blue', label = 'Temp. Inicial') 
plt.bar(X_axis + 0.2, valor2, 0.4, color='red', label = 'Temp. Final') 
plt.xticks(X_axis, tec) 
plt.ylabel('Temperatura (ºC)')
plt.title('Variação da temperatura (CPU)')
plt.savefig('13-temperaturas.png', bbox_inches='tight')
plt.figure(13).clear


tec = ['Docker', 'Podman', 'Singularity']

dockerSize = (dockerSize_1[len(dockerSize_1)-1] +
              dockerSize_2[len(dockerSize_2)-1] +
              dockerSize_3[len(dockerSize_3)-1] +
              dockerSize_4[len(dockerSize_4)-1] +
              dockerSize_5[len(dockerSize_5)-1])/5
podmanSize = (podmanSize_1[len(podmanSize_1)-1] + 
              podmanSize_2[len(podmanSize_2)-1] + 
              podmanSize_3[len(podmanSize_3)-1] + 
              podmanSize_4[len(podmanSize_4)-1] +
              podmanSize_5[len(podmanSize_5)-1])/5
singularitySize = (singularitySize_1[0] + singularitySize_2[0] + singularitySize_3[0] + singularitySize_4[0] + singularitySize_5[0])/5
valor = [round(dockerSize,1), round(podmanSize,1), round(singularitySize,1)]

plt.figure(5)
plt.bar(tec, valor)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Tamanho (MB)')
plt.title('Tamanho da imagem')
plt.savefig('2-Size.png', bbox_inches='tight')
plt.figure(5).clear

dockerImageTime = (dockerImageTime_1[len(dockerImageTime_1)-2] + dockerImageTime_1[len(dockerImageTime_1)-1]/1000 +
                   dockerImageTime_2[len(dockerImageTime_2)-2] + dockerImageTime_2[len(dockerImageTime_2)-1]/1000 +
                   dockerImageTime_3[len(dockerImageTime_3)-2] + dockerImageTime_3[len(dockerImageTime_3)-1]/1000 +
                   dockerImageTime_4[len(dockerImageTime_4)-2] + dockerImageTime_4[len(dockerImageTime_4)-1]/1000 +
                   dockerImageTime_5[len(dockerImageTime_5)-2] + dockerImageTime_5[len(dockerImageTime_5)-1]/1000)/5
podmanImageTime = (podmanImageTime_1[len(podmanImageTime_1)-2] + podmanImageTime_1[len(podmanImageTime_1)-1]/1000 +
                   podmanImageTime_2[len(podmanImageTime_2)-2] + podmanImageTime_2[len(podmanImageTime_2)-1]/1000 +
                   podmanImageTime_3[len(podmanImageTime_3)-2] + podmanImageTime_3[len(podmanImageTime_3)-1]/1000 +
                   podmanImageTime_4[len(podmanImageTime_4)-2] + podmanImageTime_4[len(podmanImageTime_4)-1]/1000 +
                   podmanImageTime_5[len(podmanImageTime_5)-2] + podmanImageTime_5[len(podmanImageTime_5)-1]/1000)/5
singularityImageTime = (singularityImageTime_1[len(singularityImageTime_1)-2] + singularityImageTime_1[len(singularityImageTime_1)-1]/1000 +
                        singularityImageTime_2[len(singularityImageTime_2)-2] + singularityImageTime_2[len(singularityImageTime_2)-1]/1000 +
                        singularityImageTime_3[len(singularityImageTime_3)-2] + singularityImageTime_3[len(singularityImageTime_3)-1]/1000 +
                        singularityImageTime_4[len(singularityImageTime_4)-2] + singularityImageTime_4[len(singularityImageTime_4)-1]/1000 +
                        singularityImageTime_5[len(singularityImageTime_5)-2] + singularityImageTime_5[len(singularityImageTime_5)-1]/1000)/5

mindockerImageTime = min([dockerImageTime_1[len(dockerImageTime_1)-2] + dockerImageTime_1[len(dockerImageTime_1)-1]/1000,
                          dockerImageTime_2[len(dockerImageTime_2)-2] + dockerImageTime_2[len(dockerImageTime_2)-1]/1000,
                          dockerImageTime_3[len(dockerImageTime_3)-2] + dockerImageTime_3[len(dockerImageTime_3)-1]/1000,
                          dockerImageTime_4[len(dockerImageTime_4)-2] + dockerImageTime_4[len(dockerImageTime_4)-1]/1000,
                          dockerImageTime_5[len(dockerImageTime_5)-2] + dockerImageTime_5[len(dockerImageTime_5)-1]/1000])
minpodmanImageTime = min([podmanImageTime_1[len(podmanImageTime_1)-2] + podmanImageTime_1[len(podmanImageTime_1)-1]/1000,
                          podmanImageTime_2[len(podmanImageTime_2)-2] + podmanImageTime_2[len(podmanImageTime_2)-1]/1000,
                          podmanImageTime_3[len(podmanImageTime_3)-2] + podmanImageTime_3[len(podmanImageTime_3)-1]/1000,
                          podmanImageTime_4[len(podmanImageTime_4)-2] + podmanImageTime_4[len(podmanImageTime_4)-1]/1000,
                          podmanImageTime_5[len(podmanImageTime_5)-2] + podmanImageTime_5[len(podmanImageTime_5)-1]/1000])
minsingularityImageTime = min([singularityImageTime_1[len(singularityImageTime_1)-2] + singularityImageTime_1[len(singularityImageTime_1)-1]/1000,
                               singularityImageTime_2[len(singularityImageTime_2)-2] + singularityImageTime_2[len(singularityImageTime_2)-1]/1000,
                               singularityImageTime_3[len(singularityImageTime_3)-2] + singularityImageTime_3[len(singularityImageTime_3)-1]/1000,
                               singularityImageTime_4[len(singularityImageTime_4)-2] + singularityImageTime_4[len(singularityImageTime_4)-1]/1000,
                               singularityImageTime_5[len(singularityImageTime_5)-2] + singularityImageTime_5[len(singularityImageTime_5)-1]/1000])

maxdockerImageTime = max([dockerImageTime_1[len(dockerImageTime_1)-2] + dockerImageTime_1[len(dockerImageTime_1)-1]/1000,
                          dockerImageTime_2[len(dockerImageTime_2)-2] + dockerImageTime_2[len(dockerImageTime_2)-1]/1000,
                          dockerImageTime_3[len(dockerImageTime_3)-2] + dockerImageTime_3[len(dockerImageTime_3)-1]/1000,
                          dockerImageTime_4[len(dockerImageTime_4)-2] + dockerImageTime_4[len(dockerImageTime_4)-1]/1000,
                          dockerImageTime_5[len(dockerImageTime_5)-2] + dockerImageTime_5[len(dockerImageTime_5)-1]/1000])
maxpodmanImageTime = max([podmanImageTime_1[len(podmanImageTime_1)-2] + podmanImageTime_1[len(podmanImageTime_1)-1]/1000,
                          podmanImageTime_2[len(podmanImageTime_2)-2] + podmanImageTime_2[len(podmanImageTime_2)-1]/1000,
                          podmanImageTime_3[len(podmanImageTime_3)-2] + podmanImageTime_3[len(podmanImageTime_3)-1]/1000,
                          podmanImageTime_4[len(podmanImageTime_4)-2] + podmanImageTime_4[len(podmanImageTime_4)-1]/1000,
                          podmanImageTime_5[len(podmanImageTime_5)-2] + podmanImageTime_5[len(podmanImageTime_5)-1]/1000])
maxsingularityImageTime = max([singularityImageTime_1[len(singularityImageTime_1)-2] + singularityImageTime_1[len(singularityImageTime_1)-1]/1000,
                               singularityImageTime_2[len(singularityImageTime_2)-2] + singularityImageTime_2[len(singularityImageTime_2)-1]/1000,
                               singularityImageTime_3[len(singularityImageTime_3)-2] + singularityImageTime_3[len(singularityImageTime_3)-1]/1000,
                               singularityImageTime_4[len(singularityImageTime_4)-2] + singularityImageTime_4[len(singularityImageTime_4)-1]/1000,
                               singularityImageTime_5[len(singularityImageTime_5)-2] + singularityImageTime_5[len(singularityImageTime_5)-1]/1000])

valor = [round(dockerImageTime,1), round(podmanImageTime,1), round(singularityImageTime,1)]

plt.figure(7)
_min = [mindockerImageTime, minpodmanImageTime, minsingularityImageTime]
_max = [maxdockerImageTime, maxpodmanImageTime, maxsingularityImageTime]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Tempo (s)')
plt.title('Tempo de construção da imagem')
plt.savefig('1-buildimage.png', bbox_inches='tight')
plt.figure(7).clear

dockerImageTimerm = (dockerImageTimerm_1[len(dockerImageTimerm_1)-2]*1000 + dockerImageTimerm_1[len(dockerImageTimerm_1)-1] +
                     dockerImageTimerm_2[len(dockerImageTimerm_2)-2]*1000 + dockerImageTimerm_2[len(dockerImageTimerm_2)-1] +
                     dockerImageTimerm_3[len(dockerImageTimerm_3)-2]*1000 + dockerImageTimerm_3[len(dockerImageTimerm_3)-1] +
                     dockerImageTimerm_4[len(dockerImageTimerm_4)-2]*1000 + dockerImageTimerm_4[len(dockerImageTimerm_4)-1] +
                     dockerImageTimerm_5[len(dockerImageTimerm_5)-2]*1000 + dockerImageTimerm_5[len(dockerImageTimerm_5)-1])/5
podmanImageTimerm = (podmanImageTimerm_1[len(podmanImageTimerm_1)-2]*1000 + podmanImageTimerm_1[len(podmanImageTimerm_1)-1] +
                     podmanImageTimerm_2[len(podmanImageTimerm_2)-2]*1000 + podmanImageTimerm_2[len(podmanImageTimerm_2)-1] +
                     podmanImageTimerm_3[len(podmanImageTimerm_3)-2]*1000 + podmanImageTimerm_3[len(podmanImageTimerm_3)-1] +
                     podmanImageTimerm_4[len(podmanImageTimerm_4)-2]*1000 + podmanImageTimerm_4[len(podmanImageTimerm_4)-1] +
                     podmanImageTimerm_5[len(podmanImageTimerm_5)-2]*1000 + podmanImageTimerm_5[len(podmanImageTimerm_5)-1])/5
singularityImageTimerm = (singularityImageTimerm_1[len(singularityImageTimerm_1)-2]*1000 + singularityImageTimerm_1[len(singularityImageTimerm_1)-1] +
                          singularityImageTimerm_2[len(singularityImageTimerm_2)-2]*1000 + singularityImageTimerm_2[len(singularityImageTimerm_2)-1] +
                          singularityImageTimerm_3[len(singularityImageTimerm_3)-2]*1000 + singularityImageTimerm_3[len(singularityImageTimerm_3)-1] +
                          singularityImageTimerm_4[len(singularityImageTimerm_4)-2]*1000 + singularityImageTimerm_4[len(singularityImageTimerm_4)-1] +
                          singularityImageTimerm_5[len(singularityImageTimerm_5)-2]*1000 + singularityImageTimerm_5[len(singularityImageTimerm_5)-1])/5

mindockerImageTimerm = min([dockerImageTimerm_1[len(dockerImageTimerm_1)-2]*1000 + dockerImageTimerm_1[len(dockerImageTimerm_1)-1],
                            dockerImageTimerm_2[len(dockerImageTimerm_2)-2]*1000 + dockerImageTimerm_2[len(dockerImageTimerm_2)-1],
                            dockerImageTimerm_3[len(dockerImageTimerm_3)-2]*1000 + dockerImageTimerm_3[len(dockerImageTimerm_3)-1],
                            dockerImageTimerm_4[len(dockerImageTimerm_4)-2]*1000 + dockerImageTimerm_4[len(dockerImageTimerm_4)-1],
                            dockerImageTimerm_5[len(dockerImageTimerm_5)-2]*1000 + dockerImageTimerm_5[len(dockerImageTimerm_5)-1]])
minpodmanImageTimerm = min([podmanImageTimerm_1[len(podmanImageTimerm_1)-2]*1000 + podmanImageTimerm_1[len(podmanImageTimerm_1)-1],
                            podmanImageTimerm_2[len(podmanImageTimerm_2)-2]*1000 + podmanImageTimerm_2[len(podmanImageTimerm_2)-1],
                            podmanImageTimerm_3[len(podmanImageTimerm_3)-2]*1000 + podmanImageTimerm_3[len(podmanImageTimerm_3)-1],
                            podmanImageTimerm_4[len(podmanImageTimerm_4)-2]*1000 + podmanImageTimerm_4[len(podmanImageTimerm_4)-1],
                            podmanImageTimerm_5[len(podmanImageTimerm_5)-2]*1000 + podmanImageTimerm_5[len(podmanImageTimerm_5)-1]])
minsingularityImageTimerm = min([singularityImageTimerm_1[len(singularityImageTimerm_1)-2]*1000 + singularityImageTimerm_1[len(singularityImageTimerm_1)-1],
                                 singularityImageTimerm_2[len(singularityImageTimerm_2)-2]*1000 + singularityImageTimerm_2[len(singularityImageTimerm_2)-1],
                                 singularityImageTimerm_3[len(singularityImageTimerm_3)-2]*1000 + singularityImageTimerm_3[len(singularityImageTimerm_3)-1],
                                 singularityImageTimerm_4[len(singularityImageTimerm_4)-2]*1000 + singularityImageTimerm_4[len(singularityImageTimerm_4)-1],
                                 singularityImageTimerm_5[len(singularityImageTimerm_5)-2]*1000 + singularityImageTimerm_5[len(singularityImageTimerm_5)-1]])

maxdockerImageTimerm = max([dockerImageTimerm_1[len(dockerImageTimerm_1)-2]*1000 + dockerImageTimerm_1[len(dockerImageTimerm_1)-1],
                            dockerImageTimerm_2[len(dockerImageTimerm_2)-2]*1000 + dockerImageTimerm_2[len(dockerImageTimerm_2)-1],
                            dockerImageTimerm_3[len(dockerImageTimerm_3)-2]*1000 + dockerImageTimerm_3[len(dockerImageTimerm_3)-1],
                            dockerImageTimerm_4[len(dockerImageTimerm_4)-2]*1000 + dockerImageTimerm_4[len(dockerImageTimerm_4)-1],
                            dockerImageTimerm_5[len(dockerImageTimerm_5)-2]*1000 + dockerImageTimerm_5[len(dockerImageTimerm_5)-1]])
maxpodmanImageTimerm = max([podmanImageTimerm_1[len(podmanImageTimerm_1)-2]*1000 + podmanImageTimerm_1[len(podmanImageTimerm_1)-1],
                            podmanImageTimerm_2[len(podmanImageTimerm_2)-2]*1000 + podmanImageTimerm_2[len(podmanImageTimerm_2)-1],
                            podmanImageTimerm_3[len(podmanImageTimerm_3)-2]*1000 + podmanImageTimerm_3[len(podmanImageTimerm_3)-1],
                            podmanImageTimerm_4[len(podmanImageTimerm_4)-2]*1000 + podmanImageTimerm_4[len(podmanImageTimerm_4)-1],
                            podmanImageTimerm_5[len(podmanImageTimerm_5)-2]*1000 + podmanImageTimerm_5[len(podmanImageTimerm_5)-1]])
maxsingularityImageTimerm = max([singularityImageTimerm_1[len(singularityImageTimerm_1)-2]*1000 + singularityImageTimerm_1[len(singularityImageTimerm_1)-1],
                                 singularityImageTimerm_2[len(singularityImageTimerm_2)-2]*1000 + singularityImageTimerm_2[len(singularityImageTimerm_2)-1],
                                 singularityImageTimerm_3[len(singularityImageTimerm_3)-2]*1000 + singularityImageTimerm_3[len(singularityImageTimerm_3)-1],
                                 singularityImageTimerm_4[len(singularityImageTimerm_4)-2]*1000 + singularityImageTimerm_4[len(singularityImageTimerm_4)-1],
                                 singularityImageTimerm_5[len(singularityImageTimerm_5)-2]*1000 + singularityImageTimerm_5[len(singularityImageTimerm_5)-1]])

valor = [round(dockerImageTimerm,3), round(podmanImageTimerm,3), round(singularityImageTimerm,3)]

plt.figure(11)
_min = [mindockerImageTimerm, minpodmanImageTimerm, minsingularityImageTimerm]
_max = [maxdockerImageTimerm, maxpodmanImageTimerm, maxsingularityImageTimerm]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Tempo (ms)')
plt.title('Tempo de remoção da imagem')
plt.savefig('11-imageremove.png', bbox_inches='tight')
plt.figure(11).clear

dockerContainerTime = (dockerContainerTime_1[len(dockerContainerTime_1)-3]*60 + dockerContainerTime_1[len(dockerContainerTime_1)-2] +
                       dockerContainerTime_2[len(dockerContainerTime_2)-3]*60 + dockerContainerTime_2[len(dockerContainerTime_2)-2] +
                       dockerContainerTime_3[len(dockerContainerTime_3)-3]*60 + dockerContainerTime_3[len(dockerContainerTime_3)-2] +
                       dockerContainerTime_4[len(dockerContainerTime_4)-3]*60 + dockerContainerTime_4[len(dockerContainerTime_4)-2] +
                       dockerContainerTime_5[len(dockerContainerTime_5)-3]*60 + dockerContainerTime_5[len(dockerContainerTime_5)-2])/5
podmanContainerTime = (podmanContainerTime_1[len(podmanContainerTime_1)-3]*60 + podmanContainerTime_1[len(podmanContainerTime_1)-2] +
                       podmanContainerTime_2[len(podmanContainerTime_2)-3]*60 + podmanContainerTime_2[len(podmanContainerTime_2)-2] +
                       podmanContainerTime_3[len(podmanContainerTime_3)-3]*60 + podmanContainerTime_3[len(podmanContainerTime_3)-2] +
                       podmanContainerTime_4[len(podmanContainerTime_4)-3]*60 + podmanContainerTime_4[len(podmanContainerTime_4)-2] +
                       podmanContainerTime_5[len(podmanContainerTime_5)-3]*60 + podmanContainerTime_5[len(podmanContainerTime_5)-2])/5
singularityContainerTime = (singularityContainerTime_1[len(singularityContainerTime_1)-3]*60 + singularityContainerTime_1[len(singularityContainerTime_1)-2] +
                            singularityContainerTime_2[len(singularityContainerTime_2)-3]*60 + singularityContainerTime_2[len(singularityContainerTime_2)-2] +
                            singularityContainerTime_3[len(singularityContainerTime_3)-3]*60 + singularityContainerTime_3[len(singularityContainerTime_3)-2] +
                            singularityContainerTime_4[len(singularityContainerTime_4)-3]*60 + singularityContainerTime_4[len(singularityContainerTime_4)-2] +
                            singularityContainerTime_5[len(singularityContainerTime_5)-3]*60 + singularityContainerTime_5[len(singularityContainerTime_5)-2])/5

mindockerContainerTime = min([dockerContainerTime_1[len(dockerContainerTime_1)-3]*60 + dockerContainerTime_1[len(dockerContainerTime_1)-2],
                              dockerContainerTime_2[len(dockerContainerTime_2)-3]*60 + dockerContainerTime_2[len(dockerContainerTime_2)-2],
                              dockerContainerTime_3[len(dockerContainerTime_3)-3]*60 + dockerContainerTime_3[len(dockerContainerTime_3)-2],
                              dockerContainerTime_4[len(dockerContainerTime_4)-3]*60 + dockerContainerTime_4[len(dockerContainerTime_4)-2],
                              dockerContainerTime_5[len(dockerContainerTime_5)-3]*60 + dockerContainerTime_5[len(dockerContainerTime_5)-2]])
minpodmanContainerTime = min([podmanContainerTime_1[len(podmanContainerTime_1)-3]*60 + podmanContainerTime_1[len(podmanContainerTime_1)-2],
                              podmanContainerTime_2[len(podmanContainerTime_2)-3]*60 + podmanContainerTime_2[len(podmanContainerTime_2)-2],
                              podmanContainerTime_3[len(podmanContainerTime_3)-3]*60 + podmanContainerTime_3[len(podmanContainerTime_3)-2],
                              podmanContainerTime_4[len(podmanContainerTime_4)-3]*60 + podmanContainerTime_4[len(podmanContainerTime_4)-2],
                              podmanContainerTime_5[len(podmanContainerTime_5)-3]*60 + podmanContainerTime_5[len(podmanContainerTime_5)-2]])
minsingularityContainerTime = min([singularityContainerTime_1[len(singularityContainerTime_1)-3]*60 + singularityContainerTime_1[len(singularityContainerTime_1)-2],
                                   singularityContainerTime_2[len(singularityContainerTime_2)-3]*60 + singularityContainerTime_2[len(singularityContainerTime_2)-2],
                                   singularityContainerTime_3[len(singularityContainerTime_3)-3]*60 + singularityContainerTime_3[len(singularityContainerTime_3)-2],
                                   singularityContainerTime_4[len(singularityContainerTime_4)-3]*60 + singularityContainerTime_4[len(singularityContainerTime_4)-2],
                                   singularityContainerTime_5[len(singularityContainerTime_5)-3]*60 + singularityContainerTime_5[len(singularityContainerTime_5)-2]])

maxdockerContainerTime = max([dockerContainerTime_1[len(dockerContainerTime_1)-3]*60 + dockerContainerTime_1[len(dockerContainerTime_1)-2],
                              dockerContainerTime_2[len(dockerContainerTime_2)-3]*60 + dockerContainerTime_2[len(dockerContainerTime_2)-2],
                              dockerContainerTime_3[len(dockerContainerTime_3)-3]*60 + dockerContainerTime_3[len(dockerContainerTime_3)-2],
                              dockerContainerTime_4[len(dockerContainerTime_4)-3]*60 + dockerContainerTime_4[len(dockerContainerTime_4)-2],
                              dockerContainerTime_5[len(dockerContainerTime_5)-3]*60 + dockerContainerTime_5[len(dockerContainerTime_5)-2]])
maxpodmanContainerTime = max([podmanContainerTime_1[len(podmanContainerTime_1)-3]*60 + podmanContainerTime_1[len(podmanContainerTime_1)-2],
                              podmanContainerTime_2[len(podmanContainerTime_2)-3]*60 + podmanContainerTime_2[len(podmanContainerTime_2)-2],
                              podmanContainerTime_3[len(podmanContainerTime_3)-3]*60 + podmanContainerTime_3[len(podmanContainerTime_3)-2],
                              podmanContainerTime_4[len(podmanContainerTime_4)-3]*60 + podmanContainerTime_4[len(podmanContainerTime_4)-2],
                              podmanContainerTime_5[len(podmanContainerTime_5)-3]*60 + podmanContainerTime_5[len(podmanContainerTime_5)-2]])
maxsingularityContainerTime = max([singularityContainerTime_1[len(singularityContainerTime_1)-3]*60 + singularityContainerTime_1[len(singularityContainerTime_1)-2],
                                   singularityContainerTime_2[len(singularityContainerTime_2)-3]*60 + singularityContainerTime_2[len(singularityContainerTime_2)-2],
                                   singularityContainerTime_3[len(singularityContainerTime_3)-3]*60 + singularityContainerTime_3[len(singularityContainerTime_3)-2],
                                   singularityContainerTime_4[len(singularityContainerTime_4)-3]*60 + singularityContainerTime_4[len(singularityContainerTime_4)-2],
                                   singularityContainerTime_5[len(singularityContainerTime_5)-3]*60 + singularityContainerTime_5[len(singularityContainerTime_5)-2]])

valor = [round(dockerContainerTime,1), round(podmanContainerTime,1), round(singularityContainerTime,1)]

plt.figure(12)
_min = [mindockerContainerTime, minpodmanContainerTime, minsingularityContainerTime]
_max = [maxdockerContainerTime, maxpodmanContainerTime, maxsingularityContainerTime]
yerr = [np.subtract(valor, _min), np.subtract(_max, valor)]
plt.bar(tec, valor, yerr=yerr, capsize=10)
for index, value in enumerate(valor):
    plt.text(index, value,
             str(value))
plt.xticks(tec)
plt.ylabel('Tempo (s)')
plt.title('Tempo de execução do contentor')
plt.savefig('12-containertime.png', bbox_inches='tight')
plt.figure(12).clear
