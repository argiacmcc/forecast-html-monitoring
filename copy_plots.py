import glob, shutil, os

origin_folder='/work/csp/sp1/scratch/11/'

files = [origin_folder+'SPS3.5_sic_obs_assim_IC_202111_01.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_02.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_03.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_04.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_05.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_06.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_07.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_08.png', origin_folder+'SPS3.5_sic_obs_assim_IC_202111_09.png']

for f in files:
    shutil.copy(f, 'plots_folder')

###########
files = ['/work/csp/sp1/scratch/ICCLM2plot/202111/clm_forcing_202111.png', '/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/202111/Uprofile_202111.png', '/work/csp/sp1/scratch/11/noaa_anom_202111.png', '/work/csp/sp1/scratch/11/20211101_all_anom.png']

for f in files:
    shutil.copy(f, 'plots_folder')

###########
origin_folder_cam = '/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/202111/'
files = glob.iglob(os.path.join(origin_folder_cam, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder')

