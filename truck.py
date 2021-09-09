from hashtable import HashTable
from distances import *
from datetime import datetime, timedelta
from packages import readpackages
from math import ceil


class Truck:
     #initialize the hashtable and total distance variable. O(1) Complexity
    def __init__(self):
        self.hashtable = HashTable()
        self.createhashtable()
        self.totaldistance=0
    # this method create a hashtable to store all packages. O(N) Complexity
    def createhashtable(self):
        for package in readpackages():
            self.hashtable.insert(package)

    #this method manually create the package list and set truck leaving time. O(1) complexity
    def loadtruck(self):
        truck1 = self.load([1, 2, 4, 7, 14, 15, 16, 19, 20, 21, 24, 26, 29, 33, 34, 40])
        truck2 = self.load([3, 11, 12, 13, 17, 18, 22, 23, 27, 30, 31, 35, 36, 37, 38, 39])
        truck3 = self.load([5, 6, 8, 9, 10, 25, 28, 32])
        self.route(truck1, '08:00:00')
        self.route(truck2, '08:00:00')
        self.route(truck3, '09:30:00')

    #this method load all the packages from the list to truck. O(N) Complexity
    def load(self, trucknum):
        temp = []
        for i in trucknum:
            temp.append(self.hashtable.search(i))
        return temp
    #sorting packages and delivery algorithm using nearest neighbor Algorithm. O(N^3) Complexity
    def route(self, trucknum, starttime):
        packagelist = trucknum
        currentloc = 0
        completedroute = []
        currenttime = datetime.strptime(starttime, '%H:%M:%S')
        location = 0
        distant = 0.0


        while len(packagelist) != 0:
            min = 99
            for i in packagelist:
                locID = i[1]
                if getdistance(currentloc, locID) <= min:
                    min = getdistance(currentloc, locID)
                    location = locID
            distant = distant + min
            for i in packagelist:
                if i[1] == location:
                    i[6] = currenttime.strftime("%H:%M:%S")
                    currenttime = (self.deliverytime(min, currenttime))
                    i[7] = currenttime.strftime("%H:%M:%S")
                    i[8] = 'Delivered'
                    completedroute.append(i)
                    packagelist.pop(packagelist.index(i))
                    currentloc = location
                    break

        for package in completedroute:
            self.hashtable.update(package)
        self.totaldistance = self.totaldistance + distant

    #this method calculate delivery time. O(1) complexity
    @staticmethod
    def deliverytime(dis, currenttime):
        speed = 18
        time_traveled = ceil((dis / speed) * 60)
        currenttime += timedelta(minutes=time_traveled)
        return currenttime
