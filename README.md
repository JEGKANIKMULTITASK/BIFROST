# Github repo for the McStas simulations of BIFROST

*By: Kristine M. L. Krighaar* 

This repository contains the work of the BIFROST McStas model. However, no simulation data is included as files are to big, but can be provided upon reasonable reasonable request. 

** Illustration of the type of simulations performed **

![Pb Phonon dispersion](https://github.com/NBI-Magnetism-Group/BIFROST/blob/main/Phonon_GIF2.gif)

**NOTE**: Since I am using VScode as my editor, I have developed a slightly bad happit by being able to choose the environment for each individual notebook. Therefore multible are needed to make the scripts run. 

Backend written in McStasScript and datareduction is made using scipp and python. 
 
## Description of folders:
 
### Analyzer_positions: 
Files provided from Rasmus Toft-Petersen of analyzer the BIFOST backend geometry.
 
### BIFROST_Design_Article: 
 
Code used for the BIFROST design article. Includes energy resolution and brilliance transfer simulations, as well as guide drawing for the article.
 
Primary content: 

**Brilliance_flux**: Intrument file and python script to analyse the flux of BIFROSt at sample position (Made for design article and is not a part of MSc thesis).

**Guide_drawing**: Python script to construct comprehensive figure of the BIFROST guide with colors indicating the m-valus coating. Also have txt file of the placements of all the McStas components in the primary spectrometer. Used as a base line for the figure.

**Energy resolution**: 
    
- **Inelastic_line_resolution.ipynb**: Datatreatment to determine the energy resolution at different energy transfers and PSC settings. Also performs the calculatations for theoretical predictions and compare to the simulated data. This script makes the figure:

![FWHM overview](https://github.com/NBI-Magnetism-Group/BIFROST/blob/main/BIFROST_Design_Article/Energy_resolution/Inelastic_Energy_resolution_Article_limits.png)

- **BifrostFullInstrument_v2_inelastic_linewidths.instr**: The instrument file to produce the inelastic energy resolution data.

- **run.batch**: The *.batch* script used to commit to the ESS cluster.
- **Inelastic_lines.sh**: The *bash* script to run the simulations locally.
- **E_transfer_detectors.ipynb**: datatreatment of monitors and energy transfer distributions for the simulated data of inelastic resolutions.
- **BIFROST_article_plots.ipynb**: Figure of things needed for the BIFROST design article. 


### DataConversion: 
The dataconversion scripts that are using scipp. 

*To run notebooks the Env_with_KGS.yml should be used as I have my own libary I use on a daily basis.* 
 
### McStasScript: 
Code used to make a mcstas simulation of the backend of BIFROST. 

Primary content: 
- **BIFROST_UNION_Backend.ipynb**: The McStasScript code used to generate intrument files in wanted configurations. Instrument files are saved in the *run_folder* and the simulation results are saved in the *data_folder*.

- **backend_information_Analyzer_information.csv**: Information about the analysers geometry formated into a easily readable .csv format.

- **backend_information_Detector_information.csv**: Information about the detector geometry formated into a easily readable .csv format.
 
  

Hope the Env_with_KGS.yml works with KGS (Kristines Golden Standard), if not, please let me know. 
