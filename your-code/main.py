#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.version.version)

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))
a

#4. Print a.


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))
b

#6. Print b.



#7. Do a and b have the same size? How do you prove that in Python code?


'Tienen la misma cardinalidad'

#8. Are you able to add a and b? Why or why not?
'No se pueden sumar no tienen la misma cardinalidad'


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.reshape(b, (2,3,5))
c

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = a+c
d
array([[[1.67752708, 1.98495101, 1.68019902, 1.26075628, 1.38254903],
        [1.96080461, 1.75419127, 1.58343362, 1.52338944, 1.12143929],
        [1.91326628, 1.06367518, 1.68982045, 1.22623423, 1.71554117]],

       [[1.79762172, 1.47021665, 1.38929885, 1.20108452, 1.89578344],
        [1.78546989, 1.43255904, 1.29605205, 1.65048646, 1.4979804 ],
        [1.55244051, 1.21249332, 1.94844079, 1.57212456, 1.22120639]]])

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
'ls valores de 'a'  don floats y los valores de 'd' es la suma de 'c', que eran numeros enteros, y 'a' '
#12. Multiply a and c. Assign the result to e.
e = a*c
e
1
e = a*c
2
e
array([[[0.67752708, 0.98495101, 0.68019902, 0.26075628, 0.38254903],
        [0.96080461, 0.75419127, 0.58343362, 0.52338944, 0.12143929],
        [0.91326628, 0.06367518, 0.68982045, 0.22623423, 0.71554117]],

       [[0.79762172, 0.47021665, 0.38929885, 0.20108452, 0.89578344],
        [0.78546989, 0.43255904, 0.29605205, 0.65048646, 0.4979804 ],
        [0.55244051, 0.21249332, 0.94844079, 0.57212456, 0.22120639]]])

#13. Does e equal to a? Why or why not?
''' Si es equivalentes 'a'  a 'e' por que solo se multiplica por valores de '1'

array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
'''




#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
'''
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("El valor maximo de 'd' es: ", d_max)
print("El valor minimo de 'd' es: ", d_min)
print("El promedio de 'd' es: ", d_mean)'''


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
"""
for primer_arreglo in f:
    for segundo_arreglo in primer_arreglo:
        for tercer_arreglo in segundo_arreglo:
            if tercer_arreglo > d_min and tercer_arreglo < d_mean:
                tercer_arreglo = 25
array([[[ 4.24399158e-314,  0.00000000e+000,  0.00000000e+000,
          0.00000000e+000,  0.00000000e+000],
        [ 0.00000000e+000,  0.00000000e+000,  0.00000000e+000,
          0.00000000e+000,  0.00000000e+000],
        [ 0.00000000e+000, -8.15824090e-311,  2.95929617e+203,
          3.98576416e-038,  6.01334510e-154],
        [-1.25635059e-310,  4.62857235e-072,  1.05963508e-153,
          2.95967890e+203,  2.61211041e-033]],

       [[ 6.01334510e-154,  6.01347002e-154,  3.03338118e-067,
         -8.79059753e-311,  4.24399158e-314],
        [ 0.00000000e+000,  0.00000000e+000,  0.00000000e+000,
          0.00000000e+000,  0.00000000e+000],
        [ 0.00000000e+000,  0.00000000e+000,  0.00000000e+000,
          0.00000000e+000,  0.00000000e+000],
        [-9.48024571e-311,  6.32264832e+233,  1.02215496e-234,
          4.14647719e+185, -1.43481042e-310]]])

"""

#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

d[(np.where((d > d_min) & (d < d_mean)))]


array([1.26075628, 1.38254903, 1.52338944, 1.12143929, 1.22623423,
       1.47021665, 1.38929885, 1.20108452, 1.43255904, 1.29605205,
       1.4979804 , 1.21249332, 1.22120639])
"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""