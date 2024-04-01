; Q1
(define (sign x)
  'YOUR-CODE-HERE
  (cond
  ((> x 0) 1)
  ((< x 0) -1)
  (else 0))
)

; Q2
(define (square x) (* x x))

(define (pow b n)
(cond
( (= n 0)  1 )
( (even? n)  (square (pow b (/ n 2) ) ) )
( (odd? n) (* b (pow b (- n 1) ) ) )
)
)

; Q3
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

; Q4
(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
  ( (or (null? s) (null? (cdr s))) #t)
  (else (and (<= (car s) (cadr s)) (ordered? (cdr s))))
)
)

; Q5
(define (nodots s)
  'YOUR-CODE-HERE
  (define (dotpar s)
    (and (pair? s)
          (not
              (or (pair? (cdr s)) (null? (cdr s)) )
          )
    )
  )
  (cond ((null? s) s)
        ((dotpar s) (list (nodots (car s)) (cdr s)))
        ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
        (else s)
        )
)

; Q6
(define (empty? s) (null? s))

(define (add s v)
    'YOUR-CODE-HERE
    (cond ((empty? s) (list v))
          ((= (car s) v) s)
          ((> (car s) v) (cons v s))
          ((< (car s) v) (cons (car s) (add (cdr s) v)) )
    )
)

; Q7
; Sets as sorted lists
(define (contains? s v)
    'YOUR-CODE-HERE
    (cond ((empty? s) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v))
    )
)

; Q8
(define (intersect s t)
    'YOUR-CODE-HERE
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t)))
    )
)

(define (union s t)
    'YOUR-CODE-HERE
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
    )
)
