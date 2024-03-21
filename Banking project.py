#TOPIC:BANKING SYSTEM REPLICA
#MAIN MENU:1.CREATE NEW ACCOUNT,2. ACCOUNT LOG IN
# BANK OPERATIONS: 1.DEPOSIT,2.WITHDRAW,3.BALANCE EQUIRY,4.ACCOUNT DETAILS
Bank_name='MY_BANK'
print("******WELCOME TO",Bank_name,"******")
def create(accounts):
    Ac_no=input("Enter your account number:")
    if Ac_no in accounts:
        print("Your are entered account holder is already exist")
    else:
        name=input("Name:")
        address=input("Address:")
        ph_no=input("Phone number:91-")
        password=input("Password:")
        balance=float(input("Initial balance:"))
        accounts[Ac_no]={'Name':name,'Address':address,'Ph_no':ph_no,'Password':password,'Balance':balance}
        print("Hello",name,"Congradulations,Welcome To **",Bank_name,"**,Your account created successfully.\nYour account number  is:",Ac_no)
def Ac_login(accounts):
    Ac_no=input("Enter your account number:")
    password=input("Enter your account password:")
    if Ac_no in accounts and accounts[Ac_no]['Password']==password:
        return Ac_no
    else:
        print("Invalid account number or password..")
def deposit(accounts,Ac_no):
    amount=float(input("enter the amount to deposit:"))
    if amount>0:
        accounts[Ac_no]['Balance']+=amount
        print("Your account is credited with Rs",amount,"current balance is Rs.",accounts[Ac_no]['Balance'])
    else:
        print("Please enter a valid amount")
def withdraw(accounts,Ac_no):
    amount=float(input("Enter the amount to withdraw:"))
    if accounts[Ac_no]['Balance']>=amount>0:
        accounts[Ac_no]['Balance']-=amount
        print("Rs.",amount,"debited from your account, Available balance is",accounts[Ac_no]['Balance'])
    else:
        print("Insufficent fund")
def balance_enq(accounts,Ac_no):
    print("Available balance for account number",Ac_no,"available balance is Rs.",accounts[Ac_no]['Balance'])
def Ac_details(accounts,Ac_no):
    print("------Your Account Details-------")
    print("Account name:",accounts[Ac_no]['Name'])
    print("Account Number:",Ac_no)
    print("Address:",accounts[Ac_no]['Address'])
    print("Phone number:",accounts[Ac_no]['Ph_no'])
    print("Available balance:Rs.",accounts[Ac_no]['Balance'],"\n-------------------------")



def bank_main():
    accounts={}
    while True:
        print("1.Create new account\n2.Aclog_in\n3.Exit")#MAIN MENU
        choice=int(input("Enter your choice:"))
        if choice==1:
            create(accounts)
        elif choice==2:
            Ac_no=Ac_login(accounts)
            if Ac_no:
                print("Logged in successfully, Welcome",accounts[Ac_no]['Name'])
                while True:
                    print("Bank Operations")#BANK OPERATIONS MENU
                    print("1.Deposit\n2.Withdraw\n3.Balance Enquiry\n4.Account details\n5.Log out")
                    choice_opt=int(input("Enter the bank operation choice:"))
                    if choice_opt==1:
                        deposit(accounts,Ac_no)
                    elif choice_opt==2:
                        withdraw(accounts,Ac_no)
                    elif choice_opt==3:
                        balance_enq(accounts,Ac_no)
                    elif choice_opt==4:
                        Ac_details(accounts,Ac_no)
                    elif choice_opt==5:
                        print("Logging out, Thank you for using",Bank_name)
                        break
                    else:
                        print("wrong choice, try again")
        elif choice==3:
            print("Thank you for using",Bank_name,",visit again")
            break
        else:
            print("invalid choice, try again")

bank_main()
