#NameValidation.py<--Module Name
from NameExcept import InvalidNameError,SpaceError,ZeroNameLengthError
def validatename(name):#name=Guido Va2n Rossum
    if(len(name)==0):
        raise ZeroNameLengthError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return " ".join(words)
        else:
            raise InvalidNameError