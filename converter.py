from pdf2image import convert_from_path

pages = convert_from_path('pdf_files/SPS3.5_sic_obs_assim_IC_202111.pdf', 500)
for idx,page in enumerate(pages):
	page.save('images/page_sic'+str(idx)+'.png', 'PNG')

pages = convert_from_path('pdf_files/clm_forcing_202111.pdf', 500)
for idx,page in enumerate(pages):
	page.save('images/page_clm'+str(idx)+'.png', 'PNG')

pages = convert_from_path('pdf_files/10hPa_IC_vs_IFS_202111.pdf', 500)
for idx,page in enumerate(pages):
	page.save('images/page_10hPa'+str(idx)+'.png', 'PNG')

pages = convert_from_path('pdf_files/500hPa_IC_vs_IFS_202111.pdf', 500)
for idx,page in enumerate(pages):
	page.save('images/page_500hPa'+str(idx)+'.png', 'PNG')

pages = convert_from_path('pdf_files/monitorforecast_20211102-125607.pdf', 500)
for idx,page in enumerate(pages):
	page.save('images/page_monitor'+str(idx)+'.png', 'PNG')
