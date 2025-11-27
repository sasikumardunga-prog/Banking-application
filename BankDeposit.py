import oracledb as orc
conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
curobj=conobj.cursor()

def deposit():
    Account_no = int(input("Enter Your Account_Number: "))
    amount = int(input("Enter the amount You want to Deposit: "))
    query = """
            update bank set bal = bal + :amount where acno = :acc_no
        """
    data = {
        "acc_no": Account_no,
        "amount": amount
    }
    try:
        # Insert the data
        curobj.execute(query, data)
    except Exception as e:
        print(str(e))
    print("Your Balance Deposited Successfully! Thank you for using our service! ")
    conobj.commit()
