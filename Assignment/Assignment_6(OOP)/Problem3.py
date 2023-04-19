class Arithmetic:

    def __init__(self,A):
        self.Value =A

    def Factor(self):
        Factors = list()
        for i in range(1,int((self.Value/2))+1):
            if(self.Value%i ==0):
                Factors.append(i)
        return Factors

    def SumFactor(self):
        Sum =0
        Fact = self.Factor()
        for no in Fact:
            Sum = Sum+no
        return Sum

    def ChkPrime(self):
        Flag =False
        Fact = self.Factor()
        if(len(Fact)==1):
            Flag =True
        return Flag
        
    def ChkPerfect(self):
        Flag =False
        Sum = self.SumFactor()

        if (self.Value == Sum):
            Flag =True 

        return Flag

def main():

    obj1 = Arithmetic(7)
    Ret1 = obj1.Factor()
    print("Factor :",Ret1)
    Ret2 = obj1.SumFactor()
    print("Sum of Factor :",Ret2)
    Ret3 = obj1.ChkPrime()
    if(Ret3 == True):
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")

    Ret4 = obj1.ChkPerfect()
    if(Ret4 == True):
        print("Number is Perfect Number")
    else:
        print("Number is not Perfect Number")      
    print("---------------------------------------------")
    obj2 = Arithmetic(6)
    Ret5 = obj2.Factor()
    print("Factor :",Ret5)
    Ret6 = obj2.SumFactor()
    print("Sum of Factor :",Ret6)
    Ret7 = obj2.ChkPrime()
    if(Ret7 == True):
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")

    Ret8 = obj2.ChkPerfect()
    if(Ret8 == True):
        print("Number is Perfect Number")
    else:
        print("Number is not Perfect Number")       

    print("---------------------------------------------")

    obj3 = Arithmetic(10)
    Ret9 = obj3.Factor()
    print("Factor :",Ret9)
    Ret10 = obj2.SumFactor()
    print("Sum of Factor :",Ret10)
    Ret11 = obj2.ChkPrime()
    if(Ret11 == True):
        print("Number is Prime Number")
    else:
        print("Number is not Prime Number")

    Ret12 = obj3.ChkPerfect()
    if(Ret12 == True):
        print("Number is Perfect Number")
    else:
        print("Number is not Perfect Number")       
    


if __name__=="__main__":
    main()
