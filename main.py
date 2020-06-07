import math
globalDirectory = {}
class City:
    locX = 0
    locY = 0
    name = ""
    directory = {}
    def coords(self):
        return [x, y]
    def distance(self, coord):
        return math.sqrt((self.locX-coord[0])^2 + (self.locY - coord[1])^2)
    def __str__(self):
        return self.name+"\n" + str(self.directory)
    def updateDirectory(self, direc):
        direc[self] = [self.locX, self.locY]
    def assembleDirectory(self,globalDir):
        count = 0
        test = self
        for place in globalDir:
            count += 1
            for places in globalDir:
                print(places)
            print("Place: "+ place.name +"    "+ str(count)+ "    Self: "+self.name+"    Test: "+test.name)
            #print("Self "+ str(self)+"    "+ str(count)+"    "+place.name+"    "+test.name)
            self.directory[place.name] = self.distance(globalDirectory[place])
            #place.directory[self.name] = self.distance(globalDirectory[place])
    def __init__(self, x, y, nym):
        self.locX = x
        self.locY = y
        self.name = nym
        self.updateDirectory(globalDirectory)
        self.assembleDirectory(globalDirectory)
gagetown = City(0, 0, "Gagetown")
#print("Global Directory:\n    " + str(globalDirectory))
#print(gagetown)
samville = City(0, 1, "Samville")
#print("Global Directory:\n    " + str(globalDirectory))
#print(samville)
#print(gagetown)
charlieburg = City (2, 2, "Charlieburg")
#print("Global Directory:\n    " + str(globalDirectory))
#for place in globalDirectory:
#    print(place)
