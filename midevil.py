import pygame, sys, time, random, math, copy



pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((650,650))
pygame.display.set_caption("Midevil")
screen.set_alpha(None) #improve performance
#pygame.display.set_icon()


debugfont = pygame.font.Font("asset\\font\\debug.ttf", 12)
consolefont = pygame.font.Font("asset\\font\\console.ttf", 30)
textfont = pygame.font.Font("asset\\font\\console.ttf", 50)
itemFont = pygame.font.Font("asset\\font\\console.ttf", 25)
tinyFont = pygame.font.Font("asset\\font\\console.ttf", 18)



VERSION = 1.01




class image:
    """Class that handles images by keeping imported images in a dictionary so that do not have to be imported more than once."""
    images = {None:pygame.image.load("asset\\image\\none.png")} #start with the "null" image already imported
    def get(name):
        """Either returns the image if it has already been imported, or import it if it has not."""
        pic = image.images.get(name)
        if (pic == None):
            try:
                pic = pygame.image.load("asset\\image\\"+name+".png")
                image.images[name] = pic
            except Exception: #maybe should be more specific?
                return image.images.get(None)
        return pic
    def blit(name, x, y, width=50, height=50):
        """renders an image."""
        try:
            screen.blit(pygame.transform.scale(name, (width, height)), [x,y])
        except TypeError:
            screen.blit(pygame.transform.scale(image.get(name), (width, height)), [x,y])
    def reverse(picture):
        """Switches the order in the dictionary."""
        temp = {v: k for k, v in image.images.items()}
        return temp[picture]


