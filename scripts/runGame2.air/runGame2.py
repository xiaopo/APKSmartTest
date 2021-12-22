# -*- encoding=utf8 -*-
__author__ = "Administrator"
import random
import string
from airtest.core.api import *

auto_setup(__file__)

mainTaskPos = None
ran_str = None
step = 0

def ifTouch(param):
    pos = exists(param)
    if pos:
        try:
            touch(pos)
        except Exception:
            print ("Error")

def randomName():

    global ran_str
    global step
    if not ran_str:
        pos = exists(Template(r"tpl1586529665597.png", record_pos=(0.115, -0.018), resolution=(1920, 1080)))
        if pos:
            touch(pos)
            
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
            print(ran_str)
            
            text(ran_str)
            
            ifTouch(Template(r"tpl1586529726633.png", record_pos=(0.415, 0.206), resolution=(1920, 1080)))
            
            step = 1
            
    
def enterGame():
    global step
    ifTouch(Template(r"tpl1586508880483.png", record_pos=(0.008, 0.082), resolution=(1920.0, 1080.0)))
    
    ifTouch(Template(r"tpl1586508886767.png", record_pos=(-0.001, 0.194), resolution=(1920.0, 1080.0)))
    
    
    pos1 = exists(Template(r"tpl1586510001066.png", record_pos=(0.368, 0.201), resolution=(1920, 1080)))
    if pos1:
        try:
            touch(pos1)
            step = 2
        except Exception:
            print ("Error")
    
    
    
    pos2 = exists(Template(r"tpl1586509389777.png", record_pos=(0.371, 0.23), resolution=(1920, 1080)))
    if pos2:
        try:
            touch(pos2)
            
            ifTouch(Template(r"tpl1586842055737.png", record_pos=(0.462, 0.176), resolution=(1920, 1080)))
            ifTouch(Template(r"tpl1586509389777.png", record_pos=(0.371, 0.23), resolution=(1920, 1080)))
            step = 2
        except Exception:
            print ("Error")


def enterTest():
    global step
    pos = exists(Template(r"tpl1587544773904.png", record_pos=(-0.114, 0.182), resolution=(2340, 1080)))
    if pos:
        try:
            touch(pos)
            
            
            if exists(Template(r"tpl1587548730275.png", record_pos=(0.444, -0.094), resolution=(2340, 1080))):
                touch(Template(r"tpl1587548763529.png", record_pos=(0.443, -0.162), resolution=(2340, 1080)))

            
            ifTouch(Template(r"tpl1587541605126.png", record_pos=(0.195, 0.208), resolution=(2244, 1080)))

            text("cd/test")

            ifTouch(Template(r"tpl1587543475838.png", record_pos=(0.383, 0.173), resolution=(2340, 1080)))
            pos = exists(Template(r"tpl1587543494997.png", record_pos=(0.429, 0.196), resolution=(2340, 1080)))
            if pos:
                try:
                    touch(pos)
                    step = 3
                except Exception:
                    print ("Error")

        except Exception:
            print ("Error")


def testUI():
    global step
    pos = exists(Template(r"tpl1587544975514.png", record_pos=(-0.271, -0.168), resolution=(2340, 1080)))
    if pos:
        try:
            touch(pos)
            
            text("1")
            
            ifTouch(Template(r"tpl1587543475838.png", record_pos=(0.383, 0.173), resolution=(2340, 1080)))
            
            pos1 = exists(Template(r"tpl1587544374304.png", record_pos=(-0.192, -0.167), resolution=(2340, 1080)))
            
            if pos1:
                
                touch(pos1)
                
                text("700")
                
                ifTouch(Template(r"tpl1587543475838.png", record_pos=(0.383, 0.173), resolution=(2340, 1080)))
                
                ifTouch(Template(r"tpl1587545091526.png", record_pos=(0.082, -0.172), resolution=(2340, 1080)))
                
                sleep(10)
                
                step = 4
                
                #
                #text(13090)
                
        except Exception:
            print ("Error")  

            
