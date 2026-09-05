#Mock Test 02 - NumPy Basic — 30 Questions
#Time: 45 minutes
#Total: 30 marks
#Level: Beginner
#Focus: NumPy basics, arrays, indexing, slicing, shape, dtype, basic operations
import numpy as np

#Part A — MCQ (5 marks)
1. Which function changes the shape of a NumPy array?
A. np.change()
B. np.reshape()
C. np.shape_change()
D. np.resize_array()
Ans: B

#2. What does a.size return?
A. Number of dimensions
B. Shape of the array
C. Total number of elements
D. Data type
Ans: C

#3. Which function calculates the total/sum of array elements?
A. np.total()
B. np.add_all()
C. np.sum()
D. np.plus()
Ans: C

#4. Which function returns the largest value?
A. np.large()
B. np.max()
C. np.high()
D. np.maximum_value()
Ans: B

#5. Which attribute tells you the data type of an array?
A. a.type
B. a.datatype
C. a.dtype
D. a.data
Ans: C

#Part B — Predict the Output (5 marks)
#6.
a = np.array([10, 20, 30, 40, 50])

print(a.sum())

Output: 150

#7.
a = np.array([5, 15, 25, 35])

print(a.max())

Output: 35

#8.
a = np.array([5, 10, 15, 20])

print(a.mean())

Output: 12.5

#9.
a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print(b)

Output: [[1 2 3]
         [4 5 6]]

#10.
a = np.array([[10, 20, 30],
              [40, 50, 60]])

print(a[1, 2])

Output: 60

#Part C — Write Python Code (5 marks)
#11 Create a NumPy array containing: 10, 20, 30, 40, 50 Then print its size using NumPy.
arry = np.array([10, 20, 30, 40, 50])
print(arry.size)

#12 Print the minimum value using NumPy.
arr = np.array([10, 20, 30, 40, 50])
print(arr.min())

#13 Create an array from 1 to 12 and reshape it into 3 rows × 4 columns.
b = np.arange(1, 13).reshape(3, 4)
print(b)

#14
a = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(a[1, 1])
#15
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])