
class Circle:

    PI =3.14

    def __init__(self):
        Radius = 0
        Area = 0
        Circumference = 0

    def Accept(self):
        self.Radius = int(input("Enter Redius \n"))
        
    def CalculateArea(self):
        self.Area = self.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2*self.PI*self.Radius

    def Display(self):
        print("Radius of Circle :",self.Radius)
        print("Area of Circle :",self.Area)
        print("Circumference of Circle :",self.Circumference)

def main():

    obj = Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()


if __name__=="__main__":
    main()