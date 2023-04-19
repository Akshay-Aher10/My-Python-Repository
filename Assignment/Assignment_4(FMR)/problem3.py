# use Filter Map Reduce.
# Accpet list of number From user.
# Filter : All such number which number>=70 and number<=90
# Map : increase each no by 10
# Reduce : Return Product of All that mapped number.

# Entered Data : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# Filtered Data : [76, 89, 86, 90, 70]
# Mapped Data : [86, 99, 96, 100, 80]
# Reduced Data : 6538752000

#-----------------------------------------------------#

def AcceptNumber():
    Result = []

    No = int(input("Enter Number of Element you want in List\n"))

    print("Enter Elemnet")
    for i in range(0,No):
        Value = int(input())
        Result.append(Value)

    return Result
#-----------------------------------------------------#  
# Filter 

DataFilter = lambda no: no>=70 and no<=90

def filterX(Helper_Function,Arr):
    Result = []

    for i in Arr:
        if(Helper_Function(i)==True):
            Result.append(i)
    return Result

#-----------------------------------------------------#  
# Map
Increase = lambda No: No+10

def mapX(Helper_Function,Arr):
    Result = []

    for i in Arr:
        No = Helper_Function(i)
        Result.append(No)
    
    return Result

#-----------------------------------------------------#  
# Reduce

Product = lambda No1,No2 : No1*No2

def reduceX(Helper_Function,Arr):
    Mult =1
    for i in Arr:
        Mult = Helper_Function(Mult,i)

    return Mult

#-----------------------------------------------------#  

def main():

    Data = AcceptNumber()
    print("Entered Data :",Data)

    Filtered_Data = filterX(DataFilter,Data)
    print("Filtered Data :",Filtered_Data)

    Mapped_Data = mapX(Increase,Filtered_Data)
    print("Mapped Data :",Mapped_Data)

    Reduced_Data = reduceX(Product,Mapped_Data)
    print("Reduced Data :",Reduced_Data)

if __name__=="__main__":
    main() 