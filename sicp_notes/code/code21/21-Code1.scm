; Demo 1

> (define x 2)
x
> 'x ;preventing evaluating
x
> x
2
> (eval 'x)
2
> '(+ 1 2 3)
(+ 1 2 3)
> (eval '(+ 1 2 3))
6
> '(if (= x 2) 5 6)
(if (= x 2) 5 6)
> (eval '(if (= x 2) 5 6))
5
> 'quotient
quotient
> quotient
#[quotient] ;built-in procedure
> (list quotient 10 2)
(#[quotient] 10 2)
> (eval (list 'quotient 10 2))
5
> (eval '(quotient 10 2))
5
> (list '+ x 2)
(+ 2 2)
> (list '+ 'x 2)
(+ x 2)

; Demo 2
> (define and-expr '(and 5 (= 7 8) 9))
and-expr
> and-expr
(and 5 (= 7 8) 9)
> (eval and-expr)
#f

(define-macros)


> (define (make-and-expr e1 e2)
              (list 'and e1 e2))
make-and-expr
> (make-and-expr #f #t)
(and #f #t)
> (eval (make-and-expr #f #t))
#f
> (eval (make-and-expr (= 1 0) (/ 1 0)))
#f
> (define (fact-expr n)
	    (if (= n 0)
		1
		(list '* n (fact-expr (- n 1)))))
fact-expr
> (fact-expr 5)
(* 5 (*4 (* 3 (* 2 (* 1 1)))))
> (eval (fact-expr 5))
120

; Demo 3
; The following two usages are different from
; 'begin' special-form expression

> (let ((a 1) (b (+ a 1))) (+ a b))
Error: unknown identifier a 
; (the bindings are done in parallel)
; like in Python a, b = 1, a + 1 error too
> (let ((a 1) (b 2) (+ a b)))
2
> b
Error: unknown identifier b
; (outside of let expression, b not visible)
> (begin (define a 1) (define b 2) (+ a b))
3
> b
2

