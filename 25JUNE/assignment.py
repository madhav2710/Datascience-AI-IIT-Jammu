import math
# import 
class math1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def GM(self):# Geometric Mean
        return (self.a * self.b)/ (self.a + self.b)
    def HM(self):# Harmonic Mean
        return 2 * (self.a * self.b) / (self.a + self.b)
    def AM(self):# Arithmetic Mean
        return (self.a + self.b) / 2
    def AreaofRectangle(self):
        return self.a * self.b
    def PerimeterofRectangle(self):
        return 2 * (self.a + self.b)
    def CC(self):#2 Cosine Rule
        return 2*math.cos((self.a + self.b) / 2) * math.sin((self.a - self.b) / 2)
    def rt(self):# Right Triangle
        return math.sqrt(self.a**2 + self.b**2)
    def AreaofTriangle(self):
        return (self.a * self.b) / 2
    def AeraofconcentricCircle(self):
        return math.pi * (self.a + self.b) / 2
    def Aerawithdaigonal(self):
        return (self.a * self.b) / 2
    
m1= math1(3, 4)
print("Geometric Mean:", m1.GM())
print("Harmonic Mean:", m1.HM())
print("Arithmetic Mean:", m1.AM())
print("Area of Rectangle:", m1.AreaofRectangle())
print("Perimeter of Rectangle:", m1.PerimeterofRectangle())
print("Cosine Rule:", m1.CC())
print("Right Triangle:", m1.rt())
print("Area of Triangle:", m1.AreaofTriangle())
print("Area of Concentric Circle:", m1.AeraofconcentricCircle())
print("Area with Diagonal:", m1.Aerawithdaigonal())    