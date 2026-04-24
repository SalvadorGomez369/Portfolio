import pandas as pd

1#Extract 

# Load the CSV file into a DataFrame
df = pd.read_csv('E:\\Visualstudio\\Work_Projects\\Data_analysis_projects\\arbnb\Resources\\Aemf1.csv')

df



2#Transform

# Load the CSV file into a DataFrame
df = pd.read_csv('E:\\Visualstudio\\Work_Projects\\Data_analysis_projects\\arbnb\\Resources\\Aemf1.csv')

# Print info of the DataFrame
df.info() #print(df.info())






# Load the CSV file into a DataFrame
df = pd.read_csv('E:\\Visualstudio\\Work_Projects\\Data_analysis_projects\\arbnb\\Resources\\Aemf1.csv')

# Get the frequency of each unique value in the 'name' column
name_counts = df['City'].value_counts()

# Print the result
name_counts



3#Load data
#Visualize
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('E:\\Visualstudio\\Work_Projects\\Data_analysis_projects\\arbnb\\Resources\\Aemf1.csv')

# Use boolean indexing to extract rows with the name 'Southland Leisure Centre'
slc = df[df.loc[:,'City'] == 'Paris']

p = slc.mean(numeric_only=True)
# slc.median(numeric_only=True)
# slc.mode(numeric_only=True)


# create a bar graph
p.plot(kind='barh')

# add title and axis labels
plt.title('Paris mean')
plt.xlabel('Mean')
plt.ylabel('Value')

# rotate x-axis labels for better visibility
#plt.xticks(rotation=0)

# display the plot
plt.show()