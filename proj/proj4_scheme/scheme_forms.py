from scheme_eval_apply import *
from scheme_utils import *
from scheme_classes import *
from scheme_builtins import *

#################
# Special Forms #
#################

# Each of the following do_xxx_form functions takes the cdr of a special form as
# its first argument---a Scheme list representing a special form without the
# initial identifying symbol (if, lambda, quote, ...). Its second argument is
# the environment in which the form is to be evaluated.


def do_define_form(expressions, env):
    """Evaluate a define form.
    >>> env = create_global_frame()
    >>> do_define_form(read_line("(x 2)"), env) # evaluating (define x 2)
    'x'
    >>> scheme_eval("x", env)
    2
    >>> do_define_form(read_line("(x (+ 2 8))"), env) # evaluating (define x (+ 2 8))
    'x'
    >>> scheme_eval("x", env)
    10
    >>> # problem 10
    >>> env = create_global_frame()
    >>> do_define_form(read_line("((f x) (+ x 2))"), env) # evaluating (define (f x) (+ x 8))
    'f'
    >>> scheme_eval(read_line("(f 3)"), env)
    5
    """
    validate_form(expressions, 2)  # Checks that expressions is a list of length at least 2
    signature = expressions.first
    if scheme_symbolp(signature):
        # assigning a name to a value e.g. (define x (+ 1 2))
        validate_form(expressions, 2, 2)  # Checks that expressions is a list of length exactly 2
        # BEGIN PROBLEM 4
        env.define(signature, scheme_eval(expressions.rest.first, env))
        return signature
        # END PROBLEM 4
    elif isinstance(signature, Pair) and scheme_symbolp(signature.first):
        # defining a named procedure e.g. (define (f x y) (+ x y))
        # BEGIN PROBLEM 10
        # signature == (f x y) (symbol), formals, and body.
        symbol = signature.first#名称
        formals = signature.rest#形参
        body = expressions.rest#函数体
        validate_formals(formals)
        lambdaprocedure = LambdaProcedure(formals,body,env)
        env.define(symbol, lambdaprocedure)
        return symbol
        # END PROBLEM 10
    else:
        bad_signature = signature.first if isinstance(signature, Pair) else signature
        raise SchemeError('non-symbol: {0}'.format(bad_signature))


def do_quote_form(expressions, env):
    """Evaluate a quote form.

    >>> env = create_global_frame()
    >>> do_quote_form(read_line("((+ x 2))"), env) # evaluating (quote (+ x 2))
    Pair('+', Pair('x', Pair(2, nil)))
    """
    #2) Pair(A, nil), where:
    #  A is the quoted expression
    validate_form(expressions, 1, 1)
    # BEGIN PROBLEM 5
    return expressions.first
    # END PROBLEM 5


def do_begin_form(expressions, env):
    """Evaluate a begin form.

    >>> env = create_global_frame()
    >>> x = do_begin_form(read_line("((print 2) 3)"), env) # evaluating (begin (print 2) 3)
    2
    >>> x
    3
    """
    validate_form(expressions, 1)
    return eval_all(expressions, env)


def do_lambda_form(expressions, env):
    """Evaluate a lambda form.

    >>> env = create_global_frame()
    >>> do_lambda_form(read_line("((x) (+ x 2))"), env) # evaluating (lambda (x) (+ x 2))
    LambdaProcedure(Pair('x', nil), Pair(Pair('+', Pair('x', Pair(2, nil))), nil), <Global Frame>)
    """
    validate_form(expressions, 2)
    formals = expressions.first#参数列表
    validate_formals(formals)
    # BEGIN PROBLEM 7
    #LambdaProcedure(formals, lambda_proc.body, <Global Frame>)
    return LambdaProcedure( formals, expressions.rest, env)
    # END PROBLEM 7


def do_if_form(expressions, env):
    """Evaluate an if form.

    >>> env = create_global_frame()
    >>> do_if_form(read_line("(#t (print 2) (print 3))"), env) # evaluating (if #t (print 2) (print 3))
    2
    >>> do_if_form(read_line("(#f (print 2) (print 3))"), env) # evaluating (if #f (print 2) (print 3))
    3
    """
    validate_form(expressions, 2, 3)
    if is_scheme_true(scheme_eval(expressions.first, env)):
        return scheme_eval(expressions.rest.first, env,True)
    elif len(expressions) == 3:
        return scheme_eval(expressions.rest.rest.first, env,True)

notflag = False
def do_and_form(expressions, env):
    """Evaluate a (short-circuited) and form.

    >>> env = create_global_frame()
    >>> do_and_form(read_line("(#f (print 1))"), env) # evaluating (and #f (print 1))
    False
    >>> # evaluating (and (print 1) (print 2) (print 4) 3 #f)
    >>> do_and_form(read_line("((print 1) (print 2) (print 3) (print 4) 3 #f)"), env)
    1
    2
    3
    4
    False
    """
    # BEGIN PROBLEM 12
    validate_form(expressions, 0)  # and can have 0 or more expressions
    current = expressions
    result = True  # Initialize to True for the case of empty expressions

    while current is not nil:
        
        if current.rest is nil:
            result = scheme_eval(current.first,env,True)
        else:
            result = scheme_eval(current.first, env)
        if  is_scheme_false(result):
            return result  # Return immediately if any expression evaluates to #f

        current = current.rest

    return result
    # END PROBLEM 12


