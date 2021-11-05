import glob, shutil, os

###########
files = ['/work/csp/sp1/scratch/nemo_timeseries/202111/plots/SPS3.5_202111_sst_timeseries.png', '/work/csp/sp1/scratch/nemo_timeseries/202111/plots/SPS3.5_202111_sss_timeseries.png', '/work/csp/sp1/scratch/SIE/SIE_202111.png']

for f in files:
    shutil.copy(f, 'plots_folder_diag')

###########
###########
origin_folder_diag = '/work/csp/sp1/scratch/202111/diag/month/'
files = glob.iglob(os.path.join(origin_folder_diag, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder_diag')

###########
origin_folder_diag = '/work/csp/sp1/scratch/202111/diag/lead/'
files = glob.iglob(os.path.join(origin_folder_diag, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder_diag_lead')

