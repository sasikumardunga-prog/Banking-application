#ATMOperations.py
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter ur Deposit Amount:"))
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tur Account xxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tur Account xxxxxxxx123 Balance after Deposit INR:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter ur withdraw Amount:"))
    if(wamt<=0):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tur Account xxxxxxxx123 Debited With INR:{}".format(wamt))
        print("\tur Account xxxxxxxx123 Balance after withdraw INR:{}".format(bal))
def balenq():
    print("\tur Account xxxxxxxxx123 Balance with INR:{}".format(bal))