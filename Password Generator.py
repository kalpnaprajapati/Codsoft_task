#Random password generator with a combination of characters.
import random
import string

def grpassword(l):
    c = string.ascii_letters + string.digits
    pd = ''.join(random.choice(c) for _ in range(l))
    return pd

ch='y' or 'yes' or 'Yes'
while ch=='y' or 'yes' or 'Yes':
    length=int(input("Enter Desired length for the PASSWORD :"))
    gp = grpassword(length)
    print("")
    print("Generated password:", gp)
    print("")
    print("NOTE - Enter y/yes/Yes to continue or any key + enter to Exit!")
    print("")
    ch=input("Do you want more suggestions?")
    print("")
print("Thank You For Using")
print("")