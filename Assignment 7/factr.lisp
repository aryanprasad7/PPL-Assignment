; ATHARVA MUKUND JOSHI
; 111803142

;function 'factorial' for getting factorial of a number using recursion
(defun factorial (n)
    (cond
        ((= n 0) 1) ;; Special case, 0! = 1
        ((= n 1) 1) ;; Base case, 1! = 1
        (t
            ;; Recursive case
            ;; Multiply n by the factorial of n - 1.
            (* n (factorial (- n 1)))
            ;n * factorial(n-1)
        )
    )
)



; calling function factorial for checking its working
; calculated the factorial of 5 (= 120)
(format t "~a ~%"(factorial 5))
