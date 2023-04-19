import threading

def DisplayEven(No):

    for i in range(1,No+1):
        if(i%2 ==0):
            print("{} is even Number".format(i))


def DisplayOdd(No):

    for i in range(1,No+1):
        if(i%2 !=0):
            print("{} is Odd Number".format(i))

def main():

    Value =20

    T1 = threading.Thread(target=DisplayEven, args=(Value,))
    T2 = threading.Thread(target=DisplayOdd, args =(Value,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Successfully Print first 10 Even and Odd numbers")

if __name__=="__main__":
    main()


#output:

# 2 is even Number
# 4 is even Number 
# 6 is even Number 
# 8 is even Number 
# 10 is even Number
# 1 is Odd Number  
# 12 is even Number
# 3 is Odd Number
# 14 is even Number
# 16 is even Number
# 18 is even Number
# 5 is Odd Number
# 7 is Odd Number
# 9 is Odd Number
# 11 is Odd Number
# 20 is even Number
# 13 is Odd Number
# 15 is Odd Number
# 17 is Odd Number
# 19 is Odd Number
# Successfully Print first 10 Even and Odd numbers