# distance formula coordinate geometry
# using the oop concept

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
 
    def __str__(self):
        return "{},{}".format(self.x_coord,self.y_coord)
    
    def euclidean_distance(self, other):
        # self.other = other
        return ((self.x_coord - other.x_coord)**2 + (self.y_coord - other.y_coord)**2)**0.5
    
    # lets create a method to calculate the distance from the origin 
    def dist_from_origin(self):
        # also can be done as 
        return ((self.x_coord)**2 + (self.y_coord)**2)**0.5
        # return self.euclidean_distance(Point(0,0))
    # yasma ek point self vayo arko point chai (0,0) vayo


class Line:
    def __init__(self, A, B, C): #the eqn of line Ax+By+C=0
        self.A =A
        self.B =B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
    # A user should able to check if a point lies on a goven line or not
    def point_on_line(line, point):
        if line.A*point.x_coord + line.B*point.y_coord + line.C == 0 :
            return "lies on the line"
        else:
            return "does not lie on the line"
 
    #  A user can find the distance between a given 2D point and a given line.
        

    def shortest_distance(line, point):
        return abs(line.A*point.x_coord + line.B*point.y_coord + line.C)/(line.A **2 + line.B**2)


# P1 = Point(3,5)  #yo one point 
# P2 = Point(10,0)  #yo other point
# # s = P1.euclidean_distance(P2)
# # print(s)
# o = P2.dist_from_origin()
# print("the distance from origin is", o)    
    

#    Line object 
l1 = Line(1,1,-2)
p1 = Point(1, 1)
dddd = l1.shortest_distance(p1)
print( dddd)


# when the point lies on the line the shortest point well be o obviously.
