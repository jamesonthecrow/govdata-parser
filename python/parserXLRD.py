import xlrd

PATH = "/Users/saul/Downloads/Sequence_Number_and_Table_Number_Lookup.xls"

delim = "|"

wb = xlrd.open_workbook(PATH)

sheet = wb.sheet_by_index(0)

lvl1 = ''
lvl2 = ''
lvl3 = ''
lvl4 = ''
lvl5 = ''

headers = {}

last_subjectarea = ''
last_title = ''
last_seqcells = ''
last_tablecells = ''

for row in range(1,sheet.nrows):

		source 		= 	sheet.cell(row,0).value
		table  		= 	sheet.cell(row,1).value
		seq    		= 	sheet.cell(row,2).value
		line   		= 	sheet.cell(row,3).value
		startpos 	= 	sheet.cell(row,4).value
		tablecells 	= 	sheet.cell(row,5).value
		seqcells 	= 	sheet.cell(row,6).value
		title 		= 	sheet.cell(row,7).value
		subjectarea = 	sheet.cell(row,8).value

		if subjectarea != '' :
			header = subjectarea + delim + title
			running_subjectarea = subjectarea
			running_title = title
			continue
			
		elif title[0:8] == 'Universe:' :
			running_title = running_title + title
			universe = title
			header = subjectarea + delim + title + delim + univers
			continue
			
		elif title[-1] == ':' :
			running_title = running_title + title
			header = subjectarea + delim + running_title 
			continue
		else :
			header = subjectarea + delim + running_title + delim + title
			print header + "\n"
			

