import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

jobs_sectors = [
    {'Company' : 'Avivia', 'Sector': 'Manufacturing', 'Year': '2024', 'Skills': 'Speed, Precision'}, 
    {'Company': 'Le Mont des Petits', 'Sector': 'Daycare', 'Year': '2021', 'Skills': 'Caregiving, Communication'}, 
    {'Company': 'Groupe Villeneuve Electrique', 'Sector': 'Construction - Electrical', 'Year': '2020', 'Skills': 'Problem Solving, Logical Thinking, Hardship Management, Precision, Teamwork'}, 
    {'Company': 'Novo Inc', 'Sector': 'Food Production', 'Year': '', 'Skills': 'Speed, Cleanliness'}, 
    {'Company': 'Top Tech Solutions Inc', 'Sector': 'Tech - Networking', 'Year': '2018', 'Skills': 'Logical Thinking, Problem Solving, Teamwork, Precision, Organization, Communication'},
    {'Company': 'Ondel Inc', 'Sector': 'Construction - Electrical', 'Year': '2015', 'Skills': 'Problem Solving, Logical Thinking, Hardship Management, Precision, Teamwork'},
    {'Company': 'Subway', 'Sector': 'Food and Beverage', 'Year': '2014', 'Skills': 'Customer Service, Cleanliness, Communication'},
    {'Company': 'Silex Element', 'Sector': 'Manufacturing', 'Year': '2013', 'Skills': 'Organization'},
    {'Company': 'Renaud-Bray Warehouse', 'Sector': 'Manutension', 'Year': '2013', 'Skills': 'Organization, Teamwork'},
    {'Company': 'Natrel', 'Sector': 'Food Production', 'Year': '2011', 'Skills': 'Speed, Cleanliness'},
    {'Company': 'Le vent dans les voiles', 'Sector': 'Customer Service', 'Year': '2010', 'Skills': 'Customer Service, Cleanliness, Communication'},
    {'Company': 'Service Alimentaire Direct', 'Sector': 'Food Production', 'Year': '2006', 'Skills': 'Customer Service, Precision, Communication'}]
## let's create a skills per sector heatmap

df = pd.DataFrame(jobs_sectors)

# Pivot: count how many times each skill appears per sector
skills_cols = [col for col in df.columns if col.startswith('Skill')]
skills_data = []

for index, row in df.iterrows():
    sector = row['Sector']
    skills = str(row['Skills']).split(',')
    for skill in skills:
        skills_data.append({'Sector': sector, 'Skill': skill.strip()})

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
