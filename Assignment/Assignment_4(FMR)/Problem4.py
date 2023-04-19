# use Filter Map Reduce.
# Accpet list of number From user.
# Filter : All such number which Even
# Map : calculate its square.
# Reduce : Return Addition of All that mapped number.

# Entered Data : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# Filtered Data : [2, 4, 4, 2, 8, 10]
# Mapped Data : [4, 16, 16, 4, 64, 100]
# Reduced Data : 204


#-----------------------------------------------------#

from functools import reduce


def AccpetNumber():
    Result = []

    No = int(input("Enter Number of Element you want in List\n"))

    print("Enter Elemnet")
    for i in range(0,No):
        Value = int(input())
        Result.append(Value)

    return Result 
    
def main():

    Data = AccpetNumber()
    print("Entered Data :",Data)

    #-----------------------------------------------------#  
    # in build_Filter

    Filtered_Data = list(filter(lambda No : No%2 ==0,Data))
    print("Filtered Data :",Filtered_Data)

    #-----------------------------------------------------#  
    # in build_Map

    Mapped_Data = list(map(lambda No :No**2,Filtered_Data))
    print("Mapped Data :",Mapped_Data)

    #-----------------------------------------------------#  
    # in build_Reduce

    Reduced_Data = reduce(lambda A,B : A+B,Mapped_Data)
    print("Reduced Data :",Reduced_Data)



if __name__=="__main__":
    main()
