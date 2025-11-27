import oracledb as orc
conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
curobj=conobj.cursor()

def close_account():
    Account_no = int(input("Enter your Account Number: "))

    while True:
        if len(str(Account_no)) != 12:
            print("Enter Valid Account Number! ")
        else:
            break
    query = """
                delete bank where acno = :acc_no
            """
    data = {
        "acc_no": Account_no
    }

    while True:
        statement = input("Do You want to Close your Account? type : yes / no \n")
        if statement.lower() == 'yes':
            try:
                curobj.execute(query, data)
                print("Your Account has been closed successfully!")
                break
            except Exception as e:
                print(str(e))
                break
        elif statement.lower() == 'no':
            print("Account Closure has been Cancelled! ")
            break
        else:
            print("Invalid option!! Try Again !!")

    conobj.commit()
