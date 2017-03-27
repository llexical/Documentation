import pandas

dataframe = pandas.import_csv("csvhere.csv");

# selects the first 5 rows by default
dataframe.head(<int rows:opt>)
# selects the last 5 rows by default
dataframe.tail(<int rows:opt>)

# get dataframe length
dataframe.shape[0]

# Selecting rows
dataframe.loc[<int row>]
dataframe.loc[23]; # get single row
dataframe.loc[3:6] # get the rows between & uncluding 3 & 6
dataframe.loc[[1,34,5]] # gets the rows by index in the array (1, 34, 5)
dataframe.loc[(dataframe.shape[0] - 5), dataframe.shape[0]] # getting the last 5 rows, version: retarded method.

# Selecting columns
dataframe[<any column>]
dataframe["label"]
dataframe[["label1", "label2"]]

# Selecting columns that meet a condition
columns = food_info.columns.tolist()
gram_columns = [column for column in columns if column.endswith("(g)")]
gram_df = food_info[gram_columns]
print(gram_df.head(3))

# Normalizing data
# The best way is to divide all rows by max value in column
max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat

# Sorting
# Allows the sorting of columns either in place or returning a new serise, 
# you can also choose if ascending or decending
food_info.sort_values(<string column>, <bool inplace:opt default:false>, <bool ascending:opt default:true>) 
food_info.sort_values("Sodium_(mg)")
food_info.sort_values("Sodium_(mg)", inplace=True)
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
