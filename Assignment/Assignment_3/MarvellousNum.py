
def CheckPrime(No):  
        i =2
        while(i<=((No//2))):
        
            if No % i == 0:
                return False 
            i+=1
        return True

def PrimeList(Arr):

    Result = []
    for no in Arr:
        if(CheckPrime(no)==True):
            Result.append(no)
    return Result

def PrimeAddition(Arr):
    Sum =0
    for no in Arr:
        Sum =Sum+no

    return Sum        
