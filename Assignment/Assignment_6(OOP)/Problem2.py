
class BankAccount:

    ROI = 5.56

    def __init__(self,A,B,C):
        self.Name =A
        self.Amount = B
        self.Account_Number = C
        self.Intrest = self.CalculateIntrest()


    def Display(self):

        print("""
        Account Holder Name : {Name}
        Account Number : {Number}
        Balance in Account : {Amount}
        """.format(Name =self.Name,Number =self.Account_Number,Amount =self.Amount))

    def Deposite(self,Amount):

        self.Amount = self.Amount+Amount

    def Withdraw(self,Amount):
        if self.Amount<Amount:
            print("Not Enough Balance..")
            return      
        self.Amount = self.Amount-Amount

    def CalculateIntrest(self):
        Intrest = self.Amount*BankAccount.ROI/100
        return Intrest

def main():
    
    Accounts = dict()
    No = 1
    print()
    print("---Welcome to HDFC Bank Portal---")    
    while(True):

        print("""
        Choise your Service
            1 : Open Bank Account
            2 : Deposite
            3 : Withdraw
            4 : Return on Investment
            5 : Intrest Rate
            6 : Account Details
            7 : Close App
        """)
        
        user_input = int(input("Enter Serive Number : "))
        if(user_input>7 or user_input<1):
            print()
            print("----Please Enter Valid Service Number")
            continue

        if(user_input == 1):
            FName = input("Enter Your First Name : ")
            LName = input("Enter Your Last  Name : ")
            Name = FName+" "+LName
            Amount = int(input("Enter yout Intial Amount :"))
            object = FName+str(No)
            object = BankAccount(Name,Amount,No)
            Accounts[No]=object
            #index+=1
            No+=1
            print()
            print("----------------------------------")
            print("Account Open Successfully")
            print("Your Account Number is : ",(No-1))
            print("----------------------------------")
            print()
            continue

        elif(user_input == 2):
            object = int(input("Enter your Account_No : "))

            if(object >= 1 and object <=len(Accounts)):
                no =1
                while(no <= len(Accounts)):

                    if no == object:
                        Amount = int(input("Enter Amount to Deposite :"))
                        Accounts[no].Deposite(Amount)
                        print("----------------------------------")
                        print("{} Deposited Successfully..!".format(Amount))
                        print("----------------------------------")
                    no+=1
            else:
                print()
                print("----------------------------------")
                print("Entered Wrong Account Number.")
                print("----------------------------------")
                continue     

        elif(user_input == 3):
            object = int(input("Enter your Account_No : "))
            if(object >= 1 and object <=len(Accounts)):
                no =1
                while(no <= len(Accounts)):

                    if no == object:
                        Amount = int(input("Enter Amount to WithDraw :"))
                        if(Amount < Accounts[no].Amount):
                            Accounts[no].Withdraw(Amount)
                            print("--------------------------------------")
                            print("{} Withdrew Successfully..!".format(Amount))
                            print("--------------------------------------")
                        else:
                            print()
                            print("----------------------------------")
                            print("Not Enough Balance....")
                            print("----------------------------------")
                            continue
                                            
                    no+=1
            else:
                print()
                print("----------------------------------")
                print("Entered Wrong Account Number.")
                print("----------------------------------")
                continue 

        elif(user_input == 4):
            object = int(input("Enter your Account_No : "))
            if(object >= 1 and object <=len(Accounts)):
                no =1
                while(no <= len(Accounts)):

                    if no == object:
                        Inrest =Accounts[no].CalculateIntrest()
                        print()
                        print("---------------------------------------")
                        print("intrest on Balance Amount. : ",Inrest)
                        print("---------------------------------------")
                    no+=1
            else:
                print()
                print("----------------------------------")
                print("Entered Wrong Account Number.")
                print("----------------------------------")
                continue 
            
        elif(user_input == 5):
            print("------------------------------------------------")
            print("Bank current Intrest Rate {}% ".format(BankAccount.ROI))
            print("------------------------------------------------")
        elif(user_input == 6):

            object = int(input("Enter your Account_No : "))

            if(object >= 1 and object <=len(Accounts)):
                no =1
                while(no <= len(Accounts)):

                    if no == object:
                        print()
                        print("---------Your Account Information---------")
                        Accounts[no].Display()
                        print("------------------------------------------")
                    no+=1  

            else:
                print()
                print("----------------------------------")
                print("Entered Wrong Account Number.")
                print("----------------------------------")
                continue 

        elif(user_input == 7):
            print()
            print("....Thank You ....")
            exit()   



if __name__=="__main__":
    main()    