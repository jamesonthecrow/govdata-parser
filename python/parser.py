"""This code parses data from the American Community Survey.
We perform the task using two main data structures, the actual survey data
and the header information for data columns.  For each row in the ACS, we get
the proper column headers using the provided sequence number, looking up the sequence
informatin in our header data structure.

In order to perform this parsing, we first identify the hierarchy present
in the column header information.  We need to give each column in the database a unique
name so while two census tables may contain data for 'male' and 'female' we 
must provide unique column names to enter them into the database.  To do this,
we include the entire hierarchy into each column name delineating levels with the '|'
symbol."""
from starflow.utils import MakeDir
import os
import xlrd
PATH = "/Users/jltoole/Documents/Projects/GovData/"

def acs_downloader():
	


def CreateHeaderDict():
    PATH = "/Users/jltoole/Documents/Projects/GovData/"

    fid = open(PATH + 'data/headers.txt','rU')
    #wfid = open(PATH + 'data/hierachy.txt', 'w')

    wb = xlrd.open_workbook(PATH + '/data/headers.xls')
    sheet = wb.sheet_by_index(0);

    # There are 5 levels table data
    lvl1 = '' # this is the general topic of the table
    lvl2 = '' 
    lvl3 = ''
    lvl4 = '' # levels 4 and 5 can be loosely interpreted as column heads
    lvl5 = '' 

    headers = {}
    
    for row in range(1,sheet.nrows):
 
        # read in the rest of the line and update the heirarchy based on identifiers in the file
        
        source = str(sheet.cell(row,0).value)
        table = str(sheet.cell(row,1).value)
        seq = str(sheet.cell(row,2).value)
        seq = seq[0:-2]
        line = str(sheet.cell(row,3).value)
        startpos = str(sheet.cell(row,4).value)
        tablecells = str(sheet.cell(row,5).value)
        seqcells = str(sheet.cell(row,6).value)
        if type(sheet.cell(row,7).value) is unicode:
            title = sheet.cell(row,7).value.encode('utf-8')
        else:
            title = str(sheet.cell(row,7).value)
        subjectarea = str(sheet.cell(row,8).value) 
            
        # Below are rules to identify the heirarchy for each line in the header file
        if subjectarea != '':
            lvl1 = subjectarea
            lvl2 = title
            lvl3 = ''
            lvl4 = ''
            lvl5 = ''
        if line == '' and subjectarea == '':
            lvl3 = title
            lvl4 = ''
            lvl5 = ''
        if ':' == title[-1]:
            lvl4 = title
            lvl5 = ''
        if  title[-1] != ':' and line != '':
            lvl5 = title

    # Now we create a data structure that stores the column headers for each
    # sequence number.  From a row in the data file, we will take the sequence number
    # and return an array of unique column headers that can be used to identify records
        if headers.has_key(seq):
            if (line != '') and ('.5' not in line ):
                headers[seq]['headers'].append( lvl1+'|'+ lvl2+'|'+ lvl3+'|'+ lvl4+'|'+ lvl5)
        else:
            headers[seq] = {'headers' : [] }
        
        #print(lvl1 + '\t' + lvl2 + '\t' + lvl3 + '\t' +lvl4 + '\t' + lvl5 + '\n')
        #wfid.write( lvl1 + '\t' + lvl2 + '\t' + lvl3 + '\t' +lvl4 + '\t' + lvl5 + '\t' + line + '\n')
        # Also store the number of column headers
        for key in headers:
            headers[key]['NumHeaders'] = len(headers[key]['headers'])
    fid.close()
    #wfid.close()
    
    return headers

def ReadData(H):
    # The arguement of this function is a dictionary of column headers

    # Make a list of all files in data director
    DATADIR = 'data/Massachusetts_Tracts_Block_Groups_Only/'
    filelist = [file for file in os.listdir(PATH + DATADIR) if file.lower().endswith('.txt')]
    
    # Read in each file and get the column head for each row
    for fname in filelist:
        print fname
        fid = open(PATH + DATADIR + fname, 'rU')
        
        # read each line, parse it, and get the column heads from the headers dict
        for L in fid:
            l = L.split(',')

            # make sure the first 6 columns of geo data are there
            if len(l) <= 6:
                print fname
                print l
                break

            seq = l[4]
            seq = int(seq)
            seq = str(seq)
            
            if seq != '':
                headers = H[seq]['headers']
            
                # check that the number of headers is the same as the number of columns in data
                if len(l) == H[seq]['NumHeaders'] + 6:
                    1 == 1
                else:
                    1==1
                    print('ERROR! NUMBER OF COLUMNS DOESNT MATCH NUMBER OF HEADERS!'+ '\t' + str(len(l)) + '\t' + str(H[seq]['NumHeaders']))
                    print('\n' + seq + '\t' + fname)
        
        fid.close()

H = CreateHeaderDict()
ReadData(H)
#for entry in  H['11']['headers']:
#    print entry + '\n'
#print('\n' + str(H['11']['NumHeaders']))

#fid.close()
#wfid.close()
