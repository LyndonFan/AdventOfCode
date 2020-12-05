def sgn(x):
    return 1 if x>0 else (-1 if x<0 else 0)

class Moon:
    def __init__(self,x,y,z):
        self.pos = [x,y,z]
        self.vel = [0,0,0]
    
    def attract(self,other):    #NOTE: MUTUAL
        for i in range(3):
            s = sgn(other.pos[i] - self.pos[i])
            self.vel[i] += s
            other.vel[i] -= s
    
    def update(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
    
    def pot(self):
        return sum(abs(v) for v in self.pos)
    
    def kin(self):
        return sum(abs(v) for v in self.vel)
    
    def nrg(self):
        return self.pot() * self.kin()


"""
<x=-9, y=-1, z=-1>
<x=2, y=9, z=5>
<x=10, y=18, z=-12>
<x=-6, y=15, z=-7>
"""

moons = [
    Moon(-9,-1,-1),
    Moon(2,9,5),
    Moon(10,18,-12),
    Moon(-6,15,-7)
]

NUMSTEPS = 4686774924
for step in range(NUMSTEPS):
    for i in range(len(moons)-1):
        for j in range(i+1,len(moons)):
            moons[i].attract(moons[j])
    for m in moons:
        m.update()
    if (step%10000000==0):
        print(step)
print(sum(m.nrg() for m in moons))