"""
CALC SUM USING MATRIX
sum will calculate the total of each value on the axis provided
axis: 
 - 0 row 
 - 1 column
"""
matrix = numpy.array([
                [5, 10, 15], 
                [20, 25, 30],
                [35, 40, 45]
             ])
    matrix.sum(axis=1)