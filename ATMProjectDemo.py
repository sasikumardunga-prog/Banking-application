from ATMExcept import DepositError,WithDrawError,InSuffFundError
from ATMMenu import menu
from ATMOperactions import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("enter ur choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tdon't deposit -ve and Zero Values")
                except ValueError:
                 print("\tDont try to withdraw alnums,str and symbols")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDont Withdraw -ve and Zero values")
                except ValueError:
                    print("\tDont try to withdraw alnums,strs and symbols")
                except InSuffFundError:
                    print("\tur Account does not contains Funds")
            case 3:
                balenq()
            case 4:
                print("thx for using this project")
                break
            case _:
                print("\tur selection of operation is wrong-try again")
    except ValueError:
                print("\tDon't enter alnums,strs and symbols for choice--try again")

