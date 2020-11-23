class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return "(" + str(self.x) +"," + str(self.y) + "," + str(self.z) + ")"


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


    def __mul__(self, other):
        return Vector(self.x*other.x, self.y*other.y, self.z*other.z)


    def __truediv__(self, other):
        return Vector(self.x/other.x, self.y/other.y, self.z/other.z)


    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**(1/2)


#ploschad
    def area(self, other):
        return (((self.x**2 + self.y**2)*(other.x**2 + other.y**2)(1 - (self.x*other.x + self.y*other.y))**(1/2))/((self.x**2 + self.y**2)**(1/2))*(other.x**2 + self.y**2)**(1/2))


    #obiom
    def volume(u, v, w):
        return abs(u.x*(v.y*w.z - v.z*w.y) - u.y*(v.x*w.z - w.x*v.z) + u.z*(v.x*w.y - v.y*w.z))


    #tsentr mass
    def centrmass(u, v, w):
        return Vector((u.x + v.x + w.x)/3, (u.y + v.y + w.y)/3, (u.z + v.z + w.z)/3)


    #naibolee udalennaya tochka ot nachala koordinat
    n = int(input())
    mas = []
    while n != 0:
        x1, y1, z1 = (map(int, input().split()))
        u = Vector(x1, y1, z1)
        v = u*u
        i = (v.x + v.y + v.z)**(1/2)
        mas.append(i)
        if i == max(mas):
            s = u
        n -= 1
    print(s.x, s.y, s.z)


a = Vector(4, 2, 6)
b = Vector(1, 3, 5)
c = Vector(5, 6, 7)

    p = area(a,b)
    print(p)
    print(volume(a, b, c))
    print(centrmass(a, b, c))