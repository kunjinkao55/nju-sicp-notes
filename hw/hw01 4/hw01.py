""" Homework 1: Variables & Functions, Control """

from operator import add, sub, mul, neg

def a_sub_abs_b(a, b):
    r"""Return a-abs(b), but without calling abs.

    >>> a_sub_abs_b(2, 3)
    -1
    >>> a_sub_abs_b(2, -3)
    -1
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_sub_abs_b), re.M)
    ['return h(a, b)']
    """
    return h(a, b)
def h(a,b):
     if (b >= 0):
        h = a-b
     else:
        h = a+b
     return h

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two largest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return max(x**2+y**2, x**2+z**2, y**2+z**2)

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    i=0
    while(True):
        i=i+1
        if (x%i==0 and i!=1 and i!=x):
            m=x//i
            return m
        if(i==x):
            m=x
            return 1

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():#语句
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()
#直接执行，但是他的函数体和另一个函数调用的那个是一样的
#区别在于被调用的那个函数吧
def with_if_function():#函数调用时不管条件是否满足，都要完整读取一边被调用函数的全部内容，如果这时候函数有副作用，不管条件是否满足，副作用都会被执行
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())
#调用另外一个函数
def c():
    False

def t():
   print(1)

def f():
    print(2)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(x)
    num=1
    while(x!=1):
        if(x%2==0):
            x=x//2
        else:
            x=3*x+1
        print(x,end="\n")
        num=num+1
    return num
     

def double_factorial(n):
    """Compute the double factorial of n.

    >>> double_factorial(6)  # 6 * 4 * 2
    48
    >>> double_factorial(5)  # 5 * 3 * 1
    15
    >>> double_factorial(3)  # 3 * 1
    3
    >>> double_factorial(1)  # 1
    1
    """
    fac=1
    while(n>=0):
        if(n==0):
            return fac
        fac=fac*n
        n=n-2
    return fac

def double_ones(n):
    """Return true if n has two ones in a row.
    
    >>> double_ones(1)
    False
    >>> double_ones(11)
    True
    >>> double_ones(2112)
    True
    >>> double_ones(110011)
    True
    >>> double_ones(12345)
    False
    >>> double_ones(10101010)
    False
    """
    "*** YOUR CODE HERE ***"
    str_n=str(n)
    if(n==1):
        return False
    i=0
    range_n=len(str_n)
    while(i<range_n):
        if (str_n[i]=='1' and str_n[i+1]=='1'):
            return True
        i=i+1
    return False
            
           

