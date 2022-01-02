import glob, shutil, os

month = input("Please enter the month:\n")
year = input("Please enter the year:\n")
st_date_dir = 'st_' + year + month

destination_dir = '/work/csp/sp2/scratch/ARGIA/forecast-html-monitoring/'
print('Using ' + destination_dir + st_date_dir + 'as destination dir')

# DIAGNOSTIC FILES #
print('Copying diagnostic files')
diagnostic_files = ['/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/mslp_ano_forecast_glo_'+year+month+'_lead0.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/mslp_ano_forecast_glo_'+year+month+'_lead1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/precip_ano_forecast_glo_'+year+month+'_lead0.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/precip_ano_forecast_glo_'+year+month+'_lead1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/sst_ano_forecast_glo_'+year+month+'_lead0.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/sst_ano_forecast_glo_'+year+month+'_lead1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/t2m_ano_forecast_glo_'+year+month+'_lead0.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/lead/t2m_ano_forecast_glo_'+year+month+'_lead1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/month/mslp_ano_forecast_glo_'+year+month+'_month1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/month/precip_ano_forecast_glo_'+year+month+'_month1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/month/sst_ano_forecast_glo_'+year+month+'_month1.png',
'/work/csp/sp1/scratch/runtimediag/'+year+month+'/month/t2m_ano_forecast_glo_'+year+month+'_month1.png',
'/work/csp/sp1/scratch/nemo_timeseries/'+year+month+'/plots/SPS3.5_'+year+month+'_sss_timeseries.png',
'/work/csp/sp1/scratch/nemo_timeseries/'+year+month+'/plots/SPS3.5_'+year+month+'_sst_timeseries.png']

for f in diagnostic_files:
    print('Copying ' + f)
    shutil.copy(f, destination_dir + st_date_dir + '/data/diagnostic')

# IC FILES #
print('Copying ic files')
ic_files = ['/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_01.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_02.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_03.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_04.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_05.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_06.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_07.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_08.png',
'/work/csp/sp1/scratch/'+month+'/SPS3.5_sic_obs_assim_IC_'+year+month+'_09.png',
'/work/csp/sp1/scratch/ICCLM2plot/'+year+month+'/clm_forcing_'+year+month+'.png', 
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/Uprofile_'+year+month+'.png', 
'/work/csp/sp1/scratch/'+month+'/noaa_anom_'+year+month+'.png', 
'/work/csp/sp1/scratch/'+month+'/'+year+month+'01_all_anom.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/Q10_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/Q500_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/T10_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/T500_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/U10_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/U500_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/Uprofile_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/V10_panel_CAMvsIFS_'+year+month+'.png',
'/work/csp/sp1/CMCC-SPS3.5/WORK_IC4CAM/plots/'+year+month+'/V500_panel_CAMvsIFS_'+year+month+'.png']

for f in ic_files:
    print('Copying ' + f)
    shutil.copy(f, destination_dir + st_date_dir + '/data/ic')


