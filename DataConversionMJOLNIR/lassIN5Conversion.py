"""
Created on Thu Nov 16 09:37:50 2023
 
@author: lass_j
 
 
Import and plotting of IN5 data in 3D
"""
 
 
try:
    import IPython
    shell = IPython.get_ipython()
    shell.enable_matplotlib(gui='qt')
except:
    pass
import os,sys
from os.path import join
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
sys.path.append(r"C:\Users\lass_j\Documents\Software\MJOLNIR")
 
 
 
 
from MJOLNIR.Data import DataSet,Sample,Mask
from MJOLNIR._tools import fileListGenerator
 
files = fileListGenerator('1246', r'C:\Users\lass_j\Documents\CAEMA2023\20230045_Ni3TeO6_MA02',year = 2023)
   
df = DataSet.DataSet(files)[0]
sample = df.sample
 
# h=kkk
 
from MJOLNIR import TasUBlibDEG
from scipy.optimize import curve_fit
import pickle
 
dat = None
convert = False
 
folder = r'C:\Users\lass_j\Documents\Ni3TeO6\IN52023\ConvertedData\3D\3D2'
 
if convert:
   
    files = os.listdir(folder)
   
    dat = []
   
    for file in files:
        if not file.split(os.path.extsep)[-1] == 'mat': continue
        data = loadmat(os.path.join(folder,file))
        E,H,K,L,I,I_err,nonZero = data['dat'][0][0]
       
        E = E.flatten()
        H = H[0][0].flatten()
        K = K.flatten()
        L = L[0][0].flatten()
        I = I.flatten().reshape(len(H)-1,len(L)-1)
        I_err = I_err.flatten().reshape(len(H)-1,len(L)-1)
       
        HCentre = H[:-1]+np.diff(H)*0.5
        LCentre = L[:-1]+np.diff(L)*0.5
   
        
        HH,LL = [x.T for x in np.meshgrid(HCentre,LCentre)]
       
        HHin = HH[nonZero>0]
        LLin = LL[nonZero>0]
       
        qx, qy = np.einsum('ij,j...->i...',sample.convert,[HHin,LLin])
       
        
        cIn = nonZero[nonZero>0]
        inside = [qx,qy,np.ones_like(qx)*E,I[nonZero>0]*cIn,cIn]
        dat.append(inside)
        # h=kkk
   
    
    dat = np.asarray(np.concatenate(dat,axis=1))
   
    np.save(os.path.join(folder,'data'),dat)
    #pickle.dump(sample, os.path.join(folder,'sample'))
    #
   
if dat is None:
    dat = np.load(os.path.join(folder,'data.npy'))
 
df.qx = dat[0]
df.qy = dat[1]
df.energy = dat[2]
df.I = dat[3]
df.Monitor = dat[4]
df.Norm = np.ones_like(df.I)
df.type = 'nxs'

ds = DataSet.DataSet(df)