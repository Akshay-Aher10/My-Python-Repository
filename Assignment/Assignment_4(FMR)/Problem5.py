# use Filter Map Reduce.
# Accpet list of number From user.
# Filter : Filter out all prime number
# Map : Multiply Each number ny 2
# Reduce : return Maximum number from that numbers.

# Entered Data : [2, 70, 11, 10, 17, 23, 31, 77]
# Filtered Data : [2, 11, 17, 23, 31]
# Mapped Data : [4, 22, 34, 46, 62]
# Reduced Data : 62

#-----------------------------------------------------#  

def AccpetNumber():
    Result = []

    No = int(input("Enter Number of Element you want in List\n"))

    print("Enter Elemnet")
    for i in range(0,No):
        Value = int(input())
        Result.append(Value)

    return Result

#-----------------------------------------------------#  
# Filter 

def CheckPrime(No):
    
    for i in range(1,No+1):
        if(No%i==0 and i != 1 and i !=No):
            return False
    return True

def filterX(Helper_Function,Arr):
    result = []
    for i in Arr:
        if Helper_Function(i)==True:
            result.append(i)
    return result

#-----------------------------------------------------#  
# Map
 
Increase = lambda No: No*2

def mapX(Helper_Function,Arr):
    Result = []

    for i in Arr:
        No = Helper_Function(i)
        Result.append(No)
    
    return Result

#-----------------------------------------------------#
#Reduce

Maximum = lambda Arr : max(Arr)

def reduceX(Helper_Function,Arr):

    max = Helper_Function(Arr)
    return max

#-----------------------------------------------------#   
def main():

    Data = AccpetNumber()
    print("Entered Data :",Data)

    Filtered_Data = filterX(CheckPrime,Data)
    print("Filtered Data :",Filtered_Data)

    Mapped_Data = mapX(Increase,Filtered_Data)
    print("Mapped Data :",Mapped_Data)

    Reduced_Data = reduceX(Maximum,Mapped_Data)
    print("Reduced Data :",Reduced_Data)


if __name__ =="__main__":
    main()