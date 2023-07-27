'''
#Types of variables and constructor
class Var():
    BankName = 'UNION'
    ROI = 0.7
    def __init__(self,Name,AccNo,Address):
        self.Name=Name
        self.AccNo=AccNo
        self.Address=Address
        print(self.Name,self.AccNo,self.Address,sep=' ')
ob1=Var('Prakash',2211334455,'Guntur')
print(ob1.BankName,ob1.ROI)
Var.ROI=0.5
Var.BankName='SBI'
print(ob1.BankName,ob1.ROI)

#Types of methods
class Bank():
    BName='Union Bank'
    ROI = 0.7
    def __init__(self,Name,AccNo,Amount):
        self.Name=Name
        self.AccNo=AccNo
        self.Amount=Amount
        print(self.Name,self.AccNo,self.Amount,sep=' ')
    @classmethod
    def changeROI(cls,n):
        cls.ROI=n
ob1=Bank('Prakash',22113344,20000)
print(ob1.ROI)
Bank.changeROI(0.5)
print(ob1.ROI)

#Encapsulation
class A:
    def __init__(self):
        self.__x=10
    def Getter(self):
        print(self.__x)
    def Setter(self,n):
        self.__x=n
        print(self.__x)
ob1=A()
ob1.Getter()
ob1.Setter(30)

#Inheritance
class BankV1():
    BName='Union Bank'
    ROI=0.5
    def __init__(self,Name,Acc,Amount,Pin):
        self.Name=Name
        self.Acc=Acc
        self.Amount=Amount
        self.Pin=Pin
    def display(self):
        print(f'Name    :   {self.Name}')
        print(f'Account :   {self.Acc}')
        print(f'Amount  :   {self.Amount}')
    def withdraw(self,amt):
        self.amt=amt
        if self.Pin==self.getPin():
            if self.amt<=self.Amount:
                self.Amount-=self.amt
            else:
                print('Insufficient Funds')
        else:
            print('Incorrect Pin...')
            
class BankV2(BankV1):
    def __init__(self, Name, Acc, Amount,Pin,PhNo,Address):
        BankV1.__init__(self,Name, Acc, Amount, Pin)
        self.PhNo=PhNo
        self.Address=Address
    def display(self):
        BankV1.display(self)
        print(f'Ph-No   :   {self.PhNo}')
        print(f'Address :   {self.Address}')
    @staticmethod
    def getPin():
        n=int(input('Enter your pin : '))
        return n

ob1=BankV2('Prakash',22113344,50000,1234,9963896549,'Guntur')
ob1.display()
ob1.withdraw(10000)
ob1.display()

# Method OverLoading
class Sample():
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x
    def __mul__(self,other):
        return self.x*other.x
ob1=Sample(2)
ob2=Sample(3)
print(ob1+ob2)
print(ob1*ob2)

#Abstraction
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def speak(self):
        pass
    def move(self):
        pass
class Dog(A):
    def speak(self):
        print('BOW BOW')
class cat(A):
    def speak(self):
        print('Meow Meow')
ob1=Dog()
ob2=cat()
ob1.speak()
ob2.speak()'''

