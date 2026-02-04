import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

jobs_sectors = [
    {'Companie' : 'Avivia', 'Sector': 'Manufacturing', 'Year': '2024', 'Skill1': 'Speed', 'Skill2': 'Precision'}, 
    {'Companie': 'Le Mont des Petits', 'Sector': 'Daycare', 'Year': '2021', 'Skill1': 'Caregiving', 'Skill2': 'Communication'}, 
    {'Companie': 'Groupe Villeneuve Electrique', 'Sector': 'Construction - Electrical', 'Year': '2020', 'Skill1': 'Problem Solving', 'Skill2': 'Logical Thinking', 'Skill3': 'Hardship Management', 'Skill4': 'Precision', 'Skill5': 'Teamwork'}, 
    {'Companie': 'Novo Inc', 'Sector': 'Food Production', 'Year': '', 'Skill1': 'Speed', 'Skill2': 'Cleanliness'}, 
    {'Companie': 'Top Tech Solutions Inc', 'Sector': 'Tech', 'Year': '2018', 'Skill1': 'Logical Thinking', 'Skill2': 'Problem Solving', 'Skill3': 'Teamwork', 'Skill4': 'Precision', 'Skill5': 'Organization', 'Skill6': 'Communication'}, 
    {'Companie': 'Ondel Inc', 'Sector': 'Construction - Electrical', 'Year': '2015', 'Skill1': 'Problem Solving', 'Skill2': 'Logical Thinking', 'Skill3': 'Hardship Management', 'Skill4': 'Precision', 'Skill5': 'Teamwork'},
    {'Companie': 'Subway', 'Sector': 'Food and Beverage', 'Year': '2014', 'Skill1': 'Customer Service', 'Skill2': 'Cleanliness', 'Skill3': 'Communication'},
    {'Companie': 'Silex Element', 'Sector': 'Manufacturing', 'Year': '2013', 'Skill1': 'Organization'},
    {'Companie': 'Renaud-Bray Warehouse', 'Sector': 'Manutension', 'Year': '2013', 'Skill1': 'Organization', 'Skill2': 'Teamwork'},
    {'Companie': 'Natrel', 'Sector': 'Food Production', 'Year': '2011', 'Skill1': 'Speed', 'Skill2': 'Cleanliness'},
    {'Companie': 'Le vent dans les voiles', 'Sector': 'Customer Service', 'Year': '2010', 'Skill1': 'Customer Service', 'Skill2': 'Cleanliness', 'Skill3': 'Communication'},
    {'Companie': 'Service Alimentaire Direct', 'Sector': 'Food Production', 'Year': '2006', 'Skill1': 'Customer Service', 'Skill2': 'Precision', 'Skill3': 'Communication'}]

## let's create a skills per sector heatmap

df = pd.DataFrame(jobs_sectors)

# Pivot: count how many times each skill appears per sector
skills_cols = [col for col in df.columns if col.startswith('Skill')]
skills_data = []

for _, row in df.iterrows(): # iterate through each row
    sector = row['Sector']
    for skill_col in skills_cols: # iterate through each skill column
        if pd.notna(row[skill_col]):
            skills_data.append({'Sector': sector, 'Skill': row[skill_col]})

# Create DataFrame from skills data
skills_df = pd.DataFrame(skills_data)

# Create a pivot table: sectors x skills
skills_matrix = pd.crosstab(skills_df['Sector'], skills_df['Skill'])

# Create heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(skills_matrix, annot=True, fmt='d', cmap='YlOrRd', cbar=True)
plt.title('Skills per Sector Heatmap')
plt.tight_layout()
plt.show()
