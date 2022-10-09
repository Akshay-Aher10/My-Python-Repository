# Accept Number and return Addition of its Factor

def FactorAdd(No):
    iSum =0
    for i in range(1,No):
        if (No % i) == 0:
            iSum = iSum+i
    return iSum    

def main():
    No = int(input("Ener Number\n"))
    ret = FactorAdd(No)
    print(ret)

if __name__ =="__main__":
    main()