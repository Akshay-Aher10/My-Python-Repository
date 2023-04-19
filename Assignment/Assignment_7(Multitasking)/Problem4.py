import threading

def Display_Capital(String1):
    No = 0
    for i in String1:
        if(i>='A' and i<='Z'):
            No+=1
    print("No of Capital Characters :",No)

def Display_Small(String1):
    No = 0
    for i in String1:
        if(i>='a' and i<='z'):
            No+=1
    print("No of Small Characters :",No)

def Display_Digit(String1):
    No = 0
    for i in String1:
        #if(i.isdigit()==True):
        if(i>='1' and i<='9'):
            No+=1
    print("No of Digits :",No)

def main():

    str ="AkshayAher123"

    T1 = threading.Thread(target=Display_Capital, args=(str,))
    T2 = threading.Thread(target=Display_Small, args=(str,))
    T3 = threading.Thread(target=Display_Digit, args=(str,))        

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__=="__main__":
    main()

# C:\Users\dell\Desktop\Python\Assignment\Assignment_7>python Problem4.py
# No of Capital Characters : 2
# No of Small Characters : 8
# No of Digits : 3    