import threading

def Display_1to50():
    for i in range(1,51):
        print(i)

def Display_50to1():
    for i in range(50,0,-1):
        print(i)

def main():

    T1 = threading.Thread(target=Display_1to50)
    T2 = threading.Thread(target=Display_50to1)

    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__=="__main__":
    main()