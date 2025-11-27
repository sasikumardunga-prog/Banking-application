import oracledb as orc
from BankAccountOpen import open_account, check_balance
from BankPinGenerateUpdate import pin_update
from BankDeposit import deposit
from BankWithDraw import withdraw
from BankSearchCustomer import search_customer, single_customer_details, fetch_all_customers
from BankCloseAccount import close_account

conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
#print("Print obtains connection from oracle Database")
#print("Type of conobj=",type(conobj))
curobj=conobj.cursor()

print("\t\t\t Welcome to Ajith's Bank Services")
print("\n 1.Open an Account")
print("\n 2.Check Balance")
print("\n 3.PIN Change")
print("\n 4.Deposit")
print("\n 5.Withdraw")
print("\n 6.Search for Customer")
print("\n 7.View Single Customer Details")
print("\n 8.View All Customer Details")
print("\n 9.Close Account")

print("\n 10.Exit")


inp = int(input("Enter Your Choice: "))

while True:

    if inp == 1:
        open_account()

    elif inp == 2:
        check_balance()

    elif inp == 3:
        pin_update()

    elif inp == 4:
        deposit()

    elif inp == 5:
        withdraw()

    elif inp == 6:
        search_customer()

    elif inp == 7:
        single_customer_details()

    elif inp == 8:
        fetch_all_customers()

    elif inp == 9:
        close_account()

    elif inp == 10:
        print("Exited")
        break
        exit()

    else:
        print("Enter Valid Option! Try Again ")
        inp = int(input("Enter Your Choice: "))

