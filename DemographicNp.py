import pandas as pd

# Load the dataset (CSV format)
df = pd.read_csv('adult_data.csv')

# 1. How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
total_count = len(df)
bachelors_count = len(df[df['education'] == 'Bachelors'])
percentage_bachelors = (bachelors_count / total_count) * 100

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
advanced_education_rich = advanced_education[advanced_education['salary'] == '>50K']
percentage_advanced_education_rich = (len(advanced_education_rich) / len(advanced_education)) * 100

# 5. What percentage of people without advanced education make more than 50K?
non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
non_advanced_education_rich = non_advanced_education[non_advanced_education['salary'] == '>50K']
percentage_non_advanced_education_rich = (len(non_advanced_education_rich) / len(non_advanced_education)) * 100

# 6. What is the minimum number of hours a person works per week?
min_hours_worked = df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_workers = df[df['hours-per-week'] == min_hours_worked]
rich_min_hours_workers = min_hours_workers[min_hours_workers['salary'] == '>50K']
percentage_min_hours_rich = (len(rich_min_hours_workers) / len(min_hours_workers)) * 100

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_counts = df['native-country'].value_counts()
rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
highest_earning_country = (rich_country_counts / country_counts * 100).idxmax()
highest_earning_country_percentage = (rich_country_counts / country_counts * 100).max()

# 9. Identify the most popular occupation for those who earn >50K in India.
india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
top_occupation_india_rich = india_rich['occupation'].value_counts().idxmax()

# Print results
print("Race counts:\n", race_counts)
print("Average age of men:", average_age_men)
print("Percentage with Bachelor's degrees:", percentage_bachelors)
print("Percentage with advanced education earning >50K:", percentage_advanced_education_rich)
print("Percentage without advanced education earning >50K:", percentage_non_advanced_education_rich)
print("Minimum hours worked per week:", min_hours_worked)
print("Percentage of min hour workers earning >50K:", percentage_min_hours_rich)
print("Country with highest percentage of >50K earners:", highest_earning_country)
print("Highest percentage of >50K earners by country:", highest_earning_country_percentage)
print("Most popular occupation for those who earn >50K in India:", top_occupation_india_rich)