def testTask():
    global step
    pos = exists(Template(r"tpl1587544975514.png", record_pos=(-0.271, -0.168), resolution=(2340, 1080)))
    if pos:
        try:
            touch(pos)
            
            text("15")
            
            ifTouch(Template(r"tpl1587543475838.png", record_pos=(0.383, 0.173), resolution=(2340, 1080)))
            
            pos1 = exists(Template(r"tpl1587544374304.png", record_pos=(-0.192, -0.167), resolution=(2340, 1080)))
            
            if pos1:
                
                touch(pos1)
                
                text("13090")
                
                ifTouch(Template(r"tpl1587543475838.png", record_pos=(0.383, 0.173), resolution=(2340, 1080)))
                
                ifTouch(Template(r"tpl1587545091526.png", record_pos=(0.082, -0.172), resolution=(2340, 1080)))
                
                sleep(60)

                
                step = 4
                #
                #text(13090)
                
        except Exception:
            print ("Error")  
    
    
def Copy11():
    global step
    
    ifTouch(Template(r"tpl1587548547800.png", record_pos=(0.471, -0.165), resolution=(2340, 1080)))
    ifTouch(Template(r"tpl1587545908499.png", record_pos=(0.343, 0.188), resolution=(2340, 1080)))
    
    if exists(Template(r"tpl1587546315670.png", record_pos=(-0.253, 0.139), resolution=(2340, 1080))):
        step = 5

        
        
def Copy12():
    global step
    ifTouch(Template(r"tpl1587546392463.png", record_pos=(-0.132, -0.146), resolution=(2340, 1080)))
    
    ifTouch(Template(r"tpl1587546414321.png", record_pos=(-0.22, 0.046), resolution=(2340, 1080)))
    
    ifTouch(Template(r"tpl1587546439110.png", record_pos=(0.28, 0.159), resolution=(2340, 1080)))
    
    if exists(Template(r"tpl1587546521068.png", record_pos=(-0.22, -0.005), resolution=(2340, 1080))):
        
        step = 6
    
    
def Copy13():
    ifTouch(Template(r"tpl1587548547800.png", record_pos=(0.471, -0.165), resolution=(2340, 1080)))
    ifTouch(Template(r"tpl1587546682002.png", record_pos=(-0.032, -0.146), resolution=(2340, 1080)))

    ifTouch(Template(r"tpl1587546728156.png", record_pos=(0.348, 0.185), resolution=(2340, 1080)))
    
    if exists(Template(r"tpl1587547002495.png", record_pos=(-0.219, -0.014), resolution=(2340, 1080))):
        
         step = 7
    
def Copy14():    
    
    ifTouch(Template(r"tpl1587547094815.png", record_pos=(0.069, -0.147), resolution=(2340, 1080)))
    
    ifTouch(Template(r"tpl1587547118245.png", record_pos=(0.347, 0.191), resolution=(2340, 1080)))
    if exists(Template(r"tpl1587547002495.png", record_pos=(-0.219, -0.014), resolution=(2340, 1080))):
        
         step = 8
    
    
def Copy21():
    ifTouch(Template(r"tpl1587547326166.png", record_pos=(-0.424, -0.066), resolution=(2340, 1080)))
    
    ifTouch(Template(r"tpl1587547388482.png", record_pos=(0.337, 0.183), resolution=(2340, 1080)))
    
    ifTouch(Template(r"tpl1587547417938.png", record_pos=(0.291, 0.164), resolution=(2340, 1080)))

    ifTouch(Template(r"tpl1587547433126.png", record_pos=(0.179, 0.16), resolution=(2340, 1080)))
    
#     if exists(Template(r"tpl1587547002495.png", record_pos=(-0.219, -0.014), resolution=(2340, 1080))):
        
        
    
while True:
    if step == 0:
        randomName()
    elif step == 1:
        enterGame()
    elif step == 2:
        enterTest()
    elif step == 3:
        testTask()
    elif step == 4:
        Copy11()
    elif step == 5:
        Copy12()
    elif step == 6:
        Copy13()
    elif step == 7:
        Copy14()
    elif step == 8:
        Copy21()

    ifTouch(Template(r"tpl1587548803465.png", record_pos=(0.261, -0.118), resolution=(2340, 1080)))


