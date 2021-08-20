import csv

distances = []
#this method create a dictionary of the location and package ID. O(N) Complexity
def createpair(row):
    loc={}
    i =0
    while i < 27:
        loc[i]= float(row[i])
        i+=1
    return loc

#read from distances CSV. O(N) complexity
with open('data/distances.csv', encoding='utf-8-sig') as dis_csv:
    dis = csv.reader(dis_csv, delimiter=',')
    for row in dis:
        distances.append(createpair(row))

#this method return the distance in respect to current location . O(1) complexity
def getdistance(currentloc, locid):
    return distances[currentloc].get(locid)





