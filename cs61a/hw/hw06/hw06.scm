;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Streams

(define (find s predicate)
  'YOUR-CODE-HERE
  (if (null? s) #f
  (if (eq? (predicate (car s)) #t) (car s)
  (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  'YOUR-CODE-HERE
  (cond
  ((null? s)())
  (else (cons-stream (* k (car s)) (scale-stream (cdr-stream s) k))))
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? (car curr) seen-so-far) #t)
          (else (pair-tracker (cons-stream (car curr) seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker nil s)
)

(define (contains? lst s)
  'YOUR-CODE-HERE
  (if (null? s) #f
  (if (eq? lst (car s)) #t
  (contains? lst (cdr-stream s))))
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)

; Tail recursion

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (= n 0) start
  (if (= n 1) (combiner start (term n))
  (accumulate combiner (combiner start (term n))  (- n 1) term))))
  )
)

; Macros

(define-macro (list-of expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
  (list 'map (list 'lambda (list var) expr)
  (list 'filter (list 'lambda (list var) filter-expr) lst)
   )
)
