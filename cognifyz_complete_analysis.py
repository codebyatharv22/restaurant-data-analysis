# Cognifyz Data Analysis Internship
# Complete analysis for Level 1, Level 2 and Level 3 tasks
# Dataset: Dataset.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

# Basic cleaning
df["Cuisines"] = df["Cuisines"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")

# ---------------- LEVEL 1 ----------------

# Task 1: Top Cuisines
cuisine_counts = df["Cuisines"].str.split(",").explode().str.strip().value_counts()
top3 = cuisine_counts.head(3)
top3_percentage = top3 / len(df) * 100
print("Top 3 cuisines:")
print(pd.DataFrame({"Restaurants": top3, "Percentage": top3_percentage.round(2)}))

# Task 2: City Analysis
city_counts = df["City"].value_counts()
city_avg_rating = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
print("City with most restaurants:", city_counts.idxmax(), city_counts.max())
print("Average rating by city:")
print(city_avg_rating)
print("City with highest average rating:", city_avg_rating.idxmax(), city_avg_rating.max())

# Task 3: Price Range Distribution
price_counts = df["Price range"].value_counts().sort_index()
price_percentage = price_counts / len(df) * 100
print(pd.DataFrame({"Restaurants": price_counts, "Percentage": price_percentage.round(2)}))
price_counts.plot(kind="bar")
plt.title("Restaurant Distribution by Price Range")
plt.xlabel("Price range")
plt.ylabel("Restaurants")
plt.show()

# Task 4: Online Delivery
delivery_percentage = df["Has Online delivery"].value_counts(normalize=True) * 100
delivery_rating = df.groupby("Has Online delivery")["Aggregate rating"].mean()
print("Online delivery percentage:")
print(delivery_percentage.round(2))
print("Average rating by online delivery:")
print(delivery_rating.round(3))

# ---------------- LEVEL 2 ----------------

# Task 1: Restaurant Ratings
rating_bins = pd.cut(
    df["Aggregate rating"],
    bins=[-0.01, 0.99, 1.99, 2.99, 3.99, 4.99, 5.0],
    labels=["0-0.99","1-1.99","2-2.99","3-3.99","4-4.99","5.0"]
)
print("Most common rating range:", rating_bins.value_counts().idxmax())
print("Average votes:", df["Votes"].mean())

# Task 2: Cuisine Combination
combo_counts = df["Cuisines"].value_counts()
combo_stats = df.groupby("Cuisines").agg(
    Restaurants=("Restaurant ID","count"),
    Avg_Rating=("Aggregate rating","mean"),
    Avg_Votes=("Votes","mean")
)
# Require at least 10 restaurants before comparing average ratings
qualified = combo_stats[combo_stats["Restaurants"] >= 10]
print("Most common cuisine combinations:")
print(combo_counts.head(10))
print("Highest-rated combinations with at least 10 restaurants:")
print(qualified.sort_values("Avg_Rating", ascending=False).head(10))

# Task 3: Geographic Analysis
plt.scatter(df["Longitude"], df["Latitude"], alpha=0.25, s=10)
plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Task 4: Restaurant Chains
name_counts = df["Restaurant Name"].value_counts()
chains = name_counts[name_counts > 1]
chain_stats = df[df["Restaurant Name"].isin(chains.index)].groupby("Restaurant Name").agg(
    Locations=("Restaurant ID","count"),
    Avg_Rating=("Aggregate rating","mean"),
    Avg_Votes=("Votes","mean")
).sort_values("Locations", ascending=False)
print("Restaurant chains:")
print(chain_stats.head(20))

# ---------------- LEVEL 3 ----------------

# Task 1: Restaurant Reviews
# The supplied dataset does NOT contain review-text comments.
# It contains "Rating text" only, which is a categorical label such as
# Excellent, Very Good, Good, Average, or Poor. Therefore:
# - Positive/negative review keywords cannot be extracted.
# - Average review length cannot be calculated.
# - Review length vs rating cannot be tested.
print("Review-text analysis cannot be completed because no review comment column exists.")

# Task 2: Votes Analysis
highest = df.loc[df["Votes"].idxmax()]
lowest = df.loc[df["Votes"].idxmin()]
correlation = df[["Votes","Aggregate rating"]].corr().iloc[0,1]
print("Highest votes:", highest[["Restaurant Name","City","Votes","Aggregate rating"]])
print("Lowest votes:", lowest[["Restaurant Name","City","Votes","Aggregate rating"]])
print("Votes-rating correlation:", round(correlation,4))

plt.scatter(df["Votes"], df["Aggregate rating"], alpha=0.25, s=10)
plt.title("Votes vs. Aggregate Rating")
plt.xlabel("Votes")
plt.ylabel("Aggregate rating")
plt.show()

# Task 3: Price Range vs Online Delivery and Table Booking
delivery_by_price = pd.crosstab(
    df["Price range"], df["Has Online delivery"], normalize="index"
) * 100

booking_by_price = pd.crosstab(
    df["Price range"], df["Has Table booking"], normalize="index"
) * 100

print("Online delivery by price range:")
print(delivery_by_price.round(2))
print("Table booking by price range:")
print(booking_by_price.round(2))
