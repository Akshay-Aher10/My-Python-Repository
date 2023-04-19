
import threading

def Even_List(Numbers):
    Sum = 0
    for no in Numbers:
        if(no%2 ==0):
            Sum = Sum+no
    print("Addition of Even Elements :",Sum)

def Odd_List(Numbers):
    Sum = 0
    for no in Numbers:
        if(no%2 !=0):
            Sum = Sum+no
    print("Addition of Odd Elements :",Sum)

def main():

    List = [1,2,3,4,5,6,7,8,9,10]

    T1 = threading.Thread(target=Even_List, args=(List,))
    T2 = threading.Thread(target=Odd_List, args=(List,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__=="__main__":
    main()    


# output :
# python Problem3.py
# Addition of Even Elements : 30
# Addition of Odd Elements : 25    