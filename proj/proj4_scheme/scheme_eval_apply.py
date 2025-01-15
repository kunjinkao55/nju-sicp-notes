import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############
#Call expressions and special forms are represented as Pairs
#env.lookup(expr) finds the value of a name?
#I.   User-defined procedures open a new frame; builtins do not
#II.  Builtins simply execute a predefined function; user-defined
#  procedures must evaluate additional expressions in the body


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    #这一行一直是有效的
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        procedure = scheme_eval(first, env,_)
        #eval operator ；first其实就是operator
        validate_procedure(procedure)
        if isinstance(procedure, MacroProcedure):  # MacroProcedure is not a `pure` string-subst
            thunk = scheme_apply(procedure, rest, env)   # `scheme_apply` can bind expression to variable
            if isinstance(thunk, Unevaluated):
                 return Unevaluated(thunk.expr, thunk.env)
            else:
                return scheme_eval(thunk, env)

        args = rest.map(lambda x: scheme_eval(x, env,_))
        #评估操作数 对rest（后面的列表)进行eval
        return scheme_apply(procedure, args, env)
        # END PROBLEM 3

        
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        lst = []
        while args != nil:
            lst.append (args.first)
            args = args.rest
        if procedure.expect_env:
            lst.append(env)
        try:
            return procedure.py_func(*lst)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
            
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9

        lambdaframe= procedure.env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body, lambdaframe)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        muframe= env.make_child_frame(procedure.formals,args)
        return eval_all(procedure.body, muframe)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions is nil:
        return None 
    if expressions.rest is nil:
        return scheme_eval(expressions.first,env,True)
    else:
        scheme_eval(expressions.first,env)
        return eval_all(expressions.rest,env)
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in environment ENV. If TAIL,
        return a Thunk containing an expression for further evaluation.
        """

        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)
        # tail call

        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        res = original_scheme_eval(expr,env,tail)
        while isinstance(res,Unevaluated):
            #print(scheme_eval is optimize_tail_calls(scheme_eval))
            res = original_scheme_eval(res.expr,res.env,tail)
            #wrong version is 
            # #res = scheme_eval(res.expr,res.env,tail)

            #because 
            #there , scheme_eval is replaced by optimize_tail_calls(scheme_eval)
            #and , the original_scheme_eval is the original(it is an adj. fxxk!) scheme_eval
        return res
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

#here before eval optimize_tail_calls
scheme_eval = optimize_tail_calls(scheme_eval)
