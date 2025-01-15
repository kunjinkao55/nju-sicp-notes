""" Lab 6: OOP and Inheritance"""
import random

# ANSWER QUESTION q1

# ANSWER QUESTION q2

#####################
# Required Problems #
#####################

class PrintModule:
    def pp(self):
        pretty_print(self)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,stock,price):
        self.stock=stock
        self.price=price
    remain_stock=0
    balance=0
    def vend(self):
        if self.balance==self.price and self.remain_stock>0:
            self.remain_stock-=1
            self.balance=0
            return'Here is your {0}.'.format(self.stock)
        elif self.balance>self.price and self.remain_stock>0:
            temp=self.balance-self.price
            self.balance=0
            self.remain_stock-=1
            return'Here is your {0} and ${1} change.'.format(self.stock,temp)
        elif self.remain_stock<=0:
            return  'Machine is out of stock.'
        elif self.balance<self.price and self.remain_stock>0:
            return 'You must add ${0} more funds.'.format(self.price-self.balance)
    def add_funds(self,money):
        if self.remain_stock>0:
            self.balance+=money
            return 'Current balance: ${0}'.format(self.balance)
        else:
            return 'Machine is out of stock. Here is your ${0}.'.format(money)
    def restock(self,num):
        self.remain_stock+=num
        return 'Current {0} stock: {1}'.format(self.stock,self.remain_stock)




class Pet(PrintModule):
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)

    def to_str(self):
        return '({0}, {1})'.format(self.name,self.owner)



class Cat(Pet):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        self.lives=lives
        self.name=name
        self.owner=owner
        self.is_alive = True 

    def talk(self):
        """ Print out a cat's greeting.
        """
        print( self.name+' says meow!')


    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print(self.name + ' has no more lives to lose.')
        elif self.lives>0:
            self.lives-=1
            if self.lives == 0:
                self.is_alive=False
            
    def to_str(self):
        return '({0}, {1}, {2})'.format(self.name,self.owner,self.lives)


class NoisyCat(Cat): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        Cat.talk(self)
        Cat.talk(self)
        #通过类路径访问父类Cat的方法，保证数据抽象，避免更改实现方式导致功能异常


class Colors:
    HEADER     = '\033[95m'
    OKBLUE     = '\033[34m'
    OKCYAN     = '\033[35m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'


def pretty_print(obj):
    """Pretty prints the object using the Colors class.
    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> pretty_print(kyubey)
    \033[34mPet\033[0m\033[35m(Kyubey, Incubator)\033[0m
    """
    print(f"{Colors.OKBLUE}{type(obj).__name__}{Colors.ENDC}"+f"{Colors.OKCYAN}{type(obj).to_str(obj)}{Colors.ENDC}")


class Time:
    """ A class that can store and display the date.
    >>> time = Time(2024, 11, 20)
    >>> print(time.to_str())
    24.11.20
    >>> time.setyear(2023)
    >>> time.setmonth(2)
    >>> time.setday(5)
    >>> time.setformat("dd-mm-yy")
    >>> time.to_str()
    '05-02-23'
    >>> time.setformat("y/mm/dd")
    >>> time.to_str()
    'y/02/05'
    >>> time.setyear(-1)
    Parameter Error!
    >>> time.to_str()
    '23/02/05'
    >>> time1 = Time(-1, 11, 20)
    Parameter Error!
    """
    def __init__(self, year, month, day):
        """Initialize a Time object."""
        self.year=str(year%100).zfill(2)
        self.month=str(month).zfill(2)
        self.day=str(day).zfill(2)
        self.format='yy.mm.dd'

    def setyear(self, year):
        """Set the year of the Time object."""
        if not isinstance(year, int) or  year<0 or year > 9999:
            print('Parameter Error!')
            return
        self.year=str(year%100).zfill(2)

    def setmonth(self, month):
        """Set the month of the Time object."""
        if not isinstance(month, int) or month>12 or month<1:
            print('Parameter Error!')
            return
        self.month=str(month).zfill(2)
        
    def setday(self, day):
        """Set the day of the Time object."""
        if  not isinstance(day, int) or day>31 or day<1:
            print('Parameter Error!')
            return
        self.day=str(day).zfill(2)

    def setformat(self, format):
        """Set the format of the Time object."""
        self.format=format
        self.format=self.format.replace("yy",self.year,1)
        self.format=self.format.replace("mm",self.month,1)
        self.format=self.format.replace("dd",self.day,1)

        

    def to_str(self):
        """Return the formatted date."""
        self.setformat(self.format)
        return self.format
        