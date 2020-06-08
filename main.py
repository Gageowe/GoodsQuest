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
        self.basePrice = int(basePrice)
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
    def nPrintDir(self):
        print("Directory of " + self.name)
        for place in self.directory:
            dis = self.directory[place] * 10
            print(" " + place + ":  %.2f" % dis)
    def printPrices(self):
        for good in self.goods:
            price = float(self.goods[good])*goods[goodNames.index(good.lower())].basePrice
            print("  " + good + ": %.2f" % price)
    def getPrice(self, good):
        if good in goodNames:
            return self.goods[good.capitalize()]
        else:
            return 0
    def assembleDirectory(self):
        for place in self.gloDir:
            if place != self:
                self.addDir(place.name, self.distance(place.coords()))
                place.addDir(self.name, self.distance(place.coords()))
            else:
                self.addDir(self.name, 0)
    def __init__(self, x, y, nym, globalDir, gds = {}, dire = {}):
        self.locX = x
        self.directory = {}
        self.locY = y
        self.name = nym
        self.goods = gds
        self.gloDir = globalDir
        self.updateDirectory()
        self.assembleDirectory()

class Trader:
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
while(cont): #overall game loop
    print("Hello, welcome to GoodsQuest.\n")
    print("The goal is simple make 1,000,000 dollars")
    print("Different cities will buy and sell")
    print("goods for different prices.")
    pName = input("What is your name:  ")
    print("For now there are no options, good luck!")
    genGoods()
    genCities(16, 5, globalDirectory, goods)
    cityList = []
    for x in globalDirectory:
        cityList.append(x)
    cityNames = []
    for x in cityList:
        cityNames.append(x.name.lower())
    playerGoods = {}
    for x in goods:
        playerGoods[x] = 0
    goodNames = []
    for x in goods:
        goodNames.append(x.name.lower())
    player = Trader(cityList[0], pName, playerGoods, 100)
    pic = True #Player In City, loop of "turns"
    while(pic):
        print("\nWelcome to " + player.location.name)
        opt = True #player picking what to do
        while(opt):
            playerChoice = ""
            playerChoice = input("What would you you like to do?\n  View prices: [prices]\n  View the list of cities: [cities]\n  Move to a new city: [move]\n  View your inventory? [inventory]\n  Buy goods: [buy]  \n  Sell goods: [sell]\n  Quit: [quit]  ")
            playerChoice = playerChoice.lower()
            if playerChoice == "prices":
                print("Prices for " + player.location.name + " are: ")
                player.location.printPrices()
            elif playerChoice == "cities":
                player.location.nPrintDir()
            elif playerChoice == "move":
                move = True
                while(move == True):
                    where = ""
                    where = input("What city would you like to go to? ")
                    where = where.lower()
                    if where in cityNames:
                        player.moveLoc(cityList[cityNames.index(where)])
                        move = False
                        opt = False
                    elif where == "cancel":
                        move = False
                    else:
                        print("Please type the name of a city, or [cancel] to cancel moving cities")
            elif playerChoice == "inventory":
                print("Your inventory contains: ")
                print(str(player.money) +" dollars")
                for good in playerGoods:
                    print(good.name +"  "+ str(playerGoods[good]))
            elif playerChoice == "buy":
                trading = True
                while(trading):
                    toBuy = input("What would you like to buy? ")
                    toBuy = toBuy.lower()
                    if toBuy in goodNames:
                        choice = True
                        while(choice):
                            quant = input("How much "+ toBuy.capitalize() +" would you like to buy?  ")
                            if quant.isdigit():
                                cost = int(quant) * player.location.getPrice(toBuy) * goods[goodNames.index(toBuy)].basePrice
                                if cost <= player.money:
                                    player.money -= cost
                                    player.inventory[goods[goodNames.index(toBuy)]] += int(quant)
                                    choice = False
                                    trading = False
                                    
                                else:
                                    print("This would cost " + str(cost) + " dollars. You only have " + str(player.money) + " dollars.\n Please input a lower number.")
                            else:
                                print("Please input an integer")
                    elif (toBuy == "cancel"):
                        trading = False
                    else:
                        print("Please type the name of a good, or [cancel] to cancel buying goods")
            elif playerChoice == "sell":
                trading = True
                while(trading):
                    toBuy = input("What would you like to sell?  ")
                    toBuy = toBuy.lower()
                    if toBuy in goodNames:
                        choice = True
                        while(choice):
                            quant = input("How much "+ toBuy.capitalize() +" would you like to sell?  ")
                            if quant.isdigit():
                                cost = int(quant) * player.location.getPrice(toBuy) * goods[goodNames.index(toBuy)].basePrice
                                if int(quant) <= player.inventory[goods[goodNames.index(toBuy)]]:
                                    player.money += cost
                                    player.inventory[goods[goodNames.index(toBuy)]] -= int(quant)
                                    choice = False
                                    trading = False
                                    
                                else:
                                    print("You need " + str(quant) + " " + toBuy + ". You only have " + str(player.inventory[goodNames.index(toBuy)]) + " " + toBuy+ ".\n Please input a lower number.")
                            else:
                                print("Please input an integer")
                    elif (toBuy == "cancel"):
                        trading = False
                    else:
                        print("Please type the name of a good, or [cancel] to cancel selling goods")
            elif playerChoice == "quit":
                opt = False
                pic = False
                print("Sad to see you go.\n You ended the game with " +str(player.money) + " dollars.\n Thats just " + str(1000000 - player.money) + " dollars shy of 1,000,000 dollars.\n Better luck next time!")
            else:
                print("Please chose a valid option")
            if player.money >= 1000000:
                print("Congratulations!\n You made over 1,000,000 dollars!\nThats the end of the game.")
                opt = False
                pic = False
    choice = True
    while(choice):
        again = ""
        again = input("Would you like to play again? [yes] or [no]  ")
        if again.lower() == "yes":
            choice = False
        elif again.lower() == "no":
            choice = False
            cont = False
        else:
            print("Please type yes or no")

    
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
