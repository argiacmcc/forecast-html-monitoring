import glob, shutil, os

month = input("Please enter the month:\n")
#print ("the month is")
#print(type(month))
year = input("Please enter the year:\n")
#print ("the year is")
#print(type(year))

###########
files = ['/work/csp/sp1/scratch/nemo_timeseries/'+year+month'/plots/SPS3.5_'+year+month'_sst_timeseries.png', '/work/csp/sp1/scratch/nemo_timeseries/'+year+month'/plots/SPS3.5_'+year+month'_sss_timeseries.png', '/work/csp/sp1/scratch/SIE/SIE_'+year+month'.png']

for f in files:
    shutil.copy(f, 'plots_folder_diag')

###########
###########
origin_folder_diag = '/work/csp/sp1/scratch/'+year+month'/diag/month/'
files = glob.iglob(os.path.join(origin_folder_diag, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder_diag')

###########
origin_folder_diag = '/work/csp/sp1/scratch/'+year+month'/diag/lead/'
files = glob.iglob(os.path.join(origin_folder_diag, "*.png"))
for f in files:
    shutil.copy(f, 'plots_folder_diag_lead')
