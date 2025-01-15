;;; Lab 10: Stream

;;; Required Problems

(define (filter-stream f s)
  (if (null? s) nil
      (
        if (f (car s))
            (cons-stream  (car s) (filter-stream f (cdr-stream s)))
            (filter-stream f (cdr-stream s)))))
;(define (int first) (cons-stream first (int (+ first 1))))
(define (int first) (cons-stream first (int (+ first 1))))

(define (slice s start end)
  (define (help s start end inx)
    (cond
      ((null? s) '())
      ((< inx start) (help (cdr-stream s) start end (+ inx 1)))
      ((< inx (- end 1)) (cons (car s) (help (cdr-stream s) start end (+ inx 1))))
      ((= inx (- end 1)) (cons (car s) nil))
      (else nil)))
  (help s start end 0))

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))


(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
      nil
      (cons-stream
        (f (car xs) (car ys))
        (combine-with f (cdr-stream xs) (cdr-stream ys)))))


(define factorials 
  (cons-stream 1 (combine-with * factorials (naturals 1)))
)


(define fibs
  (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs) )))
)


(define (exp x) 
 (cons-stream 1 (combine-with + (exp x)
  (combine-with 
  (lambda (b c)(/(expt x c)b));operator
  (cdr-stream factorials);b from it
  (naturals 1);c from it
  )))
)


(define (list-to-stream lst)
  (if (null? lst) nil
      (cons-stream (car lst) (list-to-stream (cdr lst)))))


(define (nondecrease s)
  (define (help s last current)
    (cond
      ((null? s)       
       (if (null? current)
           nil
           (cons-stream current nil)))
      ((null? current)         
       (help (cdr-stream s) (car s) (list (car s))))
      ((<= last (car s))   
       (help (cdr-stream s) (car s) (append current (list (car s)))))
      (else   
      (cons-stream current (help (cdr-stream s) (car s) (list (car s)))))) ;all the expr equal to initial 'result'
      )             
       
  (if (null? s)
  nil
  (help s (car s) '())))


;;; Just For Fun Problems
(define s (list-to-stream '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1)))
(define s (list-to-stream '()))
(slice (nondecrease s) 0 8)
(define (my-cons-stream first second) ; Does this line need to be changed?
  'YOUR-CODE-HERE
)

(define (my-car stream)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)


(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes (sieve (naturals 2)))
