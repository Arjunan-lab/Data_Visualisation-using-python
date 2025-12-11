import pandas as pd
import matplotlib.pyplot as plt

# =============================
# PRODUCTS DATA
# =============================
print("="*50)
print("PRODUCTS DATA")
print("="*50)
products_df = pd.read_csv('products.csv')
print(products_df.head())
print(f"\nTotal products: {len(products_df)}")

# Products - Average Price by Category
plt.figure(figsize=(10, 6))
category_avg = products_df.groupby('category')['price'].mean().sort_values()
category_avg.plot(kind='bar', color='skyblue')
plt.title("Products: Average Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Products - Rating Distribution
plt.figure(figsize=(8, 5))
products_df['rating'].value_counts().sort_index().plot(kind='bar', color='orange')
plt.title("Products: Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Products - Price vs Rating
plt.figure(figsize=(8, 5))
plt.scatter(products_df['price'], products_df['rating'], alpha=0.5, c='green')
plt.title("Products: Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Products - Category Distribution
plt.figure(figsize=(8, 8))
products_df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Products: Category Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# =============================
# JOBS DATA
# =============================
print("\n" + "="*50)
print("JOBS DATA")
print("="*50)
jobs_df = pd.read_csv('jobs.csv')
print(jobs_df.head())
print(f"\nTotal jobs: {len(jobs_df)}")

# Jobs - Average Salary by Role
plt.figure(figsize=(10, 6))
role_salary = jobs_df.groupby('role')['salary_lpa'].mean().sort_values()
role_salary.plot(kind='barh', color='teal')
plt.title("Jobs: Average Salary by Role")
plt.xlabel("Average Salary (LPA)")
plt.ylabel("Role")
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

# Jobs - Jobs by Location
plt.figure(figsize=(10, 6))
jobs_df['location'].value_counts().plot(kind='bar', color='coral')
plt.title("Jobs: Distribution by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# Jobs - Jobs by Experience Level
plt.figure(figsize=(8, 8))
jobs_df['experience'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Jobs: Experience Level Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Jobs - Salary Distribution
plt.figure(figsize=(8, 5))
jobs_df['salary_lpa'].plot(kind='hist', bins=20, color='purple', edgecolor='black')
plt.title("Jobs: Salary Distribution")
plt.xlabel("Salary (LPA)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# =============================
# NEWS DATA
# =============================
print("\n" + "="*50)
print("NEWS DATA")
print("="*50)
news_df = pd.read_csv('news.csv')
print(news_df.head())
print(f"\nTotal news articles: {len(news_df)}")

# News - Articles by Source
plt.figure(figsize=(10, 6))
news_df['source'].value_counts().plot(kind='bar', color='steelblue')
plt.title("News: Articles by Source")
plt.xlabel("Source")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# News - Articles by Category (from headline)
news_df['category'] = news_df['headline'].str.split().str[0]
plt.figure(figsize=(10, 6))
news_df['category'].value_counts().plot(kind='bar', color='coral')
plt.title("News: Articles by Category")
plt.xlabel("Category")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# News - Category Distribution Pie Chart
plt.figure(figsize=(8, 8))
news_df['category'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#ff99cc'])
plt.title("News: Category Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# News - Articles Over Time
news_df['published_date'] = pd.to_datetime(news_df['published_date'])
news_df['month'] = news_df['published_date'].dt.to_period('M')

plt.figure(figsize=(10, 6))
news_df['month'].value_counts().sort_index().plot(kind='line', marker='o', color='darkgreen', linewidth=2)
plt.title("News: Articles Published Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Articles")
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# News - Top Authors
plt.figure(figsize=(10, 6))
news_df['author'].value_counts().head(10).plot(kind='barh', color='purple')
plt.title("News: Top 10 Authors by Article Count")
plt.xlabel("Number of Articles")
plt.ylabel("Author")
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("ALL GRAPHS COMPLETE!")
print("="*50)