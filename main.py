import math
globalDirectory = {}
helpMe = 0
class City:
    locX = 0
    locY = 0
    name = ""
    gloDir = {}
    directory = dict()
    def coords(self):
        return [self.locX, self.locY]
    def distance(self, coord):
        return math.sqrt((self.locX-coord[0])^2 + (self.locY - coord[1])^2)
    def __str__(self):
        return self.name+"\n" + str(self.directory)
    def updateDirectory(self):
        self.gloDir[self] = [self.locX, self.locY]
    def addDir(self, name, distance):
        self.directory[name] = distance
    def printDir(self):
        print("Directory of " + self.name)
        for place in self.directory:
            print("  Place: " + place)
            print("  Distance: " + str(self.directory[place]))
    def assembleDirectory(self):
        for place in self.gloDir:
            if place != self:
                self.addDir(place.name, self.distance(place.coords()))
                place.addDir(self.name, self.distance(place.coords()))
            else:
                self.addDir(self.name, 0)
    def __init__(self, x, y, nym, globalDir, dire = {}):
        self.locX = x
        self.directory = dire
        self.locY = y
        self.name = nym
        self.gloDir = globalDir
        self.updateDirectory()
        self.assembleDirectory()
gagetown = City(0, 0, "Gagetown", globalDirectory)
samville = City(0, 1, "Samville", globalDirectory)
charlieburg = City (2, 2, "Charlieburg", globalDirectory)
gagetown.printDir()
samville.printDir()
charlieburg.printDir()
