;; Lab 7: Scheme ;;

; Q2
(define (over-or-under x y)
  'YOUR-CODE-HERE
  (cond
        ((> x y) 1)
        ((< x y) -1)
        (else 0)
      )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q3
(define (make-adder num)
  'YOUR-CODE-HERE
  (lambda (x) (+ x num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13
