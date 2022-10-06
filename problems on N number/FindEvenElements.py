# Accpets N numbers from user and Display Even Elements.
def Even(Arr):

    print("Even Elements :")

    for i in range(0,len(Arr)):
        if Arr[i] % 2 == 0:
            print(Arr[i])

def main():
    
    Arr = list()

    size = int(input("enter number of elements you want\n"))

    print("Enter Elements")
    for i in  range(0,size):
        no = int(input())
        Arr.append(no)

    Even(Arr)

if __name__ == "__main__":
    main()