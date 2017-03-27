"""
CALCULATING SUM OF SPECIFIC DATA IN A MATRIX
- Creates 2 comparisons, one for empty and one for Canada, 1986
- Gets all the rows in matrix in both Canada and 1986
- Retrives column 5 from all rows
- Assigns empty string values to 0
- Transforms vector into float
- Calculates the sum of the vector
"""
empty_comp = (canada_alcohol == '')
canada_1986_comp = (world_alcohol[:, 0] == '1986') & (world_alcohol[:, 2] == 'Canada')
canada_1986 = world_alcohol[canada_1986_comp, :]

canada_alcohol = canada_1986[:, 4]
canada_alcohol[empty_comp] = 0
canada_alcohol = canada_alcohol.astype(float)

total_canadian_drinking = canada_alcohol.sum()