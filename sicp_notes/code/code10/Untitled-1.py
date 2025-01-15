# 创建树
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches) # [sth] + [ [ ] ] == [ sth , [] ]

# 检查是否为树
def is_tree(tree):
    """检查给定的数据是否为树"""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# 获取树的标签
def label(tree):
    """返回树的标签值"""
    return tree[0]

# 获取树的分支
def branches(tree):
    """返回树的子树列表"""
    return tree[1:]

# 检查是否为叶子节点
def is_leaf(tree):
    """检查树是否为叶子节点"""
    return not branches(tree)
t1=tree(1,[tree(2,[tree(4),tree(7)]),tree(3),tree(5,[tree(6,[tree(8)])])])
def depth(t,v):
    if label(t)==v:
        return 0
    for b in branches(t):
        d=depth(b,v)
        if d is not None:
            return d+1
    return None
print(depth(t1,1),depth(t1,3),depth(t1,8),depth(t1,9))

def max_path(root,k):
    '''return the highest label sum of paths with length no more than k'''
    def helper(t,k,flag):
        
    return helper(t,k,False)