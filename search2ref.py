import numpy
import csv

infile  = './search.csv'
outfile = './references.csv'

allrefs={}
with open(infile, 'r') as file:
    reader = csv.reader(file)
    next(reader, None)  # skip the headers
    for row in reader:
        slast  = row[1]
        sfirst = row[2]
        rawrefs  = row[4]
        if len(row[4])==0: continue
        rawrefs = rawrefs.split('; ')
        for rawref in rawrefs:
            rawref = rawref.split(',')
            if len(rawref)<2: continue
            rawname = rawref[0]
            last  = rawname.split(' ')[-1].strip()
            first = ' '.join(rawname.split(' ')[:-1]).strip()
            name = last+" "+first
            email = rawref[1].strip()
            sname=f'{slast}, {sfirst}'
            if name not in allrefs:
                allrefs[name] = {'Last':last, 'First':first, 'Email':email, 'Applicants' : sname}
            else:
                allrefs[name]['Applicants'] += f'; {slast}, {sfirst}'

with open(outfile, 'w', newline='') as csvfile:
    fieldnames = allrefs[next(iter(allrefs))].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for name in sorted(allrefs.keys(),key=str.casefold):
        writer.writerow(allrefs[name])
