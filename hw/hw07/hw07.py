""" Homework 07: Special Method, Linked Lists and Mutable Trees"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    >>> print(zero + zero)
    0
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    """
    @staticmethod
    def kickzero(lst):
        while lst[len(lst)-1]==0 and lst !=[0]:#傻逼了，末尾可能不只有一个0
            lst.pop(len(lst)-1)
        return lst
    def __init__(self,lst):
        self.orilst=Polynomial.kickzero(lst)
        self.highist=len(lst)-1#最高次数
        self.lst=list(enumerate(lst))
    def __str__(self):
        z=f"{self.lst[0][1]}"
        i = 1
        while(i<=self.highist):
            z+=f" + {self.lst[i][1]}*x^{i}"
            i+=1
        return z
    def __repr__(self):
        return f"Polynomial({self.orilst})"
    
    def __add__(self,other):
        highest=max(self.lst[::-1][0][0],other.lst[::-1][0][0])
        lowest=min(self.lst[::-1][0][0],other.lst[::-1][0][0])
        temp=[]
        for i in range(0,lowest+1):
            temp.append(self.lst[i][1]+other.lst[i][1])
        for i in range (lowest+1,highest+1):
            if len(self.lst)>len(other.lst):
                temp.append(self.lst[i][1])
            else:
                temp.append(other.lst[i][1])
        return Polynomial(temp)
    
          
    def __mul__(self,other):
        highest=self.lst[::-1][0][0]+other.lst[::-1][0][0]
        temp=[]
        for i in range (0,highest+1):
            temp.append(getn(self.lst,other.lst,i))
        return Polynomial(temp)
def getn(la,lb,n):
        temp = 0
        for i in la:
            for j in lb:
                if i[0]+j[0]==n:
                    temp+=i[1]*j[1]
        return temp   


def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1)
    """
    if lnk!=Link.empty :
        while lnk!=Link.empty and lnk.rest!=Link.empty and lnk.rest.first==lnk.first :
            lnk.rest.rest,lnk.rest=Link.empty,lnk.rest.rest
        remove_duplicates(lnk.rest)
        

def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    #递归
    # if lnk == Link.empty:
    #     return lnk
    # if lnk.rest==Link.empty:
    #     return lnk
    
    # a=reverse(lnk.rest)
    # lnk.rest.rest=lnk
    # lnk.rest=Link.empty
    # return a

    #三指针


    now=lnk
    pre=Link.empty
    next=now
    while(next!=Link.empty):#若为空说明now到头了，后面就是()
        now=next#第一次什么也没发生，之后next是修改方向前now的rest
        #每次开始状态now和next重叠，pre在前一个
        next=now.rest#next后移一位
        now.rest=pre#修改当前链位rest的方向到它的前一位
        pre=now#pre跟上
    return now



        
    
        
            
            
        
            



class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self,other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        temp=False
        if self.is_leaf() and other.is_leaf() :
            return self.label==other.label
        if len(self.branches)!=len(other.branches):
            return False
        for i in range( 0,(len(self.branches))):
            temp=self.label==other.label and self.branches[i].__eq__(other.branches[i])
            if temp == False:
                return False
        return temp
        
        


def generate_paths(t, value):###下周实验课着重再看一下
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** YOUR CODE HERE ***"
    #深度优先搜索
    #先找，找到和不找到都往下找
    #找到就yield一下
    #找到头应该就自动停止？因为branches不触发
    def helper(t,value,ans=[]):
        #helper的返回值是一个迭代器
        '''真正在递归中要使用的是迭代器的生成值
           所以要么yield from直接把生成值取出来
           要么手动遍历迭代器 生成生成值
           yield : 生成'''
        ans.append(t.label)
        if t.label==value:
            yield ans
        for b in t.branches:
            yield from helper(b,value,ans.copy())#避免在不同分支处对ans改来改去的复杂处理
            #应该返回生成列表的生成器，而不是生成生成列表的生成器的生成器
            #沟槽套娃
    return helper(t,value)


def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    if total==0:
        return Tree('1')
    if total<0 or len(denominations)==0:
        return 
    a=count_coins_tree(total,denominations[1::])
    b=count_coins_tree(total-denominations[0],denominations)
    if  a and b:
        return Tree(f"{total}, {denominations}",[a,b])
    elif a:
        return Tree(f"{total}, {denominations}",[a])
    elif b:
        return Tree(f"{total}, {denominations}",[b])

def bst_min(t):
    return t.branches[0].label
def bst_max(t):
    temp=[]
    return t.branches[-1].label
    
    
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    temp = True
    if len(t.branches)>2:
        return False
    if len(t.branches)==2:
        if t.label>=bst_max(t) or t.label<bst_min(t):
            return False
        for bb in t.branches[0].branches:
            if bb.label>t.label:
                return False
        for bb in t.branches[-1].branches:
            if bb.label<=t.label:
                return False
    if len(t.branches)==1 and len(t.branches[0].branches)==1:
        if (t.label-t.branches[0].label)*(t.label-t.branches[0].branches[0].label)<0:
            return False
    for b in t.branches:     
        temp = temp and is_bst(b) 
    return temp
    


##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
