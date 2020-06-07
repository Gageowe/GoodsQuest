import math, random
globalDirectory = {}

def genCities(number, size, gloDir):
    name = []
    for x in open("name.txt","r"):
        if x.find("\n") > 0:
            name.append(x[:x.find("\n")])
        else:
            name.append(x)
    nameMax = len(name)
    print(name)
    print(nameMax)
    suffix = []
    for x in open("suffix.txt", "r"):
        if x.find("\n") > 0:
            suffix.append(x[:x.find("\n")])
        else:
            suffix.append(x)
    sufMax = len(suffix)
    print(suffix)
    print(sufMax)
    used = []
    coords = []
    for city in range(number):
        x = random.randint(0,size);
        y = random.randint(0,size);
        while((x + y*size) in coords):
            x = random.randint(0,size);
            y = random.randint(0,size);
        nameNum = random.randint(0,nameMax-1);
        sufNum = random.randint(0,sufMax-1);
        while((nameNum + nameMax * sufNum) in used):
            nameNum = random.randint(0,nameMax-1);
            sufNum = random.randint(0,sufMax-1);
        gloDir[City(x, y, name[nameNum]+suffix[sufNum], gloDir)] = [x, y]
        used.append(nameNum + nameMax * sufNum)
        coords.append(x + y * size)
    for place in globalDirectory:
        place.printDir()

class City:
    locX = 0
    locY = 0
    name = ""
    gloDir = {}
    directory = dict()
    def coords(self):
        return [self.locX, self.locY]
    def distance(self, coord):
        return math.sqrt((self.locX-coord[0])**2 + (self.locY - coord[1])**2)
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
            dis = self.directory[place] * 10
            print("  Distance: " + "%.2f" % dis)
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
"""gagetown = City(0, 0, "Gagetown", globalDirectory)
samville = City(0, 1, "Samville", globalDirectory)
charlieburg = City (2, 2, "Charlieburg", globalDirectory)
gagetown.printDir()
samville.printDir()
charlieburg.printDir()"""

