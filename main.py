import json 
import random
import string
from pathlib import Path

class Bank:
    database = Path(__file__).parent / 'data.json'
    data = []

    @staticmethod
    def load_data():
        try:
            if Bank.database.exists():
                with open(Bank.database, 'r') as fs:
                    Bank.data = json.load(fs)
            else:
                Bank.data = []
                print("No file found, creating new one.")
        except Exception as err:
            print(f"Error: {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
             json.dump(Bank.data, fs, indent=4)


    @classmethod
    def __accoutgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info={
            "name":input("tell your name:-"),
            "age":int(input("tell your age:-")),
            "email":input("tell your email:-"),
            "pin":int(input("trll your 4 number pin:-")),
            "accountNo.":Bank.__accoutgenerate(),
            "balance":0
        }
        if info['age']<18 or len(str(info['pin']))!=4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i}:{info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnumber=input("please tell your account number:-")
        pin=int(input("please tell your pin number:-"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("sorry no data found")

        else:
            amount=int(input("how much you want to depoit:-"))
            if amount>10000 or amount<0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print("amount deposited successfully")


    def withdrowmoney(self):
        accnumber=input("please tell your account number:-")
        pin=int(input("please tell your pin number:-"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("sorry no data found")

        else:
            amount=int(input("how much you want to withdrow:-"))
            if userdata[0]['balance']<amount:
                print("sorry you do not have that much money")

            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print("amount withdrew successfully")


    def showdetails(self):
        accnumber=input("please tell your account number:-")
        pin=int(input("please tell your pin number:-"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        print("your information are \n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")


    def updatedetails(self):
        accnumber=input("please tell your account number:-")
        pin=int(input("please tell your pin number:-"))

        userdata=[i for i in Bank.data if i['accountNo.']==accnumber and i['pin']==pin]

        if userdata==False:
            print("no such user found")

        else:
            print("you can not change the age, account number, balance \n")

            print("Fill the details for change or leave it empty if no change")

            newdata={
                "name": input("please tell new name or press enter to skip:-"),
                "email": input("please tell new email or press enter to skip:-"),
                "pin": input("please tell new pin or press enter to skip:-"),
            }

            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']

            newdata['age']=userdata[0]['age']
            newdata['accountNo.']=userdata[0]['accountNo.']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])


            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            
            Bank.__update()
            print("details updated successfully")


    def Delete(self):
        accnumber = input("please tell your account number:-")
        pin = int(input("please tell your pin number:-"))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no such account found")
            return

        check = input("Press Y to delete account or N to cancel:- ")

        if check.lower() == 'n':
            print("Deletion cancelled")
            return

        index = Bank.data.index(userdata[0])
        Bank.data.pop(index)

        print("Account deleted successfully")
        Bank._Bank__update()



Bank.load_data()
user= Bank()

print("press 1 for Creating an account")
print("press 2 for Deposititing money in the bank account")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")


check = int(input("tell your response:-"))


if check == 1:
    user.Createaccount()

if check==2:
    user.depositmoney()

if check==3:
    user.withdrowmoney()

if check==4:
    user.showdetails()

if check==5:
    user.updatedetails()

if check==6:
    user.Delete()