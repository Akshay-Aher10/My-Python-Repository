#write a program which contain one class named as Demo
# Demo Class contain two instance variable as no1,no2.
#That Class contain one class variable as Value.
#There are two instance methods of class as Fun and Gun which display values of instance Variables.
# Initialise instance variable in init method by accepting the valuse from user.

#After Creating the Class create the two objects of Demo Class as
# obj1 =Demo(11,21)
# obj2 = Demo(51,101)

#Now Call the instance Methods as
#Obj1.Fun()
#Obj2.Fun()
#Obj1.Gun()
#Obj2.Gun()

class Demo:

    Value = 10

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Fun Method :")
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print("Gun Method :")
        print(self.No1)
        print(self.No2)

def main():

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__=="__main__":
    main()    