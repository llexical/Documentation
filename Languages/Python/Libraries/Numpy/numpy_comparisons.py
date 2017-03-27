import numpy;

"""
SINGLE COMPARISON
makes a comparison: second column == 25
prints the row where the second column is 25
"""
matrix = numpy.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
second_column_25 = (matrix[:, 1] == 25)
print(matrix[second_column_25, :])

"""
SINGLE COMPARISON
Makes a comparison: third column (country) is 'Algeria'
Assigns all rows where the country is Algeria to country_algeria
"""
country_is_algeria = world_alcohol[:, 2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria, :]

"""
MULTIPLE COMPARISON
Makes a comparison: first column is 1986 and country (3rd column) is 'Algeria'
Selects all the rows where the country is Algeria and year is 1986
"""
is_algeria_and_1986 = (world_alcohol[:, 0] == "1986") & (world_alcohol[:, 2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

"""
REPLACING VALUES BY COMPARISON
Makes a comparison: year is 1986
Updates world_alcohol so that any rows with the year 1986
will have the year value replaced with 2014
"""
year_comp = world_alcohol[:, 0] == "1986"
world_alcohol[year_comp, 0] = "2014"

"""
REPLACING VALUES BY COMPARISON
Replaces all empty values in the 5th column with 0
"""
is_value_empty = world_alcohol[:, 4] == ''
world_alcohol[is_value_empty, 4] = 0
