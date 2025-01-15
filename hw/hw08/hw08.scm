;;; HW08: Scheme

;;; Required Problems

(define (square x) (* x x))

(define (pow base exp)
  (
    if(= exp 0) 1 (if(= exp 1) base
    (
    if(odd? exp) 
    (* base (square (pow base (/ (- exp 1 ) 2) )))
    (square (pow base (/ exp 2))))
    )
  )
)
 ;every num pow 0 eq 1,pow 1 eq itself

(define (filter-lst fn lst)
  (
    if (null? lst);judge if already finish?use null?
    nil
    (
      if(fn (car lst))
    (cons
     (car lst) (filter-lst fn (cdr lst))) 
    (filter-lst fn (cdr lst))
    )
    )
)


(define (no-repeats s)
  (if (null? s)
      s

      (
        cons 
          (car s)
          (no-repeats 
              (filter-lst 
                    (lambda (x) (not (= (car s) x)))   
                    s
              )
          )
      )
  )
)
(define (substitute s old new)
(
  if(null? s)
   s
    (
      if(pair? (car s))
       (cons (substitute (car s) old new) (substitute (cdr s) old new))
      (if(eq? old (car s))
    (cons new (substitute (cdr s) old new)) 
    (cons (car s) (substitute (cdr s) old new) )
    )
    )
)
)


(define (sub-all s olds news)
;return value: s with all olds be took placed by news
  (
    if (null? olds)
    s
    ;old is empty and these is nothing to do
    (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
    ;use sub-all,but old_first_word has be replaced
  )
)

(define (tree label branches)
    (cons label branches);holy shit so simple ,because branches is already a list,look down!
)

(define (label t)
  (
    car t
  )
)

(define (branches t)
  (
    cdr t
  )
)

(define (is-leaf t)
  (
    if(null? (branches t))
    #t
    #f
  )
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
          (tree 6 (list
            (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))


(define (label-sum t)
  (
    if(is-leaf t)
    (label t)
    (+ (label t) (apply + (map label-sum (branches t)))) ;the return value of map still a list,using apply to sum all elem in the given list
  )
)


;;; Just for fun Problems

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))
(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  'YOUR-CODE-HERE
)

(define (derive-product expr var)
  'YOUR-CODE-HERE
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
)

(define (exp? exp)
  'YOUR-CODE-HERE
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  'YOUR-CODE-HERE
)
