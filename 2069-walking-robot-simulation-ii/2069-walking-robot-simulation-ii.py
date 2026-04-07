class Robot(object):
    
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = self.y = 0
        self.dir = 1
        self.dirName = ["North", "East", "South", "West"]
        self.dirPoints = [(0,1), (1,0), (0,-1), (-1,0)]
        self.perimeter = 2*(self.w+self.h-2)

    def step(self, num):
        if num >= self.perimeter:
            num%=self.perimeter
            if self.x==0 and self.y==0 and self.dir==1:
                self.dir = 2
        i=0
        while i<num:
            xNew = self.x + self.dirPoints[self.dir][0]
            yNew = self.y + self.dirPoints[self.dir][1]
            if 0<=xNew<self.w and 0<=yNew<self.h:
                self.x = xNew
                self.y = yNew
                i+=1
            else:
                self.dir = (self.dir + 3) % 4
            
    def getPos(self):
        return (self.x,self.y)
        
    def getDir(self):
       return self.dirName[self.dir]
        