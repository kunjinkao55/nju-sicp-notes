;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
(
  if (= total 0)
    '(())
    (if (or (< total 0) (= biggest 0))
    '()
    (append
      (map (lambda (sublist) (cons biggest sublist))
           (make-change (- total biggest) biggest))
      (make-change total (- biggest 1))))))

(define (find n lst)
    (define (help n lst inx)
    (
     if(= (car lst) n)
     inx
     (help n (cdr lst) (+ 1 inx))
    ) 
    )
  (help n lst 0)
)



(define (find-nest n sym)
  (let ((value (eval sym))) 
       (cond
         ((and (not (pair? (car value))) (= n (car value))) 
          `(car ,sym)) 
         ((pair? (car value)) 
          (let ((car-result (find-nest n `(car ,sym)))) 
            car-result))
         (
          (let ((cdr-result (find-nest n `(cdr ,sym)))) 
            cdr-result))))
         )




(define-macro (my/or operands)
  (cond 
    ((null? operands) #f)
    (else
      `(let ((t ,(car operands)))
         (if t
             t
             (my/or ,(cdr operands))
             )))))
             
(define-macro (my/and operands)
  (cond 
    ((null? operands) #t)
    ((null? (cdr operands)) (car operands))
    (else
      `(
         if (car ',operands)
             (my/and ,(cdr operands))
             #f))))

(define-macro (k-curry fn args vals indices)
  ''YOUR-CODE-HERE
)


(define-macro (let* bindings expr)
  (if (null? bindings)
      `(let () ,expr) 
      (let ((name (car (car bindings)))   
            (value (car (cdr (car bindings))))) 
        (let ((rest-bindings (cdr bindings))) 
          `(let ((,name ,value))         
             (let* ,rest-bindings ,expr)))))) 

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)