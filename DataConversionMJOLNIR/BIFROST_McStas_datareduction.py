import numpy as np
import h5py
import pandas as pd

class tube_measurement:
    def __init__(self,wedge=0, arc=0, tube=0, I=0, I_err=0, t_s = 0, y_m = 0, A4=0, A3=0, L_sd=0, Ef=0):
        self.wedge = wedge
        self.arc = arc
        self.tube = tube
        self.I = I
        self.I_err = I_err
        self.t_s = t_s
        self.y_m = y_m
        self.A3 = A3
        self.A4 = A4
        
        self.L_sd = L_sd
        self.Ef = Ef
    
        """ Get L_sd """
        back_info = pd.read_csv('../BIFROST_Design_Article/Energy_resolution/BIFROST_McStas_backend_information.csv')
        #back_info = back_info.loc[back_info['wedge_number'] == 1]

        back_info = np.asarray(back_info)[:,0:5]

        for j in range(len(back_info)):
            back_info[j,3] = back_info[j,3].replace(',','.')
            back_info[j,4] = back_info[j,3].replace(',','.')

        back_info = np.asarray(back_info, dtype=float)    
    
        back_info = back_info[(back_info[:,0]== 2.7)  & (back_info[:,2]== 4) | (back_info[:,0]== 3.2) & (back_info[:,2]== 4)| (back_info[:,0]== 3.8) & (back_info[:,2]== 5) | (back_info[:,0]== 4.4) & (back_info[:,2]== 5) | (back_info[:,0]== 5.0) & (back_info[:,2]== 5)]
        
        arc_values = {0: 2.7,1: 3.2,2: 3.8,3: 4.4,4: 5.0}

        # Loop through each arc value
        for arc, value in arc_values.items():
            # Check if the current arc value matches self.arc
            if self.arc == arc:
                # Filter the corresponding row from back_info
                ar = back_info[back_info[:, 0] == value]
                
                # Determine wedge conditions and calculate self.L_sd accordingly
                if self.wedge in (0, 3, 6):
                    self.L_sd = ar[0, 3] + ar[0, 4]
                elif self.wedge in (1, 4, 7):
                    self.L_sd = ar[1, 3] + ar[1, 4]
                elif self.wedge in (2, 5, 8):
                    self.L_sd = ar[2, 3] + ar[2, 4]
                break  # Exit the loop after finding the matching arc value


        """ Get Ef (Think about making the Ef correction based on the dA4 takeoff angle) """
        if arc == 0:
            self.Ef = 2.7
        if arc == 1:
            self.Ef = 3.2
        if arc == 2:
            self.Ef = 3.8
        if arc == 3:
            self.Ef = 4.4
        if arc == 4:
            self.Ef = 5.0


    def getI(self, filename):
        """
        Loading the data from the 
        """
        with h5py.File(filename, 'r') as file:
            self.I = file['entry1/data/signal_1Dspace_'+str(self.wedge)+'_'+str(self.arc)+'_'+str(self.tube)+'_dat/data'][()].astype('int64')
        return self.I
    
    def getI_err(self, filename):
        with h5py.File(filename, 'r') as file:
            self.I_err = file['entry1/data/signal_1Dspace_'+str(self.wedge)+'_'+str(self.arc)+'_'+str(self.tube)+'_dat/errors'][()].astype('int64')
        return self.I_err
    
    def get_t_s(self, filename):
        with h5py.File(filename, 'r') as file:
            self.t_s = file['entry1/data/signal_1Dspace_'+str(self.wedge)+'_'+str(self.arc)+'_'+str(self.tube)+'_dat/t__s_'][()]
        return self.t_s
    
    def get_y_m(self, filename):
        with h5py.File(filename, 'r') as file:
            self.y_m = file['entry1/data/signal_1Dspace_'+str(self.wedge)+'_'+str(self.arc)+'_'+str(self.tube)+'_dat/y__m_'][()]
        return self.y_m
    
    def getA3(self, filename): # Husk at finde rigtig index til A3
        with h5py.File(filename, 'r') as file:
            A3 = file['entry1/simulation/Param/A3'][()].astype('int64')[0]
            self.A3 = A3
        return self.A3
    
    
    def getA4(self, filename):
        #if self.y_m == 0:
        #    print('ERROR: Before A4 can be calculated first y_m need to be assigned by the .get_y_m(filename) function! ')
        
        # Get the angular offset from direct beam to first wedge
        with h5py.File(filename, 'r') as file:
            A4_offset = file['entry1/simulation/Param/A4'][()].astype('int64')[0]
            A4_offset = A4_offset

        # Get the angular offset from wedge number
        wedge_offsets = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80])
        wedge_offset = wedge_offsets[self.wedge]
            
        # Calculate the A4 degrees for each pixel on tube
        dA4 = np.degrees(np.arctan((self.y_m/self.L_sd)))
        
        # Add the offset for tank and wedge number
        self.A4 = A4_offset + wedge_offset + dA4

        return self.A4 