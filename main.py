import math, random
globalDirectory = {}
goods = []
def genGoods():
    for x in open("goods.txt"):
        name = x[:x.find(",")]
        x = x[1+x.find(","):]
        weight = x[:x.find(",")]
        x = x[1+x.find(","):]
        if "\n" in x:
            basePrice = x[:x.find("\n")]
        else:
            basePrice = x
        goods.append(Good(name,weight,basePrice))
    #print(goods)
    #for good in goods:
    #    print(good)
    

#Class for a good
class Good:
    name = ""
    weight = 1
    basePrice = 1
    def __init__(self, name, weight, basePrice):
        self.name = name
        self.weight = weight
        self.basePrice = basePrice
    def __str__(self):
        return ("Name: " + self.name + "\n  Weight: " + str(self.weight) + "\n  Base Price: " + str(self.basePrice))
    
#Function for generation of cities from list of names and suffixes
def genCities(number, size, gloDir,gds): 
    name = []
    for x in open("name.txt","r"):
        if x.find("\n") > 0:
            name.append(x[:x.find("\n")])
        else:
            name.append(x)
    nameMax = len(name)
    #print(name)
    #print(nameMax)
    suffix = []
    for x in open("suffix.txt", "r"):
        if x.find("\n") > 0:
            suffix.append(x[:x.find("\n")])
        else:
            suffix.append(x)
    sufMax = len(suffix)
    #print(suffix)
    #print(sufMax)
    used = []
    coords = []
    posGoods = []
    for good in gds:
        posGoods.append(good.name)
    numGoods = len(posGoods)
    for city in range(number):
        goodValues = []
        for x in range(numGoods):
            goodValues.append(random.uniform(.25,4))
        cityGoods = {}
        for good in posGoods:
            cityGoods[good] = goodValues[posGoods.index(good)]
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
        gloDir[City(x, y, name[nameNum]+suffix[sufNum], gloDir, cityGoods)] = [x, y]
        used.append(nameNum + nameMax * sufNum)
        coords.append(x + y * size)
   # for place in globalDirectory:
    #    place.printDir()

#City class
class City:
    locX = 0
    locY = 0
    name = ""
    gloDir = {}
    directory = dict()
    goods = {}
    def coords(self):
        return [self.locX, self.locY]
    def distance(self, coord):
        return math.sqrt((self.locX-coord[0])**2 + (self.locY - coord[1])**2)
    def __str__(self):
        return self.name#+"\n" + str(self.directory)
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
    def printPrices(self):
        for good in self.goods:
            print("  Good: " + good + "\n  Price: %.2f" % self.goods[good])
    def assembleDirectory(self):
        for place in self.gloDir:
            if place != self:
                self.addDir(place.name, self.distance(place.coords()))
                place.addDir(self.name, self.distance(place.coords()))
            else:
                self.addDir(self.name, 0)
    def __init__(self, x, y, nym, globalDir, gds = {}, dire = {}):
        self.locX = x
        self.directory = dire
        self.locY = y
        self.name = nym
        self.goods = gds
        self.gloDir = globalDir
        self.updateDirectory()
        self.assembleDirectory()

class Player:
    location = City(0,0,"Null", globalDirectory)
    name = ""
    inventory = {}
    money = 100
    def __init__(self, loc, name, inv, money):
        self.location = loc
        self.name = name
        self.inventory = inv
        self.money = money
    def giveLoc(self):
        return self.location
    def moveLoc(self, newLoc):
        self.location = newLoc
    def buyGood(self, good, quantity):
        self.inventory[good] += quantity
        self.money -= good.basePrice * quantity * location.goods[good]

cont = True
while(Cont):
    print("Hello, welcome to GoodsQuest")
    
"""gagetown = City(0, 0, "Gagetown", globalDirectory)
samville = City(0, 1, "Samville", globalDirectory)
charlieburg = City (2, 2, "Charlieburg", globalDirectory)
gagetown.printDir()
samville.printDir()
charlieburg.printDir()"""
#genGoods()
#genCities(10,4,globalDirectory,goods)
"""for place in globalDirectory:
	print(place)
	place.printPrices()"""
