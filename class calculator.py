class calculator:
    def __init__ (self, x,y):
        self.x=x
        self.y=y

    def add(self,z):
        return self.x+self.y+z
    def multiply(self,z):
        return(self.x+self.y)*z
add=calculator(20,10)
print(add.add(30))
print(add.multiply(40))




