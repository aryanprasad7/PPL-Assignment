; ATHARVA MUKUND JOSHI
; 111803142

;function'factorials' for gettting factorial of a number without recursion
(defun factorials(n)
    (defvar *m* 1)                        ;variable m
    (loop for x from 1 to n               ; looping 
	    do(setf *m* (* *m* x))	  ;updating the value of m after every call						
    )              
    (return-from factorials *m*)          ; returning the value
)
;m setf (m * x)

;calling function factorials for checking its working
(format t "~a ~%"(factorials 9))
