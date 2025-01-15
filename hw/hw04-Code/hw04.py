""" Homework 4: Data Abstraction and Trees"""

from ADT import tree, label, branches, is_leaf, print_tree, copy_tree


#####################
# Required Problems #
#####################

# Problem 1
def couple(lst1, lst2):#AXB
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    ans1= [([lst1[i]]+[lst2[i]])for i in range(0,len(lst1))]
    return ans1


# Problem 2
# The constructor and selectors of the arm
def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]


def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'


def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]


def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]


def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]


def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'


def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]


def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# Problem 2.1
def planet(size):
    """Construct a planet of some size.

    >>> planet(5)
    ['planet', 5]
    """
    assert size > 0
    return['planet',size]


def size(w):
    """Select the size of a planet.

    >>> p = planet(5)
    >>> size(p)
    5
    """
    assert is_planet(w), 'must call size on a planet'
    return w[1]


def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

# examples and usage
def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return m[1]
    return total_weight(end(left(m)))+total_weight(end(right(m)))

# Problem 2.2
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    assert is_mobile(m)
    if not total_weight(end(left(m)))*length(left(m))==total_weight(end(right(m)))*length(right(m)):
        return False
    if is_planet(end(left(m))) and is_planet(end(left(m))):
         return True
    elif is_planet(end(left(m))) and not is_planet(end(right(m))):
        return balanced(end(right(m))) 
    elif not is_planet(end(left(m))) and  is_planet(end(right(m))):
        return balanced(end(left(m)))
    else:
        return  balanced(end(left(m))) and  balanced(end(right(m))) 

# Problem 2.3
def totals_tree(m):
    """Return a tree representing the mobile/planet with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    assert is_mobile(m) or is_planet(m)
    if is_planet(m):
        return tree(total_weight(m))
    else:#不是planet
        return tree(total_weight(m),[totals_tree(end(left(m))),totals_tree(end(right(m)))])

# Problem 3.1
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1)+label(t2))
    elif is_leaf(t1) and not is_leaf(t2):
        return tree(label(t1)+label(t2),branches(t2))
    elif not is_leaf(t1) and  is_leaf(t2):
        return tree(label(t1)+label(t2),branches(t1))
    else:#两边都是树枝
        len1=len(branches(t1))
        len2=len(branches(t2))
        tempbranches=[]
        if len1>=len2:
            for i in range (0,len2):
                tempbranches.append((add_trees(copy_tree(branches(t1)[i]),copy_tree(branches(t2)[i]))))
            for i in range (len2,len1):
                tempbranches.append(copy_tree(branches(t1)[i]))
        else:
            for i in range (0,len1):
                tempbranches.append((add_trees(copy_tree(branches(t1)[i]),copy_tree(branches(t2)[i]))))
            for i in range (len1,len2):
                tempbranches.append(copy_tree(branches(t2)[i]))
        return tree(label(t1)+label(t2),tempbranches)



    

# Problem 3.2
def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    def count_paths(t, n, pathvalue):
        num1=0
    #遍历所有路径
    #每次往下多试一步，大于等于n就返回子路径数量+1，否则接着试探
        pathvalue+=label(t)
        temp1=0        
        if pathvalue>=n:
            num1+=1
        if is_leaf(t):
            return num1
        for i in branches(t): 
            temp1+= count_paths(i,n,pathvalue)
        num1+=temp1
        return num1
    return count_paths(t,n,0)   

# Problem 3.3
def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    ans=bigpath(t,n)
    for d in branches(t):
        ans += bigger_path(d,n) 
    return ans




# Problem 3.4
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    
    def count_paths(t, word, pathvalue):
        pathvalue+=label(t)       
        if pathvalue==word:
            return True
        for i in branches(t): 
          if (count_paths(i, word, pathvalue)):#这也是一种表示或的逻辑吗
              return True
        return False
    ans=count_paths(t,word,'')
    if ans !=True:
        ans=False
    return ans  


##########################
# Just for fun Questions #
##########################

# Problem 4
def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def has_path_fold(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path_fold(greetings, 'h')
    True
    >>> has_path_fold(greetings, 'i')
    False
    >>> has_path_fold(greetings, 'hi')
    True
    >>> has_path_fold(greetings, 'hello')
    True
    >>> has_path_fold(greetings, 'hey')
    True
    >>> has_path_fold(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')
