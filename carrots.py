

import math

x2=cos(angle)*x1 − sin(angle)* y1

y2=sinanglex1+cosangley1


myCat = Cat()

myCat.move(10)
myCat.turn(45)

def turn_by_angle(v2, angle):
    """
    Rotate a 2d vector about the origin by an angle.
    Args:
        v2: List of 2 Floats: The vector to be rotated
        angle: Float: Amount to rotate 'v2' in degrees
    Returns:
        List of 2 Floats: The rotated vector.
    """
    rotation = math.radians(angle)
    x1 = round(math.cos(rotation) * angle[0] + math.sin(rotation) * angle[1])
    y1 = round(math.cos(rotation) * angle[1] - math.sin(rotation) * angle[0])
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

class Cat (object):
    def __init__(color='red', position=[8,8]):
        self.position = position
        self.color = color
        self.direction_vector = [0,1]
        self.speed = 1
        self.speedIncrement = 1

    def move(steps=1):
        for i in range(steps):
            #turn off dot
            self.position = addV2(self.position, self.direction_vector)
            #add direction vector to pos
            #show dot
            self.stepTime

    def wait(waitTime):
        time.sleep(waitTime)

    def stepTime()
        time.sleep(self.speedToWaitTime)

    @property
    def speedToWaitTime():
        """
        The higher the waitTime, the shorter the wait.
        """
        duration = self.speedIncrement/self.speed
        time.sleep(duration)

    def turn(direction):
        """
        Rotate the dicrection_vector.
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
                raise:
                    Exception ("Specify 'right' or 'left' or give degrees.")
        elif isinstance(direction_vector, float) or isinstance(direction_vector, int):
            angle = float(direction)

        self.direction_vector = turn_by_angle(self.direction_vector, angle)








