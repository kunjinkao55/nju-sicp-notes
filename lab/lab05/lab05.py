def takeWhile(t, p):
    """Take elements from t until p is not satisfied.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> list(takeWhile(s, lambda x: x == 10))
    [10]
    >>> s2 = iter([1, 1, 2, 3, 5, 8, 13])
    >>> list(takeWhile(s2, lambda x: x % 2 == 1))
    [1, 1]
    >>> s = iter(['a', '', 'b', '', 'c'])
    >>> list(takeWhile(s, lambda x: x))
    ['a']
    >>> list(takeWhile(s, lambda x: x))
    ['b']
    >>> next(s)
    'c'
    """
    for i in t:
        if p(i):
            yield i
        else:
            break
        


def backAndForth(t):
    """Yields and skips elements from iterator t, back and forth.

    >>> list(backAndForth(iter([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    [1, 4, 5, 6]
    >>> list(backAndForth(iter([1, 2, 2])))
    [1]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = backAndForth(naturals())
    >>> [next(m) for _ in range(9)]
    [0, 3, 4, 5, 10, 11, 12, 13, 14]
    """
    a=0
    try:
        while(1):
            a+=1
            if(a % 2 ==1):
                temp=a
                while temp>0:
                    yield next (t)
                    temp-=1
            else:
                temp=a
                while temp>0:
                    next (t)
                    temp-=1
    except StopIteration:
        pass
        
    



        





def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale(iter([1, 5, 2]), 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]
    >>> # generators allow us to represent infinite sequences!!!
    >>> def naturals():
    ...     i = 0
    ...     while True:
    ...         yield i
    ...         i += 1
    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [0, 2, 4, 6, 8]
    """
    itt=map(lambda x:multiplier*x,it)
    yield from itt


def merge(a, b):
    """Merge two generators that are in increasing order and without duplicates.
    Return a generator that has all elements of both generators in increasing
    order and without duplicates.

    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    # x=None
    # for i in a:
    #     if x==None or x < i:
    #         if x !=None:
    #             yield x
    #             x=None
    #         for j in b:
    #             if j<i:
    #                 yield j
    #             elif j==i:
    #                 break
    #             else:
    #                 x=j
    #                 break
    #     yield i
    a1=next(a)
    b1=next(b)
    while True:
        if a1==b1:
            yield a1
            a1=next(a)
            b1=next(b)
        elif a1<b1:
            yield a1
            a1=next(a)
        else:
            yield b1
            b1=next(b)



def hailstone(n):
    """Return a generator that outputs the hailstone sequence.

    >>> for num in hailstone(10):
    ...     print(num)
    10
    5
    16
    8
    4
    2
    1
    """
    while True:
        if n == 1:
            yield n
            return
        yield n
        if n % 2 == 0:
            n=n//2
        else:
            n=3*n+1

    
    
