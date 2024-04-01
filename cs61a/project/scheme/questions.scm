(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (cond
  ((null? rests) nil)
  (else (cons (cons first (car rests)) (cons-all first (cdr rests)))))
)

(define (zip pairs)
  (cond
  ((null? pairs) (list nil nil))
  (else (list (map car pairs) (map cadr pairs)))
  )
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper s i)
    (cond
      ((null? s) nil)
      (else (cons (cons i (cons (car s) nil)) (helper (cdr s) (+ 1 i))))
    )
  )
  (helper s 0)
  )

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((null? denoms) nil)
    ((= total 0) (list nil))
    ((> (car denoms) total) (list-change total (cdr denoms)))
    (else (append (cons-all (car denoms)
      (list-change (- total (car denoms)) denoms))
      (list-change total (cdr denoms))))
    )
  )

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr
         )
        ((quoted? expr)
         expr
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           (cons form (cons params (map let-to-lambda body)))
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           (cons (cons 'lambda (cons (car (zip values)) (map let-to-lambda body)))
           (map let-to-lambda (cadr (zip values))))
           ))
        (else
         (map let-to-lambda expr)
         )))
