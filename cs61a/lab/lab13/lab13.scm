; Lab 13: Final Review

; Q2
(define (rle s)
(define (track-run elem st len)
  (cond ((null? st) (cons-stream (list elem len) nil))
        ((= elem (car st)) (track-run elem (cdr-stream st) (+ len 1)))
        (else (cons-stream (list elem len) (rle st))))
)
(if (null? s)
    nil
    (track-run (car s) (cdr-stream s) 1))
)

; Q2 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q3
(define (tail-replicate x n)
(define (helper n so-far)
  (if (= n 0) so-far
    (helper (- n 1) (cons x so-far))))
(helper n '())
)
