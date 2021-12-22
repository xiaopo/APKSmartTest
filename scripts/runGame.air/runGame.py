# -*- encoding=utf8 -*-
__author__ = "Administrator"
import random
import string
import time
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


def doCommon():
    ifTouch(Template(r"tpl1586517356445.png", record_pos=(0.125, 0.091), resolution=(1920, 1080)))

    ifTouch(Template(r"tpl1586518509939.png", record_pos=(-0.131, 0.092), resolution=(1920, 1080)))
    
    ifTouch(Template(r"tpl1586516023794.png", record_pos=(-0.446, -0.092), resolution=(1920, 1080)))
    
    ifTouch(Template(r"tpl1586519590806.png", record_pos=(-0.468, -0.263), resolution=(1920, 1080)))
    
            
while True:

    if step == 0:
        randomName()
    elif step == 1:
        enterGame()
    elif step == 2:
        doCommon()
        pos1 = exists(Template(r"tpl1586511779007.png", record_pos=(0.001, 0.21), resolution=(1920, 1080)))
        if pos1:
            try:
                touch(pos1)
                step = 3
            except Exception:
                print ("Error")
            
    elif step == 3:
        doCommon()
        
        pos1 = exists(Template(r"tpl1586519431433.png", record_pos=(0.431, -0.188), resolution=(1920, 1080)))
        if pos1:
            try:
                touch(pos1)
                step = 4
            except Exception:
                print ("Error")
    
    elif step == 4:
        doCommon()

        ifTouch(Template(r"tpl1586521454524.png", record_pos=(-0.423, -0.094), resolution=(1920, 1080)))

        
    time.sleep(1)

        


