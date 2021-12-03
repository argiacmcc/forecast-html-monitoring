import glob, shutil, os

month = input("Please enter the month:\n")
#print ("the month is")
#print(type(month))
year = input("Please enter the year:\n")
#print ("the year is")
#print(type(year))

origin_folder = '/work/csp/sp1/scratch/'+month+'/'
plots_folder = 'plots_folder_'+year+month
print(plots_folder)

'''
print("path")
print(origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_01.png')
'''

origin_folder='/work/csp/sp1/scratch/11/'

files = [origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_01.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_02.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_03.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_04.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_05.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_06.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_07.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_08.png', origin_folder+'SPS3.5_sic_obs_assim_IC_'+year+month+'_09.png']

for f in files:
    shutil.copy(f, 'plots_folder')

###########
files = ['/work/csp/sp1/scratch/ICCLM2plot/'+year+month+'/clm_forcing_'+year+month+'.png', '/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/Uprofile_'+year+month+'.png', '/work/csp/sp1/scratch/11/noaa_anom_'+year+month+'.png', '/work/csp/sp1/scratch/11/'+year+month+'01_all_anom.png']

for f in files:
    shutil.copy(f, 'plots_folder')

###########
origin_folder_cam = '/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/'
files = glob.iglob(os.path.join(origin_folder_cam, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder')
