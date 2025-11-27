import oracledb as orc
conobj=orc.connect("system/tiger@127.0.0.1:1522/orcl")
curobj=conobj.cursor()

def search_customer():
    Account_no = int(input("Enter Your Account_Number: "))
    query = """
            select * from bank where acno = :acc_no 
        """
    data = {
        "acc_no": Account_no,
    }

    curobj.execute(query, data)

    curobj.execute("SELECT cname FROM bank WHERE ACNO = :acc_no", {"acc_no": Account_no})
    inserted_record = curobj.fetchone()
    print("Your Record: ", inserted_record)
    print("Thank you for using our service! ")
    conobj.commit()

def single_customer_details():
    Account_no = int(input("Enter Your Account_Number: "))
    query = """
                select * from bank where acno = :acc_no 
            """
    data = {
        "acc_no": Account_no,
    }

    curobj.execute(query, data)

    curobj.execute("SELECT * FROM bank WHERE ACNO = :acc_no", {"acc_no": Account_no})
    inserted_record = curobj.fetchone()
    print("Your Record: ", inserted_record)
    print("Thank you for using our service! ")
    conobj.commit()


def fetch_all_customers():
    query = """
                select * from bank 
            """

    curobj.execute(query)

    curobj.execute("SELECT * FROM bank" )
    inserted_record = curobj.fetchall()
    print("Your Record: ", inserted_record)
    print("Thank you for using our service! ")
    conobj.commit()
