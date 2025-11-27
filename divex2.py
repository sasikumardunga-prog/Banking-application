#program for cal div of two number
try:
    print("program execution started")
    s1=input("\tEnter first value:")
    s2=input("\tEnter second value:")
    a=float(s1)
    b=float(s2)
    c=a/b
except zerodivisionerror:
    print("\tdon't enter zero for den")
except valueeroor:
    print("\tdon't enter alnums,strs and symbols")
else:
    print("\tval of a=",a)
    print("\tval of b=",b)
    print("\tdiv=",c)
finally:
    print("\tend")

