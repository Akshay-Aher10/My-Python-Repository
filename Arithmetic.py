

def Addition(Value1, Value2):
    Ans = Value1+Value2
    return Ans

def Substraction(Value1, Value2):
    Ans = Value1-Value2
    return Ans

def Division(Value1, Value2):
    Ans = Value1/Value2
    return Ans

def MultiPlication(Value1, Value2):
    Ans = Value1*Value2
    return Ans

def Display1(Value1):
    print(" Problem : Accept one number from user if number is less that 10 then print Hello otherwise print Demo")
    i=0
    while i < Value1:
        if Value1>10:
            print("Demo")
        else:
            print("Hello")    

        i +=1

def Display2(Value1,Value2):
    print("Problem :Accept two number from user and display first number in second number of time.")
    i=0
    while i < Value2:
            print(Value1)

            i +=1

def CheckEven(Value1):

    if (Value1 % 2) == 0:
        return True
    else:
        return False

    
def EvenNo(Value1):
    print("Problem :accept no from user and print event factors of that number.")

    iCnt = Value1
    while iCnt >= 1:
        if  (Value1 % iCnt == 0) and (iCnt % 2  == 0) :
            print(iCnt,"\t")
        
        iCnt -= 1

def FactorMultiplication(Value1):
    print("Problem :Accept numbers from user and display multiplication of its factor.")

    iCnt = 1
    iSum =1

    while iCnt <= Value1:
        if  (Value1 % iCnt == 0):
            iSum =iSum*iCnt

        iCnt += 1

    return iSum

def FactorDifference(Value1):
    print("Problem :Accept number from user and Display Differnece between Summation of all its non factor and factor.")

    Cnt = 1
    Difference =1
    Factor =0
    NonFactor =0

    while Cnt <= Value1:
        if  (Value1 % Cnt == 0):
            Factor=Factor+Cnt
        else:
            NonFactor=NonFactor+Cnt
        Cnt += 1

    Difference =  Factor-NonFactor

    if Difference<0:
        Difference = -Difference

    return Difference    