class item:
    """Handles items in player inventories."""
    def __init__(self, name, type, rarity=0, picture=None, value=0, strength=0, speed=0, evasion=0, power=0, will=0, luck=0, armor=0, maxHealth=0, maxMana=0):
        """ADD MORE STATS HERE LATER"""
        self.name = name
        self.type = type
        self.rarity = rarity
        self.picture = image.get(picture)
        self.value = value
        self.strength = strength
        self.speed = speed
        self.evasion = evasion
        self.power = power
        self.will = will
        self.luck = luck
        self.armor = armor
        self.maxHealth = maxHealth
        self.maxMana = maxMana

    def getStats(self):
        """Get list of stats"""
        return [self.strength, self.speed, self.evasion, self.power, self.will, self.luck, self.armor, self.maxHealth, self.maxMana]

    
    def renderItem(self, x=0, y=0):
        """Render item for inventory as a toolbox, includes stats and other information."""
        total = 55 #this is used for calculating how big the final box should be
        for i in self.getStats():
            if (i != 0):
                total += 15

        

        
        key1 = {0:"Common", 1:"Uncommon", 2:"Rare", 3:"Epic", 4:"Unreal"}
        key2 = {0:[110, 110, 110],1:[156,156,156],2:[255,215,0],3:[255,0,0],4:[255,0,230]}
        pygame.draw.rect(screen, [255, 240, 199], [x, y, max(150, len(self.name)*10), total])
        pygame.draw.rect(screen, [44, 100, 76], [x, y, max(150, len(self.name)*10), total], 4)
        screen.blit(itemFont.render(self.name, True, key2[self.rarity]), [x+5, y])
        screen.blit(tinyFont.render(key1[self.rarity]+" "+self.type.capitalize(), True, [0,0,0]), [x+5, y+20])
        line = 45
        if (self.strength > 0):
            screen.blit(tinyFont.render("+"+str(self.strength)+" Strength",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.strength < 0):
            screen.blit(tinyFont.render(str(self.strength)+" Strength",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.speed > 0):
            screen.blit(tinyFont.render("+"+str(self.speed)+" Speed",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.speed < 0):
            screen.blit(tinyFont.render(str(self.speed)+" Speed",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.evasion > 0):
            screen.blit(tinyFont.render("+"+str(self.evasion)+" Evasion",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.evasion < 0):
            screen.blit(tinyFont.render(str(self.evasion)+" Evasion",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.power > 0):
            screen.blit(tinyFont.render("+"+str(self.power)+" Power",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.power < 0):
            screen.blit(tinyFont.render(str(self.power)+" Power",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.will > 0):
            screen.blit(tinyFont.render("+"+str(self.will)+" Will",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.will < 0):
            screen.blit(tinyFont.render(str(self.will)+" Will",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.luck > 0):
            screen.blit(tinyFont.render("+"+str(self.luck)+" Luck",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.luck < 0):
            screen.blit(tinyFont.render(str(self.luck)+" Luck",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.armor > 0):
            screen.blit(tinyFont.render("+"+str(self.armor)+" Armor",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.armor < 0):
            screen.blit(tinyFont.render(str(self.armor)+" Armor",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.maxHealth > 0):
            screen.blit(tinyFont.render("+"+str(self.maxHealth)+" HP",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.maxHealth < 0):
            screen.blit(tinyFont.render(str(self.maxHealth)+" HP",True,[255,0,0]),[x+5,y+line])
            line += 15
        if (self.maxMana > 0):
            screen.blit(tinyFont.render("+"+str(self.maxMana)+" Mana",True,[0,255,0]),[x+5,y+line])
            line += 15
        elif (self.maxMana < 0):
            screen.blit(tinyFont.render(str(self.maxMana)+" Mana",True,[255,0,0]),[x+5,y+line])
            line += 15
            
        











class player:
    """Information about the player.
    Stats: Strength, Speed, Evasion, Power, Will, Luck, HP, Mana"""
    x = 100
    y = 100
    pos = [2,2]

    select = None

    gold = 20
    name = ""
    picture = image.get("player")
    moving = None
    noclip = False
    moveRate = 1 #has to be divisable by 50?
    prevMove = 0
    staticMove = False
    inventory = [None, None, None, None,None, None, None, None,None, None, None, None,None, None, None, None] #None is empty slot
    equip = [None, None, None, None]

    strength = 5
    speed = 10
    evasion = 3
    power = 2
    will = 3
    luck = 1

    mana = 0
    maxMana = 0
    

    health = 10
    maxHealth = 10

    experience = 0
    level = 1

    def heal(ghost):
        player.health += ghost
        if player.health > player.maxHealth:
            player.health = player.maxHealth

    def findItem(ghost):
        """Attempt to add item to inventory. Returns false if that can't happen."""
        if player.inventoryFull():
            dialog.infoBox("Can't pick up "+ghost.name+", inventory is full.")
            return False
        else:
            for i in range(0,len(player.inventory)): #find an empty slot
                if player.inventory[i] == None:
                    player.inventory[i] = copy.copy(ghost)
                    dialog.infoBox("Got the "+ghost.name+"!",ghost.picture)
                    return True

    def inventoryFull():
        """Returns true if inventory is full."""
        for i in player.inventory:
            if i == None:
                return False
        return True



    def getStrengthMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.strength
        return total
    def getStrength():
        return player.strength + player.getStrengthMod()

    def getSpeedMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.speed
        return total
    def getSpeed():
        return player.speed + player.getSpeedMod()

    def getEvasionMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.evasion
        return total
    def getEvasion():
        return player.evasion + player.getEvasionMod()

    def getPowerMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.power
        return total
    def getPower():
        return player.power + player.getPowerMod()

    def getWillMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.will
        return total
    def getWill():
        return player.will + player.getWillMod()

    def getLuckMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.luck
        return total
    def getLuck():
        return player.luck + player.getLuckMod()

    def getMaxHealthMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.maxHealth
        return total
    def getMaxHealth():
        return player.maxHealth + player.getMaxHealthMod()

    def getMaxManaMod():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.maxMana
        return total
    def getMaxMana():
        return player.maxMana + player.getMaxManaMod()

    def getArmor():
        total = 0
        for i in player.equip:
            if (i != None):
                total += i.armor
        return total
    
    

    


    def update():
        """Called every tick. Moves the player, updates everything about them."""
        if (not player.staticMove):
            try:
                averageFPS = sum(pastFrameRates[50:-1])/len(pastFrameRates[50:-1])
            except ZeroDivisionError:
                averageFPS = clock.get_fps()
            #print(str(averageFPS))
            number = (.0003*math.pow(averageFPS,2)-(.087*averageFPS)+7.29)
            #print("Int: "+str(int(number))+", round: "+str(round(number))+", original: "+str(number)+", fps: "+str(math.pow(clock.get_fps(),2)))
            player.moveRate = int(number)
        if (player.moving == "up"):
            player.y -= player.moveRate
            if (player.y <= player.prevMove -50 ):
                player.moving = None
                player.y = player.prevMove - 50
        if (player.moving == "down"):
            player.y += player.moveRate
            if (player.y >= player.prevMove + 50):
                player.moving = None
                player.y = player.prevMove + 50
        if (player.moving == "left"):
            player.x -= player.moveRate
            if (player.x <= player.prevMove -50 ):
                player.moving = None
                player.x = player.prevMove - 50
        if (player.moving == "right"):
            player.x += player.moveRate
            if (player.x >= player.prevMove + 50):
                player.moving = None
                player.x = player.prevMove + 50

    def canMoveUp():
        try:
            if (player.noclip):
                return True
            if (player.moving == None and map.current.blocks[player.pos[0]][player.pos[1]-1].collision == False and player.pos[1]>0):
                return True
            return False
        except Exception as e:
            #print(str(e))
            return False
    def canMoveDown():
        try:
            if (player.noclip):
                return True
            if (player.moving == None and map.current.blocks[player.pos[0]][player.pos[1]+1].collision == False and player.pos[1]<map.current.getBounds()[1]):
                return True
            return False
        except:
            return False
    def canMoveLeft():
        try:
            if (player.noclip):
                return True
            if (player.moving == None and map.current.blocks[player.pos[0]-1][player.pos[1]].collision == False and player.pos[0]>0):
                return True
            return False
        except:
            return False
    def canMoveRight():
        try:
            if (player.noclip):
                return True
            if (player.moving == None and map.current.blocks[player.pos[0]+1][player.pos[1]].collision == False and player.pos[0]<map.current.getBounds()[0]):
                return True
            return False
        except:
            return False


    def moveUp():
        try:
            if (player.moving == None and player.canMoveUp()):
                player.moving = "up"
                player.pos[1] -= 1
                player.prevMove = player.y
        
            elif(map.current.blocks[player.pos[0]][player.pos[1]-1].teleport != None and player.moving == None):
                temp = map.current.blocks[player.pos[0]][player.pos[1]-1]
                player.pos[0] = temp.x
                player.pos[1] = temp.y
                player.x = temp.x*50
                player.y = temp.y*50
                map.current = map.get(temp.teleport)
            elif(map.current.blocks[player.pos[0]][player.pos[1]-1].action != None and player.moving == None):
                map.current.blocks[player.pos[0]][player.pos[1]-1].action()
        except Exception as e:
            #print(str(e))
            pass
    def moveDown():
        try:
            if (player.moving == None and player.canMoveDown()):
                player.moving = "down"
                player.pos[1] += 1
                player.prevMove = player.y
            
            elif(map.current.blocks[player.pos[0]][player.pos[1]+1].teleport != None and player.moving == None):
                temp = map.current.blocks[player.pos[0]][player.pos[1]+1]
                player.pos[0] = temp.x
                player.pos[1] = temp.y
                player.x = temp.x*50
                player.y = temp.y*50
                map.current = map.get(temp.teleport)
            elif(map.current.blocks[player.pos[0]][player.pos[1]+1].action != None and player.moving == None):
                map.current.blocks[player.pos[0]][player.pos[1]+1].action()
        except:
            pass
    def moveLeft():
        try:
            if (player.moving == None and player.canMoveLeft()):
                player.moving = "left"
                player.pos[0] -= 1
                player.prevMove = player.x
            
            elif(map.current.blocks[player.pos[0]-1][player.pos[1]].teleport != None and player.moving == None):
                temp = map.current.blocks[player.pos[0]-1][player.pos[1]]
                player.pos[0] = temp.x
                player.pos[1] = temp.y
                player.x = temp.x*50
                player.y = temp.y*50
                map.current = map.get(temp.teleport)
            elif(map.current.blocks[player.pos[0]-1][player.pos[1]].action != None and player.moving == None):
                map.current.blocks[player.pos[0]-1][player.pos[1]].action()
        except:
            pass
    def moveRight():
        try:
            if (player.moving == None and player.canMoveRight()):
                player.moving = "right"
                player.pos[0] += 1
                player.prevMove = player.x
            
            elif(map.current.blocks[player.pos[0]+1][player.pos[1]].teleport != None and player.moving == None):
                temp = map.current.blocks[player.pos[0]+1][player.pos[1]]





                
                player.pos[0] = temp.x
                player.pos[1] = temp.y
                player.x = temp.x*50
                player.y = temp.y*50
                map.current = map.get(temp.teleport)
            elif(map.current.blocks[player.pos[0]+1][player.pos[1]].action != None and player.moving == None):
                map.current.blocks[player.pos[0]+1][player.pos[1]].action()
        except:
            pass





class block:
    """Info about blocks (tiles)."""
    
    def __init__(self, picture, collision=False, teleport=None, x=0, y=0, action=None):
        """initialize the block. picture is a string."""
        self.picture = image.get(picture)
        self.collision = collision
        self.teleport = teleport
        self.x = x
        self.y = y
        self.action = action
    



class map:
    """Collection of blocks into a map."""
    
    current = None
    maps = {}
    def __init__(self, name, blocks):
        map.maps[name] = self
        self.blocks = blocks
    def get(name):
        ghost = map.maps.get(name)
        #print("ghost1: "+str(ghost))
        if (ghost == None):
            if (map.read(name)):
                #print("map read TRUE")
                ghost = map.maps.get(name)
                #print("ghost2: "+str(ghost))
            else:
                #print("map read FALSE")
                ghost = None
        return ghost
    
    def blit(self):
        global debug
        if (self != None): #if the player is on a map....
            for i in range(0,len(self.blocks)):
                for j in range(0,len(self.blocks[0])):
                    if (self.blocks[i][j] != None):
                        image.blit(self.blocks[i][j].picture, (i*50)-player.x+300, (j*50)-player.y+300)
                        if (debug and self.blocks[i][j].collision and self.blocks[i][j].teleport == None):
                            image.blit("collision", (i*50)-player.x+300, (j*50)-player.y+300)
                        elif (debug and self.blocks[i][j].teleport != None):
                            image.blit("teleport", (i*50)-player.x+300, (j*50)-player.y+300)
                            screen.blit(debugfont.render(self.blocks[i][j].teleport, True, [250,250,250]), [(i*50)-player.x+305,(j*50)-player.y+305])
                        
    def getBounds(self):
        return [len(self.blocks),len(self.blocks[0])]
    def export(self, ghost="test"):
        message = ghost+" = map(\""+ghost+"\",["
        for i in range(0,self.getBounds()[0]):
            if (i != 0):
                message += ","
            message += "["
            for j in range(0,self.getBounds()[1]):
                if j != 0:
                    message += ","
                if (self.blocks[i][j] == None):
                    message += "None"
                else:
                    message += "block(\""+image.reverse(self.blocks[i][j].picture)+"\","+str(self.blocks[i][j].collision)+","
                    if (self.blocks[i][j].teleport != None):
                        message += "\""+str(self.blocks[i][j].teleport)+"\","+str(self.blocks[i][j].x)+","+str(self.blocks[i][j].y)+","
                    else:
                        message += "None,"+str(self.blocks[i][j].x)+","+str(self.blocks[i][j].y)+","
                    if (self.blocks[i][j].action != None):
                        message += str(self.blocks[i][j].action.__name__)+")"
                    else:
                        message += "None)"
                

            message += "]"
        message += "])"
        
        f = open("data\\map\\"+ghost+".txt", 'w')
        f.write(message)
        f.close()
    def read(ghost):
        screen.fill([0,0,0])
        screen.blit(consolefont.render("Loading",True,[255,255,255]),[300,300])
        pygame.display.flip()
        try:
            f = open("data\\map\\"+ghost+".txt",'r')
            exec(f.readline())

        except Exception as e:
            #print("read error: "+str(e))
            f.close()
            return False
        f.close()
        return True
    def blank(x, y):
        ghost = []
        for i in range(0,x):
            timmy = []
            for j in range(0,y):
                timmy.append(None)
            ghost.append(timmy)
        return map("blank",ghost)
    def hover():
        """returns what block the cursor is hovering over."""
        try:
            for i in range(0,13):
                for j in range(0,13):
                    if collides(i*50,j*50,50,50):
                        #image.blit("collision",i*50,j*50,50,50)
                        #return map.current.blocks[i-player.pos[0]+6][j-player.pos[1]+6]
                        if (i+player.pos[0]-6<0 or j+player.pos[1]-6 < 0):
                            return None
                        return [i+player.pos[0]-6,j+player.pos[1]-6]
        except Exception as e:
            
            return None
                

    

    

class console:
    color = [255,255,255]
    enable = False
    log = []
    typing = ""
    limit = 10
    def blit():
        screen.blit(consolefont.render("> "+console.typing , True, console.color), [10,10])
        for i in range(0,console.limit):
            try:
                screen.blit(consolefont.render(console.log[i] , True, console.color), [10,(i*32)+37])
            except IndexError:
                pass
    def add(value):
        
        console.log.insert(0,value)
        if (len(console.log) > 20):
            console.log = console.log[0:-2]
    def clear():
        console.log = []

    def command(value):
        """try to complete a command"""
        dummy = value.split(' ', 1)
        ghost = value.lower().split()

        try:
            if (ghost[0] == "help"):
                if (ghost[1] == "all"):
                    console.add("get [variable]: shows the specified value.")
                    console.add("exec [command]: executes any command. Use carefully!")
                else:
                    console.add(eval(ghost[1]+".__doc__"))
            elif (ghost[0] == "teleport" or ghost[0] == "tp"):
                player.pos[0] += int(ghost[1])
                player.pos[1] += int(ghost[2])
                player.x += int(ghost[1])*50
                player.y += int(ghost[2])*50
            elif (ghost[0] == "flip"):
                coin = {0:"tails", 1:"heads"}
                console.add("Flipped "+coin[random.randint(0,1)])
            elif (ghost[0] == "roll"):
                console.add("Rolled a "+str(random.randint(1,6)))
            elif (ghost[0] == "random"):
                console.add(str(random.randint(int(ghost[1]), int(ghost[2]))))
            elif (ghost[0] == "exec" or ghost[0] == "execute"):
                temp = exec(dummy[1])
                if (temp != None):
                    console.add(str(temp))
            elif (ghost[0] == "get"):
                temp = eval(dummy[1])
                if (temp != None):
                    console.add(str(temp))
            elif (ghost[0] == "debug"):
                global debug
                debug = not debug
            elif (ghost[0] == "screenshot"):
                pygame.image.save(screen, ghost[1]+".png")
                console.add("Saved as "+ghost[1]+".png")
            elif (ghost[0] == "clear"):
                console.clear()
            elif (ghost[0] == "select"):
                exec("player.select = "+dummy[1])
                #print(dummy)
            elif(ghost[0] == "noclip"):
                player.noclip = not player.noclip
                console.add("noclip is "+str(player.noclip))
            elif (ghost[0] == "editor"):
                map.blank(int(ghost[1]),int(ghost[2]))
                map.current = map.get("blank")
                player.noclip = True
                player.pos = [0,0]
                player.x = 0
                player.y = 0
                console.add("Level editor open")
            else:
                console.add("Command not found.")
        except Exception as e:
            console.add("Error: "+str(e))
        console.add(value)

class dialog:

    def renderInfo(text, num=0, ghost=None):
        pygame.draw.rect(screen, [255, 240, 199], (50, 440, 550, 160))
        pygame.draw.rect(screen, [44, 100, 76], (50, 440, 550, 160), 4)

        line = 0
        LIMIT = 23
        final = ["","",""]
        text = text[0:num].split()
        #print(str(text))
        j = 0
        for i in range (0,3):
            #print("First loop #"+str(i))
            #print("Text: "+str(text))
            #print("Final: "+str(final))
            line = 0
            lion = True
            for j in range(0,len(text)):
                #print("Second loop: looking at "+str(j)+", which is "+text[j])
                if (len(text[j])+line>LIMIT):
                    #print("Too much! Breaking. Line is "+str(line)+", word was "+text[j])
                    text = text[(j):]
                    lion = False
                    break
                else:
                    final[i] += text[j]+" "
                    line += len(text[j])
            if (lion):
                text = text[(j+1):]
                #print("Slice array. Result is "+str(text))
        #print("Final: "+str(final))
        for i in range(0,3):     
            screen.blit(textfont.render(final[i],True,[10,10,10]), [75, 450 + (i*40)])

        if (ghost != None):
            pygame.draw.rect(screen, [255, 240, 199], (287, 340, 75, 75))
            pygame.draw.rect(screen, [44, 100, 76], (287, 340, 75, 75), 2)
            image.blit(ghost,292,345,65,65)

    def renderInput(text, num=0, arrow=True):
        dialog.renderInfo(text, num)
        if (num > len(text)):
            pygame.draw.rect(screen, [255, 240, 199], [350, 350, 250, 80])
            pygame.draw.rect(screen, [44, 100, 76], [350, 350, 250, 80], 4)
            if (arrow):
                screen.blit(textfont.render("Yes <",True,[0,230,0]),[380,365])
                screen.blit(textfont.render("No",True,[230,0,0]),[505,365])
                
            else:
                screen.blit(textfont.render("Yes",True,[230,0,0]),[380,365])
                screen.blit(textfont.render("> No",True,[0,230,0]),[473,365])
    def renderChoice(text, num=0,choice1=None, choice2=None, choice3=None, choice4=None, arrow=1):
        dialog.renderInfo(text, num)
        if (num > len(text)):
            if (choice4 != None):
                pygame.draw.rect(screen, [255, 240, 199], [300, 200, 300, 230])
                pygame.draw.rect(screen, [44, 100, 76], [300, 200, 300, 230], 4)
            elif (choice3 != None):
                
                pygame.draw.rect(screen, [255, 240, 199], [300, 200, 300, 180])
                pygame.draw.rect(screen, [44, 100, 76], [300, 200, 300, 180], 4)
            else:
                pygame.draw.rect(screen, [255, 240, 199], [300, 200, 300, 130])
                pygame.draw.rect(screen, [44, 100, 76], [300, 200, 300, 130], 4)
            if (arrow == 1):
                screen.blit(textfont.render("> "+choice1,True,[0,255,0]),[315,210])
            else:
                screen.blit(textfont.render(choice1,True,[0,0,0]),[315,210])
            if (arrow == 2):
                screen.blit(textfont.render("> "+choice2,True,[0,255,0]),[315,260])
            else:
                screen.blit(textfont.render(choice2,True,[0,0,0]),[315,260])
            if (arrow == 3):
                screen.blit(textfont.render("> "+choice3,True,[0,255,0]),[315,310])
            else:
                screen.blit(textfont.render(choice3,True,[0,0,0]),[315,310])
            if (arrow == 4):
                screen.blit(textfont.render("> "+choice4,True,[0,255,0]),[315,360])
            else:
                screen.blit(textfont.render(choice4,True,[0,0,0]),[315,360])
                
            
    def renderInventory(grabbed):
        pygame.draw.rect(screen, [255, 240, 199], [50, 50, 525, 325])
        pygame.draw.rect(screen, [44, 100, 76], [50, 50, 525, 325], 4)
        tick = 0
        for i in range(0,4):
            for j in range(0,4):
                pygame.draw.rect(screen, [200, 180, 160], [75+(i*75), 75+(j*75), 50, 50])
                if (player.inventory[tick] != None):
                    image.blit(player.inventory[tick].picture, 75+(i*75), 75+(j*75))
                    if (collides(75+(i*75), 75+(j*75), 50, 50)):
                        player.inventory[tick].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                tick += 1
                
                
        pygame.draw.rect(screen, [200, 180, 160], [375, 75, 75, 75])
        if (player.equip[0] != None):
            image.blit(player.equip[0].picture, 375,75,75,75)
        else:
            image.blit("helmet", 375,75,75,75)
        pygame.draw.rect(screen, [200, 180, 160], [475, 75, 75, 75])
        if (player.equip[1] != None):
            image.blit(player.equip[1].picture, 475,75,75,75)
        else:
            image.blit("chest", 475,75,75,75)
        pygame.draw.rect(screen, [200, 180, 160], [375, 175, 75, 75])
        if (player.equip[2] != None):
            image.blit(player.equip[2].picture, 375,175,75,75)
        else:
            image.blit("sword", 375,175,75,75)
        pygame.draw.rect(screen, [200, 180, 160], [475, 175, 75, 75])
        if (player.equip[3] != None):
            image.blit(player.equip[3].picture, 475,175,75,75)
        else:
            image.blit("trinket", 475,175,75,75)
        if (grabbed != None):
            image.blit(grabbed.picture, pygame.mouse.get_pos()[0] - 25, pygame.mouse.get_pos()[1]-25, 50, 50)


        screen.blit(tinyFont.render("Strength: "+str(player.strength)+" + "+str(player.getStrengthMod()),True,[200,10,10]),[375,255])
        screen.blit(tinyFont.render("Speed: "+str(player.speed)+" + "+str(player.getSpeedMod()),True,[100,255,100]),[375,270])
        screen.blit(tinyFont.render("Evasion: "+str(player.evasion)+" + "+str(player.getEvasionMod()),True,[10,200,10]),[375,285])
        screen.blit(tinyFont.render("Power: "+str(player.power)+" + "+str(player.getPowerMod()),True,[50,50,255]),[375,300])
        screen.blit(tinyFont.render("Will: "+str(player.will)+" + "+str(player.getWillMod()),True,[0,0,200]),[375,315])
        screen.blit(tinyFont.render("Luck: "+str(player.luck)+" + "+str(player.getLuckMod()),True,[200,200,10]),[375,330])
        screen.blit(tinyFont.render("Armor: "+str(player.getArmor()),True,[200,200,200]),[375,345])

        

        tick = 0
        for i in range(0,4):
            for j in range(0,4):
                if (collides(75+(i*75), 75+(j*75), 50, 50) and player.inventory[tick] != None):
                    player.inventory[tick].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                tick += 1
        if (collides(375, 75, 75, 75) and player.equip[0] != None):
            player.equip[0].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if (collides(475, 75, 75, 75) and player.equip[1] != None):
            player.equip[1].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if (collides(375, 175, 75, 75) and player.equip[2] != None):
            player.equip[2].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if (collides(475, 175, 75, 75) and player.equip[3] != None):
            player.equip[3].renderItem(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    def choiceBox(text, choice1, choice2, choice3=None, choice4=None):
        tick = 0
        arrow = 1
        while True:
            render()
            
            pygame.time.delay(5)
            tick += 1
            dialog.renderChoice(text, tick, choice1, choice2, choice3, choice4, arrow)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        arrow -= 1
                        if arrow < 1 and choice4 != None:
                            arrow = 4
                        elif arrow < 1 and choice3 != None:
                            arrow = 3
                        elif arrow < 1:
                            arrow = 2
                    if event.key == pygame.K_DOWN:
                        arrow += 1
                        if (arrow > 3 and choice4 == None) or (choice3 == None and arrow > 2)or (choice4 != None and arrow > 4):
                            arrow = 1
                    if event.key == pygame.K_SPACE:
                        if (tick < len(text)):
                            tick = len(text)
                        else:
                            return arrow
                    
            
    def inventory():
        lion = True
        selected = None
        while lion:
            render()
            dialog.renderInventory(selected)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and selected == None:
                        lion = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and selected == None: #pick item up
                        #left click
                        tick = 0
                        for i in range(0,4):
                            for j in range(0,4):
                                if (collides(75+(i*75), 75+(j*75), 50, 50) and player.inventory[tick] != None):
                                    selected = player.inventory[tick]
                                    player.inventory[tick] = None
                                tick += 1
                        if (collides(375, 75, 75, 75) and player.equip[0] != None):
                            selected = player.equip[0]
                            player.equip[0] = None
                        if (collides(475, 75, 75, 75) and player.equip[1] != None):
                            selected = player.equip[1]
                            player.equip[1] = None
                        if (collides(375, 175, 75, 75) and player.equip[2] != None):
                            selected = player.equip[2]
                            player.equip[2] = None
                        if (collides(475, 175, 75, 75) and player.equip[3] != None):
                            selected = player.equip[3]
                            player.equip[3] = None
                    elif event.button == 1 and selected != None: #place item down
                        tick = 0
                        for i in range(0,4):
                            for j in range(0,4):
                                if (collides(75+(i*75), 75+(j*75), 50, 50) and player.inventory[tick] == None):
                                    player.inventory[tick] = selected
                                    selected = None
                                tick += 1
                        if (collides(375, 75, 75, 75) and player.equip[0] == None and selected.type == "helmet"): #helmet
                            player.equip[0] = selected
                            selected = None
                        if (collides(475, 75, 75, 75) and player.equip[1] == None and selected.type == "chestplate"): #chest
                            player.equip[1] = selected
                            selected = None
                        if (collides(375, 175, 75, 75) and player.equip[2] == None and selected.type == "sword"): #sword
                            player.equip[2] = selected
                            selected = None
                        if (collides(475, 175, 75, 75) and player.equip[3] == None and selected.type == "trinket"): #trinket
                            player.equip[3] = selected
                            selected = None
                    if event.button == 3 and selected == None:
                        #right click
                        tick = 0
                        for i in range(0,4):
                            for j in range(0,4):
                                if (collides(75+(i*75), 75+(j*75), 50, 50) and player.inventory[tick] != None and player.inventory[tick].type == "consumable"):
                                    if (player.inventory[tick].name == "Health Potion"):
                                        if (dialog.inputBox("Consume the Health Potion?")):
                                            dialog.infoBox("Healed 15 HP.")
                                            player.heal(15)
                                            player.inventory[tick] = None
                                tick += 1
                        
                        
    def inputBox(text):
        global debug
        debug = False
        console.enable = False
        tick = 0
        arrow = True
        while True:
            render()
            pygame.time.delay(5)
            tick += 1
            dialog.renderInput(text, tick, arrow)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if (tick < len(text)):
                            tick = 100
                        elif (tick >= len(text)):
                            return arrow
                    if event.key == pygame.K_LEFT:
                        arrow = True
                    if event.key == pygame.K_RIGHT:
                        arrow = False
                            
    def infoBox(text, ghost=None):
        global debug
        debug = False
        console.enable = False
        beast = True
        tick = 0
        while beast:
            render()
            pygame.time.delay(5)
            tick += 1
            dialog.renderInfo(text, tick, ghost)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if (tick < len(text)):
                            tick = 100
                        elif (tick >= len(text)):
                            beast = False
    def shop(text, item1, item2=None, item3=None):

        while True:
            if (item3 != None):
                result = dialog.choiceBox(text, item1.name, item2.name, item3.name, "Leave")
            elif (item2 != None):
                result = dialog.choiceBox(text, item1.name, item2.name, "Leave")
            else:
                result = dialog.choiceBox(text, item1.name, "Leave")
            if ((result == 4 and item3 != None) or (result == 3 and item2 != None) or (result == 2 and item2 == None)):
                return
            else:
                ghost = {1:item1,2:item2,3:item3}
                if (dialog.inputBox("Purchase the "+ghost[result].name+" for "+str(ghost[result].value)+" gold?")):
                    if (player.gold < ghost[result].value):
                        dialog.infoBox("Not enough gold.")
                    elif (player.inventoryFull()):
                        dialog.infoBox("Inventory is full.")
                    else:
                        player.gold -= ghost[result].value
                        player.findItem(copy.copy(ghost[result]))
                
                    




















def collides(x, y, width, height):
    if (pygame.mouse.get_pos()[0] >= x and pygame.mouse.get_pos()[0] <= (x+width) and pygame.mouse.get_pos()[1] >= y and pygame.mouse.get_pos()[1] <= (y+height)):
        return True
    return False









def villager1():
    if (dialog.inputBox("I can tell you how much all of your items are worth if you wish.")):
        total = 0
        for i in player.inventory:
            if (i != None):
                total += i.value
        for i in player.equip:
            if (i != None):
                total += i.value
        if (total == 0):
            dialog.infoBox("You don't have anything of value.")
        elif (total < 300):
            dialog.infoBox("Total value is "+str(total)+" gold.")
        else:
            dialog.infoBox("Total value is "+str(total)+" gold. Thats a lot!")
    else:
        dialog.infoBox("Bye then.")
def villager2():
    if (dialog.inputBox("Hello there, would you like to buy my cross for 40 gold?")):
        if (player.inventoryFull()):
            dialog.infoBox("Sorry, doesn't look like you have the room to buy this.")
        elif (player.gold < 40):
            dialog.infoBox("Doesn't look like you have enough money.")
        else:
            player.gold -= 40
            player.findItem(item("Gold Cross","trinket",1,"cross",40, 0, 0, 0,0, 2, 3))
    else:
        dialog.infoBox("Maybe another time.")
def villager3():#shopkeeper.
    dialog.shop("Come and see my wares.",item("Health Potion","consumable",0,"healthPotion",10),item("Copper Sword","sword",0,"copperSword",25,5))
    
def treasure1():
    if (player.findItem(item("Stone Sword","sword",0,"stoneSword",10,3))):
        map.get("fountain").blocks[10][1] = block("tan",False)
def well():
    if (dialog.inputBox("Drop a gold in the well?")):
        if (player.gold > 0):
            player.gold -= 1
            dialog.infoBox("You drop a gold piece in the well. You hear it spash into water far below.")
            if (random.randint(1,1000)==1):
                dialog.infoBox("You luck increased by 1!")
                player.luck += 1
        else:
            dialog.infoBox("Not enough gold.")
def barrel1():
    amount = random.randint(1,3)+player.luck
    dialog.infoBox("You found "+str(amount)+" gold.")
    player.gold += amount
    map.get("shop").blocks[13][1] = block("barrel",True)
    
def sign1():
    dialog.infoBox("This well was constructed in memory of the late Duchess of Erenburg,")
    dialog.infoBox("...who funded the construction of this city.")

    

def render():
    """Main rendering super function."""
    screen.fill([0,0,0])

    map.blit(map.current)

    image.blit(player.picture, 300,300,50,50)

        
        

    if (debug):
        for i in range(0,13):
            pygame.draw.line(screen,[200,200,200],[i*50, 0],[i*50, 650])
            pygame.draw.line(screen,[200,200,200],[0,i*50],[650,i*50])
        pygame.draw.line(screen, [255,255,0],[0-player.x+300,0-player.y+300],[0-player.x+300+(map.current.getBounds()[0]*50),0-player.y+300],3)
        pygame.draw.line(screen, [255,255,0],[0-player.x+300,0-player.y+300+(map.current.getBounds()[1]*50)],[0-player.x+300+(map.current.getBounds()[0]*50),0-player.y+300+(map.current.getBounds()[1]*50)],3)

        pygame.draw.line(screen, [255,255,0],[0-player.x+300,0-player.y+300],[0-player.x+300,0-player.y+300+(map.current.getBounds()[1]*50)],3)
        pygame.draw.line(screen, [255,255,0],[0-player.x+300+(map.current.getBounds()[0]*50),0-player.y+300],[0-player.x+300+(map.current.getBounds()[0]*50),0-player.y+300+(map.current.getBounds()[1]*50)],3)



        
        
        screen.blit(debugfont.render("player.pos = ("+str(player.pos[0])+", "+str(player.pos[1])+")", True, [200,0,200]), [5,620])
        screen.blit(debugfont.render("player.x/y = ("+str(player.x)+", "+str(player.y)+")", True, [0,200,200]), [5,600])
        
                

            
        if (map.current == None):
            screen.blit(debugfont.render("map = "+str(map.current), True, [200,0,0]), [5,580])
        else:
            screen.blit(debugfont.render("map = "+str(map.current), True, [0,200,0]), [5,580])
        screen.blit(debugfont.render("images imported = "+str(len(image.images)), True, [200,0,0]), [5,560])
        screen.blit(debugfont.render("canMove = ("+str(player.canMoveLeft())+", "+str(player.canMoveRight())+", "+str(player.canMoveUp())+", "+str(player.canMoveDown())+")", True, [200,200,0]), [5,540])
        if (player.moving == None):
            screen.blit(debugfont.render("player.moving = "+str(player.moving), True, [200,0,0]), [5,520])
        else:
            screen.blit(debugfont.render("player.moving = "+str(player.moving), True, [0,200,0]), [5,520])
        try:
            screen.blit(debugfont.render("hover = "+str(map.hover())+" ("+str(vars(map.current.blocks[map.hover()[0]][map.hover()[1]]))[0:30]+")",True,[255,255,255]),[5,500])
        except Exception:
            screen.blit(debugfont.render("hover = "+str(map.hover())+" (None)",True,[255,255,255]),[5,500])
        if (player.select != None):
            image.blit(player.select.picture,pygame.mouse.get_pos()[0]-25,pygame.mouse.get_pos()[1]-25,50,50)
        screen.blit(debugfont.render("fps = "+str(round(clock.get_fps(),2)),True,[100,100,240]),[5,480])

        drawFPSGraph(400,450)
    
    if (console.enable):
        console.blit()
            
                    
def boxTransition(delay=500):
    render()
    for i in range(0,13):
        for j in range(0,13):
            clock.tick(FRAMERATE)
            pygame.draw.rect(screen,[0,0,0],[i*50,j*50,50,50],0)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    pygame.time.wait(delay)
    #add slide in
def wipeTransitionOut(speed=10):
    render()
    num = 0
    while (num < 650):
        clock.tick(FRAMERATE)
        num += speed
        pygame.draw.rect(screen,[0,0,0],[0,0,num,650],0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
def wipeTransitionIn(speed=10):
    num = 650
    while (num > 0):
        clock.tick(FRAMERATE)
        num -= speed
        render()
        pygame.draw.rect(screen,[0,0,0],[0,0,num,650],0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
def wipeTransition(speed=10, delay=0):
    wipeTransitionOut(speed)
    pygame.time.delay(delay)
    wipeTransitionIn(speed)






def drawFPSGraph(x, y):
    global pastFrameRates
    global FRAMERATE
    
    pygame.draw.rect(screen,[250,250,250],[x,y,200,150],0)

    for i in range(6):
        
        pygame.draw.line(screen,[220,220,220],[x,y+(i*30)],[x+200,y+(i*30)],1)
        screen.blit(debugfont.render(str(150-(i*30)),True,[255,255,255]),[x-30,y+(i*30)-7])

    num = 0
    while (num < 200):
        num += 2
        try:
            pygame.draw.line(screen,[0,0,0],[(num)+x-2,(150-pastFrameRates[num])+y],[(num)+x,(150-pastFrameRates[num+2])+y],1)
        except IndexError:
            pass
    




debug = False

running = True

mode = "logo"
menuTick = 0

FRAMERATE = 120
pastFrameRates = [0]


tanbrick = block("tanbrick", True)
graybrick = block("graybrick", True)
grass = block("grass", False)
water = block("water", True)
tandoor = block("tandoor", True, "fountain")










#town = map("town", [[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)],[copy.copy(tanbrick),block("villager",True,None,0,0,villager2),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[block("tandoor", True, "fountain", 1, 2),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),block("tandoor", True, "shop", 1, 1)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)]])
#fountain = map("fountain", [[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),block("tandoor", True, "town",3,1)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),block("treasure", True, None, 0, 0, treasure1),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),block("villager", True, None, 0, 0, villager1),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)]])

#shop = map("shop",[[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)],[block("tandoor", True, "town", 3, 4),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick)],[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick)],[None,None,copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None,None,None,None,None],[None,None,copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None,None,None,None,None],[None,None,copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None,None,None,None,None],[None,None,copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None,None,None,None,None],[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),copy.copy(grass),block("villager",True,None,0,0,villager3),copy.copy(grass),copy.copy(tanbrick),None,None],[copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),copy.copy(tanbrick),None,None]])















map.current = map.get("town")

menuColors = [False,False,False,False,False]
menuKey = {False:[0,0,0],True:[200,0,0]}




clock = pygame.time.Clock()



while running:
    
    #menu here
    while mode == "logo":
        screen.fill([0,0,0])
        image.blit("randint",50,150,550,300)
        pygame.display.flip()
        menuTick += 1
        
        if (menuTick > 300):
            mode = "menu"
            menuTick = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    while mode == "menu":
        screen.fill([0,0,0])
        for i in range(0,14):
            for j in range(0,14):
                image.blit("tanbrick",(i*50-50)+menuTick,(j*50-50)+menuTick,50,50)
        image.blit("midevil",125,50,400,100)


        screen.blit(textfont.render("Continue",True,menuKey[menuColors[0]]),[250,250])
        screen.blit(textfont.render("New Game",True,menuKey[menuColors[1]]),[230,300])
        screen.blit(textfont.render("News",True,menuKey[menuColors[2]]),[260,350])
        screen.blit(textfont.render("Option",True,menuKey[menuColors[3]]),[255,400])
        screen.blit(textfont.render("Quit",True,menuKey[menuColors[4]]),[270,450])

        menuColors = [False,False,False,False,False]
        if (collides(250,250,150,50)):
            menuColors[0] = True
        if (collides(230,300,200,50)):
            menuColors[1] = True
        if (collides(260,350,75,50)):
            menuColors[2] = True
        if (collides(255,400,75,50)):
            menuColors[3] = True
        if (collides(270,450,65,50)):
            menuColors[4] = True

        screen.blit(tinyFont.render("Midevil version "+str(VERSION),True,[0,0,0]),[10,630])
        menuTick += 1
        if (menuTick >=49):
            menuTick = 0
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (collides(250,250,150,50)):
                    pass
                if (collides(230,300,200,50)):
                    mode = "game"
                if (collides(260,350,75,50)):
                    pass
                if (collides(255,400,75,50)):
                    pass
                if (collides(270,450,65,50)):
                    exit()



    while mode == "game":


        clock.tick(FRAMERATE)
        pastFrameRates.append(clock.get_fps())
        if (len(pastFrameRates)>210):
            pastFrameRates.pop(0)
        
        if (map.current != None):
            player.update()


        keys = pygame.key.get_pressed()
        if (not console.enable):
            if keys[pygame.K_LEFT]:
                player.moveLeft()
            if keys[pygame.K_RIGHT]:
                player.moveRight()
            if keys[pygame.K_UP]:
                player.moveUp()
            if keys[pygame.K_DOWN]:
                player.moveDown()



        render()
        
        
        
        pygame.display.flip()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (player.select != None and player.moving == None and map.hover() != None and debug and event.button == 1):
                    try:
                        
                        map.current.blocks[map.hover()[0]][map.hover()[1]] = player.select
                    except IndexError as e:
                        #console.add("Index error.")
                        pass
                if (debug and map.hover() != None and event.button == 3 and player.moving == None):
                    map.current.blocks[map.hover()[0]][map.hover()[1]] = None
                    #print("check")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKQUOTE:
                    console.enable = not console.enable
                if event.key == pygame.K_F1:
                    debug = not debug

                if event.key == pygame.K_e and not console.enable:
                    dialog.inventory()
                 
                if (console.enable):
                    if event.key == pygame.K_a:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "A"
                        else:
                            console.typing += "a"
                    if event.key == pygame.K_b:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "B"
                        else:
                            console.typing += "b"
                    if event.key == pygame.K_c:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "C"
                        else:
                            console.typing += "c"
                    if event.key == pygame.K_d:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "D"
                        else:
                            console.typing += "d"
                    if event.key == pygame.K_e:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "E"
                        else:
                            console.typing += "e"
                    if event.key == pygame.K_f:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "F"
                        else:
                            console.typing += "f"
                    if event.key == pygame.K_g:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "G"
                        else:
                            console.typing += "g"
                    if event.key == pygame.K_h:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "H"
                        else:
                            console.typing += "h"
                    if event.key == pygame.K_i:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "I"
                        else:
                            console.typing += "i"
                    if event.key == pygame.K_j:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "J"
                        else:
                            console.typing += "j"
                    if event.key == pygame.K_k:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "K"
                        else:
                            console.typing += "k"
                    if event.key == pygame.K_l:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "L"
                        else:
                            console.typing += "l"
                    if event.key == pygame.K_m:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "M"
                        else:
                            console.typing += "m"
                    if event.key == pygame.K_n:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "N"
                        else:
                            console.typing += "n"
                    if event.key == pygame.K_o:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "O"
                        else:
                            console.typing += "o"
                    if event.key == pygame.K_p:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "P"
                        else:
                            console.typing += "p"
                    if event.key == pygame.K_q:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "Q"
                        else:
                            console.typing += "q"
                    if event.key == pygame.K_r:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "R"
                        else:
                            console.typing += "r"
                    if event.key == pygame.K_s:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "S"
                        else:
                            console.typing += "s"
                    if event.key == pygame.K_t:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "T"
                        else:
                            console.typing += "t"
                    if event.key == pygame.K_u:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "U"
                        else:
                            console.typing += "u"
                    if event.key == pygame.K_v:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "V"
                        else:
                            console.typing += "v"
                    if event.key == pygame.K_w:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "W"
                        else:
                            console.typing += "w"
                    if event.key == pygame.K_x:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "X"
                        else:
                            console.typing += "x"
                    if event.key == pygame.K_y:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "Y"
                        else:
                            console.typing += "y"
                    if event.key == pygame.K_z:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "Z"
                        else:
                            console.typing += "z"

                    if event.key == pygame.K_1:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "!"
                        else:
                            console.typing += "1"
                    if event.key == pygame.K_2:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "@"
                        else:
                            console.typing += "2"
                    if event.key == pygame.K_3:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "#"
                        else:
                            console.typing += "3"
                    if event.key == pygame.K_4:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "$"
                        else:
                            console.typing += "4"
                    if event.key == pygame.K_5:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "%"
                        else:
                            console.typing += "5"
                    if event.key == pygame.K_6:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "^"
                        else:
                            console.typing += "6"
                    if event.key == pygame.K_7:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "&"
                        else:
                            console.typing += "7"
                    if event.key == pygame.K_8:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "*"
                        else:
                            console.typing += "8"
                    if event.key == pygame.K_9:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "("
                        else:
                            console.typing += "9"
                    if event.key == pygame.K_0:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += ")"
                        else:
                            console.typing += "0"
                    if event.key == pygame.K_SPACE:
                        console.typing += " "
                    if event.key == pygame.K_QUOTE:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "\""
                        else:
                            console.typing += "'"
                    if event.key == pygame.K_EQUALS:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "+"
                        else:
                            console.typing += "="
                    if event.key == pygame.K_BACKSPACE:
                        console.typing = console.typing[0:-1]
                    if event.key == pygame.K_SEMICOLON:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += ":"
                        else:
                            console.typing += ";"
                    if event.key == pygame.K_COMMA:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "<"
                        else:
                            console.typing += ","
                    if event.key == pygame.K_PERIOD:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += ">"
                        else:
                            console.typing += "."
                    if event.key == pygame.K_SLASH:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "?"
                        else:
                            console.typing += "/"
                    if event.key == pygame.K_LEFTBRACKET:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "{"
                        else:
                            console.typing += "["
                    if event.key == pygame.K_RIGHTBRACKET:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "}"
                        else:
                            console.typing += "]"
                    if event.key == pygame.K_BACKSLASH:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "|"
                        else:
                            console.typing += "\\"
                    if event.key == pygame.K_MINUS:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            console.typing += "_"
                        else:
                            console.typing += "-"
                    if event.key == pygame.K_UP:
                        if (len(console.log) > 0):
                            console.typing = console.log[0]
                    if event.key == pygame.K_RETURN:
                        #execute command
                        console.command(console.typing)
                        console.typing = ""

    
        
        
        














