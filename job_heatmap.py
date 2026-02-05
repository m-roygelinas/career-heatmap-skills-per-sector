import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sectors = [
    {'Company' : 'Avivia', 'Sector': 'Manufacturing', 'Year': '2024', 'Skills': 'Speed, Precision, Problem Solving'}, 
    {'Company': 'Le Mont des Petits', 'Sector': 'Daycare', 'Year': '2021', 'Skills': 'Caregiving, Communication'}, 
    {'Company': 'Groupe Villeneuve Electrique', 'Sector': 'Construction - Electrical', 'Year': '2020', 'Skills': 'Problem Solving, Logical Thinking, Hardship Management, Precision, Teamwork'}, 
    {'Company': 'Novo Inc', 'Sector': 'Food Production', 'Year': '', 'Skills': 'Speed, Tidiness'}, 
    {'Company': 'Top Tech Solutions Inc', 'Sector': 'Tech - Networking', 'Year': '2018', 'Skills': 'Logical Thinking, Problem Solving, Teamwork, Precision, Organization, Communication'},
    {'Company': 'Ondel Inc', 'Sector': 'Construction - Electrical', 'Year': '2015', 'Skills': 'Problem Solving, Logical Thinking, Hardship Management, Precision, Teamwork'},
    {'Company': 'Subway', 'Sector': 'Food and Beverage', 'Year': '2014', 'Skills': 'Customer Service, Tidiness, Communication'},
    {'Company': 'Silex Element', 'Sector': 'Manufacturing', 'Year': '2013', 'Skills': 'Organization, Problem Solving'},
    {'Company': 'Renaud-Bray Warehouse', 'Sector': 'Manutension', 'Year': '2013', 'Skills': 'Organization, Teamwork'},
    {'Company': 'Natrel', 'Sector': 'Food Production', 'Year': '2011', 'Skills': 'Speed, Tidiness'},
    {'Company': 'Le vent dans les voiles', 'Sector': 'Customer Service', 'Year': '2010', 'Skills': 'Customer Service, Tidiness, Communication'},
    {'Company': 'Service Alimentaire Direct', 'Sector': 'Food Production', 'Year': '2006', 'Skills': 'Customer Service, Precision, Communication'},
    {'School': 'CFP LeChantier', 'Sector': 'Student', 'Year': '2015', 'Skills': 'Organization, Problem Solving, Logical Thinking, Precision, Teamwork'},
    {'School': 'UQAM', 'Sector': 'Student', 'Year': '2016', 'Skills': 'Organization, Problem Solving, Logical Thinking, Communication, Teamwork'}]

df = pd.DataFrame(sectors)

# Pivot: count how many times each skill appears per sector
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

# Add summary row
skills_matrix.loc['Total'] = skills_matrix.sum(axis=0)

# Mask zeros for better visualization
skills_matrix_masked = skills_matrix.replace(0, np.nan)
mask = skills_matrix_masked.isna()

# Create heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(skills_matrix, annot=True, fmt='d', cmap='plasma', cbar=True, mask=mask, linewidths=.5, linecolor='lightgrey', alpha=0.8)
plt.title('Skills per Sector Heatmap')
plt.tight_layout()
plt.show()
