
""" Homework 3: Recursion """

HW_SOURCE_FILE = 'hw03.py'


#####################
# Required Problems #
#####################


def integrate(f, l, r, min_interval):
    """Return the definite integration of function f over interval 
    [l,r], with interval length limit min_interval.

    >>> abs(integrate(lambda x: x * x, 1, 2, 0.01) - (7 / 3)) < 0.001
    True
    >>> abs(integrate(lambda x: x, 1, 2, 0.01) - 1.5) < 0.0001
    True
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'integrate', ['While', 'For'])
    True
    """
    #第一种方法，但是没过，什么原因？
    '''if l<=r:
        y1=f(l)
        y2=f(l+min_interval)
        area=(y1+y2)*min_interval/2
        ans=area+integrate(f,l+min_interval,r,min_interval)
    else:
        return 0
    return ans

    if l<=r:
        mid=(l+r)/2

    else:
        return 0'''
    if r - l < min_interval: 
        return (f(l) + f(r)) * (r - l) / 2  
    mid = (l + r) / 2
    left_area = integrate(f, l, mid, min_interval) 
    right_area = integrate(f, mid, r, min_interval)  
    return left_area + right_area  





    

        



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    5
    >>> pingpong(8)
    4
    >>> pingpong(15)
    3
    >>> pingpong(21)
    5
    >>> pingpong(22)
    6
    >>> pingpong(30)
    10
    >>> pingpong(68)
    0
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    -1
    >>> pingpong(72)
    -2
    >>> pingpong(100)
    6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def helpback(i, k, num_of_six):
        def count_six(k,num_of_six):
             if (k//100%10==6)or( k//10 % 10 == 6 ) or ( k % 10 == 6  ) or (k % 6 == 0):
                return num_of_six+1
             else:
                return num_of_six
        if k >= n:
            return i
        return helpback(i+pow(-1,count_six(k,num_of_six))  ,  k+1  ,  count_six(k,num_of_six))
        
       

    return helpback(1, 1, 0)




def balanced(s):
    """Returns whether the given parentheses sequence s is balanced.
    >>> balanced('()')
    True
    >>> balanced(')')
    False
    >>> balanced('(())')
    True
    >>> balanced('()()')
    True
    >>> balanced('()())')
    False
    >>> balanced('()(()')
    False
    """

    def divide(s, k):#在某个位置左右劈开
        """Divide the given parentheses sequence s into two parts at position k.
        >>> left, right = divide('()()', 2)
        >>> left
        '()'
        >>> right
        '()'
        >>> left, right = divide('(())()', 4)
        >>> left
        '(())'
        >>> right
        '()'
        >>> left, right = divide('(())()', 6)
        >>> left
        '(())()'
        >>> right
        ''
        """
        return (s[:k], s[k:])

    def peel(s):#剥离一层
        """Peel off the leftmost and rightmost parentheses in s to obtain the
        internal part of the parentheses sequence.
        >>> peel('(())')
        '()'
        >>> peel('()')
        ''
        >>> peel('))((')
        ')('
        """
        return s[1:-1]

    def match(s):#判断最外层是否平衡
        """Returns whether the leftmost and the rightmost parentheses in s match.
        >>> match('()')
        True
        >>> match('()()')
        True
        >>> match('()))')
        True
        >>> match('))')
        False
        >>> match(')())')
        False
        """
        return s[0] == '(' and s[-1] == ')'

    "*** YOUR CODE HERE ***"
    right=s
    m=0
    while right:
        left,right=divide(right,1)
        if left =='(':
            m+=1
        if left ==')':
            m-=1
        if left!="("and left !=")" :#第二次犯这种错误了，悲，条件句要写完整啊啊啊啊啊啊啊哼哼哼
            m+=1000000000000000
        if m<0:
            return False
    if m == 0:
        return True
    else:
        return False
# case 1:中间对称，左右逐层开剥
#case 2 中间不对称，从每一个人可能位置分开，判断每种断点左右两边是否平衡






def count_change(total, money):
    """Return the number of ways to make change for total,
    under the currency system described by money.

    >>> def chinese_yuan(ith):
    ...     if ith == 1:
    ...         return 1
    ...     if ith == 2:
    ...         return 5
    ...     if ith == 3:
    ...         return 10
    ...     if ith == 4:
    ...         return 20
    ...     if ith == 5:
    ...         return 50
    ...     if ith == 6:
    ...         return 100
    >>> def us_cent(ith):
    ...     if ith == 1:
    ...         return 1
    ...     if ith == 2:
    ...         return 5
    ...     if ith == 3:
    ...         return 10
    ...     if ith == 4:
    ...         return 25
    >>> count_change(15, chinese_yuan)
    6
    >>> count_change(49, chinese_yuan)
    44
    >>> count_change(49, us_cent)
    39
    >>> count_change(49, lambda x: 2 ** (x - 1))
    692
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    biggest = 0
    def largest(total,money,i):
        if money(i)==None:
            return i
        elif total<money(i):
            return i
        else:
            return largest(total,money,i+1)
    biggest = largest(total,money,1)-1#回来的是序号
    def help(total,money,notes):
        if total==0:
            return 1
        if total<0 or notes==0:
            return 0
        else:
            return help(total-money(notes),money,notes)+help(total,money,notes-1)
    ans=help(total,money,biggest)
    return ans
            

 


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n==0:
        return None
    move_stack(n-1,start,6-start-end)
    print_move(start, end)
    move_stack(n-1,6-start-end,end)



def multiadder(n):
    """Return a function that takes N arguments, one (at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    >>> from construct_check import check
    >>> # Make sure multiadder is a pure function.
    >>> check(HW_SOURCE_FILE, 'multiadder',
    ...       ['Nonlocal', 'Global'])
    True
    """
    def add(n,sum):
        if n==0:
            return sum
        return lambda a:add(n-1,sum+a)
    return add(n,0)
        
        



##########################
# Just for fun Questions #
##########################


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))

def Y(f): return (lambda x: x(x))   (lambda x: f(lambda z: x(x)(z)))
def fib_maker(f): 
def number_of_six_maker(f): 


my_fib = Y(fib_maker)
my_number_of_six = Y(number_of_six_maker)

# This code sets up doctests for my_fib and my_number_of_six.

my_fib.__name__ = 'my_fib'
my_fib.__doc__ = """Given n, returns the nth Fibonacci nuimber.

>>> my_fib(0)
0
>>> my_fib(1)
1
>>> my_fib(2)
1
>>> my_fib(3)
2
>>> my_fib(4)
3
>>> my_fib(5)
5
"""

my_number_of_six.__name__ = 'my_number_of_six'
my_number_of_six.__doc__ = """Return the number of 6 in each digit of a positive integer n.

>>> my_number_of_six(666)
3
>>> my_number_of_six(123456)
1
"""

    
