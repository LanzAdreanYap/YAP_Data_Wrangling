import pandas as pd
# Create the four different dictionaries  of the different scores of the We Bare Bears per subject
b = {'Student': ['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}
be = {'Student': ['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
bea = {'Student': ['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,83]}
bear = {'Student': ['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}
# Convert each dictionary to a dataframe
bear1 = pd.DataFrame(b, columns = ['Student','Math'])
bear2 = pd.DataFrame(be, columns = ['Student','Electronics'])
bear3 = pd.DataFrame(bea, columns = ['Student','GEAS'])
bear4 = pd.DataFrame(bear, columns = ['Student','ESAT'])
# The pd.merge() function can only merge a maximum of 2 dataframes, joining matching rows from the two 
# First, merge the dataframes bear1 and bear2 and store it to summary
summary = pd.merge(bear1,bear2)
# Then, merge the dataframes summary and bear3 and store it to summary1
summary1 = pd.merge(summary,bear3)
# Finally, merge the last dataframe to have the final and summarized dataframe 
final = pd.merge(summary1,bear4)
# Display the summarized dataframes
print("Summarized Scores:")
print(final)
# Convert the final dataframe into a long format with new columns for Subject and Grades
long = pd.melt(final, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
# Change the name of two columns to, one is Subject and the other is Grades
long = long.rename(columns = {'variable':'Subjects','value':'Grades'})
print("")
# Display the long format of the summarized dataframe
print("Long Format of the Scores")
print(long)
# Save the dataframe 
We_Bare_Bares = long.to_csv('We Bare Bears.csv')