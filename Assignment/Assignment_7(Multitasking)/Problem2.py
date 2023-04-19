import threading


def Addition_of_EvenFactor(No):
    Sum = 0
    for i in range(1,int(No/2)+1):
        if(No%i ==0 and i%2 ==0):
            Sum = Sum+i
    print("Addition of Even Factor : ",Sum)
  
def Addition_of_OddFactor(No):
    Sum = 0
    for i in range(1,int(No/2)+1):
        if(No%i ==0 and i%2 !=0):
            Sum = Sum+i
    print("Addition of Odd Factor : ",Sum)

def main():
    Value = (int(input("Enter Number : ")))

    T1 = threading.Thread(target=Addition_of_EvenFactor,args=(Value,))
    T2 = threading.Thread(target=Addition_of_OddFactor,args=(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("exit from main")
    
if __name__=="__main__":
    main()



# output:12

# Enter Number : 12
# Addition of Even Factor :  12
# Addition of Odd Factor :  4  
# exit from main