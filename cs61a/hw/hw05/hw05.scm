;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Mutable functions in Scheme

(define (make-fib)
  (define curr 0) (define next 1)
  'YOUR-CODE-HERE
  (define (fib)
    (define temp curr)
    (define temp2 (+ next curr))
    (set! curr next)
    (set! next temp2)
    temp)
    fib
  )
