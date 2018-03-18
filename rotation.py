



import math
rotation = math.radians(180.0)

x = 1
y = 0

x1 = round((math.cos(rotation) * x) + (math.sin(rotation) * y) )



y1 = round((math.cos(rotation) * y) - (math.sin(rotation) * x))

print [x1,y1]

