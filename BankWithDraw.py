import oracledb as orc
conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
curobj=conobj.cursor()

def withdraw():
    Account_no = int(input("Enter Your Account_Number: "))
    amount = int(input("Enter the amount You want to withdraw: "))
    query = """
            update bank set bal = bal - :amount where acno = :acc_no
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

    curobj.execute("SELECT bal FROM bank WHERE ACNO = :acc_no", {"acc_no": Account_no})
    inserted_record = curobj.fetchone()
    print(f"You have successfully withdrawn: {amount}/- and Your remaining Balance is: {inserted_record}")
    conobj.commit()

