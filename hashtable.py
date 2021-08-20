from datetime import datetime


class HashTable:
    #initialized hash table and bucket size. O(1) Complexity
    def __init__(self, table_size=10):
        self.hashTable = []
        self.bucket = 0
        i = 0
        while i < table_size:
            self.hashTable.append([])
            i += 1
    # return hashid. O(1) Complexity
    def hashid(self, package):
        return int(package[0]) % len(self.hashTable)
    # insert a package into the hashtable. O(1) complexity
    def insert(self, package):
        self.bucket = self.hashid(package)
        self.hashTable[self.bucket].append(package)
    #search for a specific package in hash table. O(N^2) Complexity
    def search(self, id):
        for bucket in self.hashTable:
            for package in bucket:
                if int(package[0]) == id:
                    return package

    #return a formatted string  for look up function. O(N^2) Complexity
    def printformat(self, id, time):
        for bucket in self.hashTable:
            for package in bucket:
                deliveredtime = datetime.strptime(package[7], '%H:%M:%S')
                starttime = datetime.strptime(package[6], '%H:%M:%S')
                if int(package[0]) == id and deliveredtime < time:
                    string = 'Package #' + str(package[0]) + '      Delivered at: ' + str(
                        package[7] + "{:10s}".format('      Address: ') + str(package[2]))
                    return string

                elif int(package[0]) == 9 and time < datetime.strptime('10:20:00', '%H:%M:%S'):
                    string = 'Package #' + str(package[0]) + '      Status : Not Delivered ' + '      Address: Wrong address listed, will update at 10:20AM'
                    return string
                elif int(package[0]) == id:
                    string = 'Package #' + str(package[0]) + '      Status : Not Delivered ' + '      Address: ' + str(package[2])
                    return string

    #delete a package from hash table. O(N^2) Complexity
    def delete(self, id):
        for bucket in self.hashTable:
            for package in bucket:
                if int(package[0]) == id:
                    bucket.remove(package)

    #update a package from hash table. O(1) Complexity
    def update(self, package):
        self.delete(package[0])
        self.insert(package)
