import csv

skdict = {}

with open("Levels_Table_export.csv") as csvfile:
    csvr = csv.reader(csvfile) 
    for row in csvr:
        sk, z, plan, refpt = row[7], row[10], row[11], row[13]
        if sk and z:
            skdict[sk] = 1
            print ",".join([sk, z, plan, refpt])
             
