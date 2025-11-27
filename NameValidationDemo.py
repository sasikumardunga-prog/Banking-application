#NameValidationDemo.py<---Main Program
from NameValidation import validatename
from NameExcept import InvalidNameError,SpaceError,ZeroNameLengthError
while(True):
    try:
        name=input("Enter Ur name:")
        vname=validatename(name) # Function Call gives result or exception
    except InvalidNameError:
        print("\t'{}' Invalid Name-try again".format(name))
    except SpaceError:
        print("\tDon't Enter Space for Name--try again")
    except ZeroNameLengthError:
        print("\tPlz Enter Ur Name--try again")
    else:
        print("\t'{} is valid Name".format(vname))
        break