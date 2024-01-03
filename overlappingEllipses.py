from prng import WarAndPeacePseudoRandomNumberGenerator

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getXvalue(self):
        '''
        returns x coordinate
        '''
        return self.x                                                                # x-coordinate
    
    def getYvalue(self):
        '''
        returns y coordinate
        '''
        return self.y                                                                # y-coordinate
    
    def getDistance(self, point):
        '''
        returns the distance between the points 
        '''
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5            # calculating the euclidean distance between the points
    
    def __repr__(self):
        '''
        returns a string representaion of the point object
        '''
        return f"Point({self.x}, {self.y})"

class Ellipse:

    def __init__(self, fPoint1, fpoint2, width):
        self.p1 = fPoint1
        self.p2 = fpoint2
        self.width = width

    def getWidth(self):
        '''
        returns the width of the ellipse
        '''
        return self.width

    def getMinxAxis(self):
        '''
        returns the minimum x value
        '''
        return min(self.p1.getXvalue(), self.p2.getXvalue())                             # calculating minimum value of x-coordinates of focal points
    
    def getMaxxAxis(self):
        '''
        returns the maximum x value
        '''
        return max(self.p1.getXvalue(), self.p2.getXvalue())                             # calculating maximum value of x-coordinates of focal points 

    def getMinyAxis(self):
        '''
        returns the minimum y value
        '''
        return min(self.p1.getYvalue(), self.p2.getYvalue())                             # calculating minimum value of y-coordinates of focal points 
    
    def getMaxyAxis(self):
        '''
        returns the maximum y value
        '''
        return max(self.p1.getYvalue(), self.p2.getYvalue())                             # calculating maximum value of y-coordinates of focal poitns 
    
    def isPointinside(self, point):
        '''
        returns true when the point is inside the ellipse
        '''
        return self.p1.getDistance(point) + self.p2.getDistance(point) < self.width      # condition to check if the point is inside the ellipse

def main(ellipse1, ellipse2):
    '''
    calculates the overlap between the two ellipses  
    '''

    leftXpoint = min(ellipse1.getMinxAxis(), ellipse2.getMinxAxis()) - max(ellipse1.getWidth(), ellipse2.getWidth())     # calculating the points for rectangle
    rightXpoint = max(ellipse1.getMaxxAxis(), ellipse2.getMaxxAxis()) + max(ellipse1.getWidth(), ellipse2.getWidth())
    bottomYpoint = min(ellipse1.getMinyAxis(), ellipse2.getMinyAxis()) - max(ellipse1.getWidth(), ellipse2.getWidth())
    topYpoint = max(ellipse1.getMaxyAxis(), ellipse2.getMaxyAxis()) + max(ellipse1.getWidth(), ellipse2.getWidth())

    prng = WarAndPeacePseudoRandomNumberGenerator(1000)                                  # intializing a pseudo random generator with a seed value of 1000
    
    totalAreasize = (topYpoint - bottomYpoint) * (rightXpoint - leftXpoint)              # calculating the area of the rectangle
    randomPointcount = 10000                                                             
    targetPointCount = 0

    for i in range(randomPointcount):                                                    # generating random points in the rectangle
        x = prng.customRandom(leftXpoint, rightXpoint)
        y = prng.customRandom(bottomYpoint, topYpoint)
        rPoint = Point(x,y)
        if ellipse1.isPointinside(rPoint) and ellipse2.isPointinside(rPoint):            # checking if the point is inside the ellipses
            targetPointCount += 1                                                        # if the point is in both the ellipses then keeping track of it

    overlap = targetPointCount/randomPointcount * totalAreasize                          # calculating the overlap area

    return overlap     


# Example 1: two circles at the origin with radius 2
e1 = Ellipse(Point(0,0), Point(0,0), 2)       
e2 = Ellipse(Point(0,0), Point(0,0), 2)       
overlap1 = main(e1,e2)
print(overlap1)

# Example 2
e3 = Ellipse(Point(6,6), Point(1,8), 9)
e4 = Ellipse(Point(7,3), Point(9,4), 9)
overlap2 = main(e3, e4)
print(overlap2)
