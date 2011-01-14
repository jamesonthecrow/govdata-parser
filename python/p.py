PATH = "/Users/jltoole/Documents/Projects/GovData/"

fid = open(PATH + 'data/headers.txt','rU')

headers = {}

for L in fid:
    l = L.split('\t')
    if l[0] == 'File ID' or l[0] == '':
        1 == 1
    else:
        source = l[0]
        table  = l[1]
        seq    = l[2]
        line   = l[3]
        startpos = l[4]
        tablecells = l[5]
        seqcells = l[6]
        title = l[7]
        subjectarea = l[8]

        if headers.has_key(seq):
            # 
        else:
            headers[seq] = {'NumHead' : 0, 'Headers' : ''}
            headers[seq]['NumHead'] = 
