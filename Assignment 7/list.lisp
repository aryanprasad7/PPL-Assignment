; ATHARVA MUKUND JOSHI
; 111803142

;declaring list called as n
(defparameter *n* '(9 8 7 4 1))  
	
	
	
	
;declaring 'listn' function for getting the nth element of a list 	
(defun listn(l f)                          
    (return-from listn (nth (- f 1) l))       
)

;index nth list


;calling the function with a list and an index of the element required
(format t "3rd Item in the List = ~a ~%" (listn *n* 3)) 

