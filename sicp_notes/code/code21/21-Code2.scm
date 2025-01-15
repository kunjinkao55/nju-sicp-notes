; Demo 4
> (define (double expr)
	(begin expr expr))
double
> (double (print 2))
2
; (print 2) returns nonetype value
; try ((print 2) 1)

> (define (double expr)
	(list 'begin expr expr))
> (double '(print 2))
(begin (print 2) (print 2))
> (eval (double '(print 2)))
2
2
; but I do not want to call 'eval'
; and quote input, then what can we do?

> (define-macro (double expr)
	(list 'begin expr expr))
> (double (print 2))
2
2

; Demo 5
> (define x (+ x (+ 1 2)))
x
; can draw the above expression using '(define x (+ x (+ 1 2))),
; to see the list structure
> (define-macro (add-to var expr)
	(list 'define var (list '+ var expr)))
add-to
> (define x 1)
> (add-to x (+ 2 3))
x
> x
6

; Demo 6
> (map (lambda (x) (* x x)) '(1 2 3 4))
(1 4 9 16)
> (draw '(map (lambda (x) (* x x)) '(1 2 3 4)))
; write the for loop macro based on the list figure above
> (define-macro (for var in lst do expr)
	(list 'map (list 'lambda (list var) expr) lst))
for
> (for x in '(1 2 3 4) do (* x x))
(1 4 9 16)

; Demo 7
> `(x y z); equivalent to '(x y z)
(x y z)
> (define x 2)
> `(x y z)
(x y z)
> `(,x y z)
(2 y z)

> (define-macro (for var in lst do expr)
	'(map (lambda (var) expr) lst)); wanted but not work
	`(map (lambda (,var) ,expr) ,lst); works using quasi
