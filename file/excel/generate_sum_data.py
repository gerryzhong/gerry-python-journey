#--encoding=utf8--
import xlrd,xlwt
import os
import fnmatch
pattern = "*.xls"
files = os.listdir(".")
excel_files = fnmatch.filter(files,pattern)
wb_sum = xlwt.Workbook()
sheet = wb_sum.add_sheet('Worksheet',cell_overwrite_ok=True)
file_index = 0
total_amount = 0
total_record = 0
sum_row = 0;
for file in excel_files:
	print 'Start processing %s' % file
	wb = xlrd.open_workbook(file)
	sheeta = wb.sheet_by_index(0)
	start_row = 3 if file_index else 0
	for row_s in range(start_row,sheeta.nrows):
		total_record += 1
		for column_s in range(sheeta.ncols):
			cellValue = sheeta.cell_value(row_s,column_s)
			if row_s >= 3 and column_s == 1:
				total_amount += cellValue
			sheet.write(sum_row,column_s,cellValue)
		sum_row += 1
	file_index += 1
	print 'Finish processing %s' % file
print 'total_amount=%s' % total_amount
print 'total_record=%s' % (total_record - 3)
sheet.write(1,0,total_record - 3)
sheet.write(1,1,total_amount)
wb_sum.save('sum_data.xls')

		
