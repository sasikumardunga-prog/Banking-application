import oracledb as orc
conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
curobj=conobj.cursor()

def pin_update():
    Account_no = int(input("Enter Your Account_Number: "))

    while True:
        pin = int(input("Enter Your Four Digit Pin want to update"))
        if len(str(pin)) != 4:
            print("Enter Your PIN with Four Digit only")
        else:
            break
    query = """
            UPDATE BANK SET PIN = :pin WHERE ACNO = :acc_no
        """
    data = {
        "pin": pin,
        "acc_no": Account_no
    }
    # Insert the data
    oa = curobj.execute(query, data)

    # Fetch the data you just inserted
    print("PIN Updated Successfully! Thank you for using our service! ")
    conobj.commit()