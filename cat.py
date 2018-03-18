

import math
import unicornhathd as unicorn
import time, colorsys
import numpy

        

def turn_by_angle(v2, angle):
    """
    Rotate a 2d vector about the origin by an angle.
    Args:
        v2: List of 2 Floats: The vector to be rotated
        angle: Float: Amount to rotate 'v2' in degrees
    Returns:
        List of 2 Floats: The rotated vector.
    """
    angle= float(angle)
    rotation = math.radians(angle)
    x1 = math.cos(rotation) * v2[0] + math.sin(rotation) * v2[1]
    y1 = math.cos(rotation) * v2[1] - math.sin(rotation) * v2[0]
    return [x1,y1]

def addV2(v2A, v2B):
    """
    Add vector A to B and return sum.
    Args:
        v2A: List of 2 floats
        v2B: List of 2 floats
    Returns:
        List of 2 floats
    """
    sumV2 = [0,0]
    sumV2[0] = v2A[0] + v2B[0]
    sumV2[1] = v2A[1] + v2B[1]
    return sumV2



class Color(object):
    def __init__(self):
        self.color = 'red'
        self.colors = {'red':[255,0,0],'green':[0,255,0],'blue':[0,0,255], 'black':[0,0,0]}
        self.black = self.colors['black']

    @property
    def rgb(self):
        return self.colors[self.color]


class Unicorn(object):
    def __init__(self):
        unicorn.brightness(1)
        unicorn.rotation(180)
        self.xDim = 16
        self.yDim = 16
        self.xMax = self.xDim -1
        self.xMin = 0
        self.yMax = self.yDim -1
        self.yMin = 0
        self.debugMe = False
        
    def show(self):
        unicorn.show()
        
    def set_pixel(self, v2coord, v3color):
        unicorn.set_pixel(v2coord[0], v2coord[1], v3color[0], v3color[1], v3color[2])
        

class Cat (Unicorn):
    def __init__(self, color='red', position=[7.0,7.0]):
        Unicorn.__init__(self)
        print self.yDim
        self.position = position
        self.color = Color()
        self.direction_vector = [0.0,1.0]
        self.speedAttr = 5
        self.speedIncrement = 1
        self.setPosition(self.position)

    def move(self,steps=1):
        for i in range(steps):
            
            #add direction vector to pos
            new_position = addV2(self.position, self.direction_vector)

            #turn off dot, change position, then show it.
            self.setPosition(new_position)
            
            #time delay between moves
            self.stepWait()

    def start(self, x, y):
        self.setPosition([float(x),float(y)])

    def setPosition(self, v2):
        """
        Turn off current position, change
        unicorn coordinate, and then display.
        """
        #turn off dot
        self.clear()
        
        #set the position attr
        self.position = v2
        self.wrap()
        #turn on the pixel
        self.set_pixel(self.position, self.color.rgb)
        #show it
        self.show()
    def clear(self):
        self.set_pixel(self.position, self.color.black)

    def reset(self):
        print "Resetting."
        self.clear()
        self.__init__()
        

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    def wrap(self):
        if self.x > self.xMax:
            if self.debugMe:
                print "Wrapped coord: %s"%self.x
            self.position[0] = self.x - self.xMax
        elif self.x < self.xMin:
            if self.debugMe:
                print "Wrapped coord: %s"%self.x
            self.position[0] = self.xMax + self.x

        if self.y > self.yMax:
            self.position[1] = self.y - self.yMax
        elif self.y < self.yMin:
            self.position[1] = self.yMax + self.y
        if self.debugMe:
            print "Position is: %s"%self.position

    def wait(self, waitTime):
        time.sleep(waitTime)

    def speed(self, speedValue):
        self.speedAttr = speedValue
        

    def stepWait(self):
        if self.debugMe:
            print "wait: %s"%self.speedToWaitTime
        time.sleep(self.speedToWaitTime)

    @property
    def speedToWaitTime(self):
        """
        The higher the waitTime, the shorter the wait.
        """
        return float(self.speedIncrement)/float(self.speedAttr)

    def turn(self, direction):
        """
        Rotate the direction_vector.
        Args:
            direction: String, or Float: 'right', 'left', or degrees
        Returns:
            None (sets direction_vector)
        """
        if isinstance(direction, str):
            if direction == "right":
                angle = 90
            elif direction == "left":
                angle = -90
            else:
                raise Exception ("Specify 'right' or 'left' or give degrees.")
                    
        elif isinstance(direction, float) or isinstance(direction, int):
            angle = float(direction)

        self.direction_vector = turn_by_angle(self.direction_vector, angle)
        







