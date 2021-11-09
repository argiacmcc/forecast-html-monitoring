
from pdf2image import convert_from_path

pages = convert_from_path('202111_Lead0.pdf', 500)
for idx,page in enumerate(pages):
	page.save('im'+str(idx)+'.png', 'PNG')
