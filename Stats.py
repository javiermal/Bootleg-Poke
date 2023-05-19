import math
import random


def displaySTATS(soma):
        print("ATK_EV = " + str(soma.ev_atk) + "  DEFS_EV = " + str(soma.ev_defs) + "  SPD_EV = " + str(soma.ev_spd))
        print("ATK_IV = " + str(soma.iv_atk) + "  DEFS_IV = " + str(soma.iv_defs) + "  SPD_IV = " + str(soma.iv_spd))
        print("ATK = " + str(soma.atk))
        print("DEFS = " + str(soma.defs))
        print("SPD = " + str(soma.spd)) 

def calculateSTATS(base_atk, iv_atk, ev_atk, level):
    '''
    does this work?
    '''
    return math.floor((((math.floor(((2*base_atk)+iv_atk+math.floor(ev_atk/4))*level))/100)+5)*1)

#Fucking sub class, Basestats are in a level down

class Pikomon(object):
    def __init__(self, level):
        self.level = level
        self.iv_atk = random.randint(0,31)
        self.iv_defs = random.randint(0,31)
        self.iv_spd = random.randint(0,31)
        self.ev_atk = 0
        self.ev_defs = 0
        self.ev_spd = 0
        self.atk = calculateSTATS(self.base_atk,self.iv_atk,self.ev_atk,self.level)
        self.defs = calculateSTATS(self.base_def,self.iv_defs,self.ev_defs,self.level)
        self.spd = calculateSTATS(self.base_spd,self.iv_spd,self.ev_spd,self.level)
    
    def incAtkEv(self, num):
        if (self.ev_atk + num) <= 255:
            self.ev_atk += num
        else:
            self.ev_atk = 255
        self.atk = calculateSTATS(self.base_atk,self.iv_atk,self.ev_atk,self.level)
            

    def incDefEv(self, num):
        self.ev_defs += num
        self.defs = math.floor((((math.floor(((2*self.base_def)+self.iv_defs+math.floor(self.ev_defs/4))*self.level))/100)+5)*1)

    def incSpdEv(self, num):
        self.ev_spd += num
        self.defs = math.floor((((math.floor(((2*self.base_def)+self.iv_defs+math.floor(self.ev_defs/4))*self.level))/100)+5)*1)


class Pitochu(Pikomon):
    base_hp = 35
    base_atk = 55
    base_def = 40
    base_spd = 90
    def __init__(self, level, nature):
        super(Pitochu, self).__init__(level)
        self.type = type



piko = Pitochu(50,"Adamant")
PPMD =True
while(PPMD):
    displaySTATS(piko)
    y = int(input("You defeated a Pikomon, how much EV did you get? "))
    piko.incAtkEv(y)
    displaySTATS(piko)

    x = int(input("Wanna continue? (1/0)"))
    if x == 0:
        PPMD = False