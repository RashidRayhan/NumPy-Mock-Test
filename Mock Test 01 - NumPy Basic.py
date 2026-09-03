#Mock Test 01 - NumPy Basic — 30 Questions
#Time: 45 minutes
#Total: 30 marks
#Level: Beginner
#Focus: NumPy basics, arrays, indexing, slicing, shape, dtype, basic operations

#Part A — MCQ (10 marks)

#1. Which statement correctly imports NumPy?
A. import numpy
B. import np
C. import numpy as np
D. numpy import
Ans: C

#2. Which function creates a NumPy array?
A. np.list()
B. np.array()
C. np.create()
D. np.arr()
ANs: B

#3. What is the output of:
import numpy as np

a = np.array([10, 20, 30])
print(a[1])

A. 10
B. 20
C. 30
D. Error
Ans: B

#4. What is the index of the first element in a NumPy array?
A. 0
B. 1
C. -1
D. 10
Ans: A

#5. Which attribute gives the number of dimensions?
A. a.size
B. a.shape
C. a.ndim
D. a.length
Ans: C

#6. What does a.shape return?
A. Number of elements only
B. Data type
C. Dimensions of the array
D. Memory size
ANs: C

#7. Which creates an array containing zeros?
A. np.zero()
B. np.zeros()
C. np.empty_zero()
D. np.null()
Ans: B

#8. What is the output?
a = np.array([1, 2, 3, 4])
print(a + 10)
A. [11, 12, 13, 14]
B. [1, 2, 3, 4, 10]
C. Error
D. [10, 20, 30, 40]
Ans: A
#9. Which property tells you the number of elements?
A. ndim
B. shape
C. size
D. length
Ans: C

#10. Which function creates a sequence of numbers?
A. np.range()
B. np.arange()
C. np.sequence()
D. np.numbers()
Ans: B

#11. What is the output?
import numpy as np
a = np.array([5, 10, 15, 20])
print(a[0])

#Result: 5

#12
a = np.array([10, 20, 30, 40, 50])
print(a[-1])

#Result: 50
#13
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])
#Result:  [20 30 40]

#14
a = np.array([1, 2, 3])
print(a * 2)
#Result: [2, 4, 6]

#15
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
#Result: [11 22 33]

#16
a = np.array([[1, 2], [3, 4]])
print(a.shape)
#Result [2, 2]

#17
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)
#Result: 2

#18
a = np.arange(1, 6)
print(a)
#Result: [1 2 3 4 5]

#19
a = np.zeros(4)
print(a)
#Result: [0. 0. 0. 0.]

#20
a = np.ones(3)
print(a)
#Result: [1. 1. 1.]

#Part C — Write Python Code (10 marks)

#21. Import NumPy using the standard alias np.
import numpy as np

#22 Create this NumPy array:

arr = np.array([10, 20, 30, 40, 50])
print(arr)

#23. Create an array containing numbers from 1 to 10 using np.arange().
arry =np.arange(1, 11)
print(arry)

#24. Create an array containing five zeros.
zero = np.zeros(5)
print(zero)

#25. Create an array containing five ones.
one = np.ones(5)
print(one)

#26. Create this 2D array:
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

#27. Print the third element of:
item = np.array([10, 20, 30, 40, 50])
print(item[2])

#28. Print the last element of an array.
items = np.array([10, 20, 30, 40, 50])
print(items[-1])

#29. Given:
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])

#30. Given:
a = np.array([10, 20, 30, 40, 50])
print(a.size)