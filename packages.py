import csv

# this method read and format all the packages from CSV. O(N) Complexity
def readpackages():
    with open('data/packages.csv', encoding='utf-8-sig', newline='') as packcvs:
        allpackages = []
        pack = csv.reader(packcvs)
        for i, row in enumerate(pack):
            packageid = int(row[0])
            locationid = int(row[1])
            address = row[2] + ", " + row[3] + ", " + row[4] + " " + row[5]
            weight = int(row[6])
            deadline = row[7]
            notes = row[8]
            status = 'At Hub'
            start = ''
            end = ''
            package = [packageid, locationid, address, weight, deadline, notes, start, end, status]
            allpackages.append(package)
        return allpackages