def do_or_form(expressions, env):
    """Evaluate a (short-circuited) or form.

    >>> env = create_global_frame()
    >>> do_or_form(read_line("(10 (print 1))"), env) # evaluating (or 10 (print 1))
    10
    >>> do_or_form(read_line("(#f 2 3 #t #f)"), env) # evaluating (or #f 2 3 #t #f)
    2
    >>> # evaluating (or (begin (print 1) #f) (begin (print 2) #f) 6 (begin (print 3) 7))
    >>> do_or_form(read_line("((begin (print 1) #f) (begin (print 2) #f) 6 (begin (print 3) 7))"), env)
    1
    2
    6
    """
    # BEGIN PROBLEM 12
    validate_form(expressions, 0) 
    current = expressions
    result = False  # Initialize to True for the case of empty expressions

    while current is not nil:
        if current.rest is nil:
            result = scheme_eval(current.first,env,True)
        else:
            result = scheme_eval(current.first, env)
        if  is_scheme_true(result):
            return result  # Return immediately if any expression evaluates to #f

        current = current.rest

    return result
    # END PROBLEM 12


def do_cond_form(expressions, env):
    """Evaluate a cond form.

    >>> do_cond_form(read_line("((#f (print 2)) (#t 3))"), create_global_frame())
    3
    """
    while expressions is not nil:
        clause = expressions.first# clouse is first condition
        validate_form(clause, 1)
        if clause.first == 'else':
            test = True
            if expressions.rest != nil:
                raise SchemeError('else must be last')
        else:
            test = scheme_eval(clause.first, env)
        if is_scheme_true(test):
            # BEGIN PROBLEM 13

            if clause.rest == nil:
                return test#条件后面没有返回值 返回 #t
            return eval_all(clause.rest,env) #返回条件返回值的eval结果
            # END PROBLEM 13
        expressions = expressions.rest


def do_let_form(expressions, env):
    """Evaluate a let form.

    >>> env = create_global_frame()
    >>> do_let_form(read_line("(((x 2) (y 3)) (+ x y))"), env)
    5
    """
    validate_form(expressions, 2)
    let_env = make_let_frame(expressions.first, env)
    return eval_all(expressions.rest, let_env)


def make_let_frame(bindings, env):
    """Create a child frame of Frame ENV that contains the definitions given in
    BINDINGS. The Scheme list BINDINGS must have the form of a proper bindings
    list in a let expression: each item must be a list containing a symbol
    and a Scheme expression."""
    if not scheme_listp(bindings):
        raise SchemeError('bad bindings list in let form')
    names = values = nil
    # BEGIN PROBLEM 14
    while bindings != nil:
        validate_form(bindings.first,2,2)
        if(scheme_symbolp(bindings.first.rest.first)):
            env.lookup(bindings.first.rest.first)
        names = Pair(bindings.first.first,names)
        values = Pair(scheme_eval(bindings.first.rest.first,env),values)
        #使用scheme_eval把表达式算出值，使得绑定到name上的value一定是一个最简形式
        #这里相当于把先输入的放到pair的尾部了，不过let绑定不关心顺序，所以这样是无关紧要的
        bindings = bindings.rest
    validate_formals(names)
    new_env = env.make_child_frame(names, values)
    # END PROBLEM 14
    return new_env
#所有let子式都在parent中绑定
#调用时env是临时作用域
#应该开一个新的env，把所有绑定值加进去
#加入的时候如果已经存在同名symbal，error
#每个子式只有两个元素
#辨析一下修改attribute 和创建新 attribute 在.next=    中的行为

def do_define_macro(expressions, env):
    """Evaluate a define-macro form.

    >>> env = create_global_frame()
    >>> do_define_macro(read_line("((f x) (car x))"), env)
    'f'
    >>> scheme_eval(read_line("(f (1 2))"), env)
    1
    """
    # BEGIN PROBLEM OPTIONAL_2
    "*** YOUR CODE HERE ***"
    # END PROBLEM OPTIONAL_2


def do_quasiquote_form(expressions, env):
    """Evaluate a quasiquote form with parameters EXPRESSIONS in
    Frame ENV."""
    def quasiquote_item(val, env, level):
        """Evaluate Scheme expression VAL that is nested at depth LEVEL in
        a quasiquote form in Frame ENV."""
        if not scheme_pairp(val):
            return val
        if val.first == 'unquote':
            level -= 1
            if level == 0:
                expressions = val.rest
                validate_form(expressions, 1, 1)
                return scheme_eval(expressions.first, env)
        elif val.first == 'quasiquote':
            level += 1

        return val.map(lambda elem: quasiquote_item(elem, env, level))

    validate_form(expressions, 1, 1)
    return quasiquote_item(expressions.first, env, 1)


def do_unquote(expressions, env):
    raise SchemeError('unquote outside of quasiquote')


#################
# Dynamic Scope #
#################

def do_mu_form(expressions, env):
    """Evaluate a mu form."""
    validate_form(expressions, 2)
    formals = expressions.first
    validate_formals(formals)
    # BEGIN PROBLEM 11
    return MuProcedure( formals, expressions.rest)
    # END PROBLEM 11


SPECIAL_FORMS = {
    'and': do_and_form,
    'begin': do_begin_form,
    'cond': do_cond_form,
    'define': do_define_form,
    'if': do_if_form,
    'lambda': do_lambda_form,
    'let': do_let_form,
    'or': do_or_form,
    'quote': do_quote_form,
    'define-macro': do_define_macro,
    'quasiquote': do_quasiquote_form,
    'unquote': do_unquote,
    'mu': do_mu_form,
}
