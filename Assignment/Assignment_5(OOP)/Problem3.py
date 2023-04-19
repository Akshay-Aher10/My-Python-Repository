class Arithmetic:

    def __init__(self):
        Value1 =0
        Value2 = 0
        Value3 = 0

    def Accept(self):
        self.Value1 = int(input("Enter First Number\n"))
        self.Value2 = int(input("Enter Second Number\n"))

    def Addition(self):
        Result = self.Value1+self.Value2
        return Result

    def Substraction(self):
        Result = self.Value1-self.Value2
        return Result

    def Multiplication(self):
        Result = self.Value1*self.Value2
        return Result

    def Division(self):
        Result = self.Value1/self.Value2
        return Result


def main():

    obj =Arithmetic()

    obj.Accept()
    
    Ans1 = obj.Addition()
    print("Addition is :",Ans1)
    
    Ans2 = obj.Substraction()
    print("Substraction is :",Ans2)
    
    Ans3 = obj.Multiplication()
    print("Multiplication is :",Ans3)

    Ans4 = obj.Division()
    print("Division is :",Ans4)


if __name__=="__main__":
    main()        